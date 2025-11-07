# Careers by interest
career_by_area = {
    "Negocios": ["Licenciatura en Contaduria Publica y Finanzas", "Licenciatura en Desarrollo de Talento y Cultura Organizacional", "Licenciatura en Emprendimiento", "Licenciatura en Estrategia y Transformacion de Negocios", "Licenciatura en Inteligencia de Negocios", "Licenciatura en Mercadoctenia", "Licenciatura en Negocios Internacionales"],
    "Salud": ["Licenciatura en Biociencias", "Licenciatura en Nutricion y Bienestar Integral", "Licenciatura en Psicologia Clinica y de la Salud", "Medico Cirujano", "Medico Cirujano Odontologo"],
    "Estudios Creativos": ["Arquitectura", "Licenciatura en Comunicacion", "Licenciatura en Diseño", "Licenciatura en Letras Hispanicas", "Licenciatura en Tecnologia y Produccion Musical", "Licenciatura en Arte Digital", "Licenciatura en Innovacion Educativa"],
    "Ambiente Construido": ["Arquitectura", "Ingenieria Civil", "Licenciatura en Urbanismo"],
    "Derecho, Economia y Relaciones Internacionales": ["Licenciatura en Derecho", "Licenciatura en Economia", "Licenciatura en Gobierno y Transformacion Publica", "Licenciatura en Relaciones Internacionales"],
    "Innovacion y Transformacion": ["Ingenieria Biomedica", "Ingenieria Civil", "Ingenieria en Electronica", "Ingenieria Industrial y de Sistemas", "Ingenieria en Innovacion y Desarrollo", "Ingenieria Mecanica", "Ingenieria en Mecatronica"],
    "Computacion y Tecnologias de Informacion": ["Ingenieria en Robotica y Sistemas Digitales", "Ingenieria en Tecnologias Computacionales", "Ingenieria en Transformacion Digital de Negocios"],
    "Bioingenieria y Procesos Quimicos": ["Ingenieria en Alimentos" , "Ingenieria en Biosistemas Agroalimentarios", "Ingenieria en Biotecnologia", "Ingenieria en Desarrollo Sustentable", "Ingenieria Quimica"],
    "Ciencias Aplicadas": ["Ingenieria en Ciencia de Datos y Matematicas" , "Ingenieria en Fisica Industrial", "Ingenieria en Nanotecnologia"],
    }
    
print("\n\033[1;37mUniversity of interest:\033[0m Tecnologico de Monterrey\n\033[1;33mRecommended careers:\033[0m ")
# Career recommendation based on interest
for interest in selected_interest:
    careers = career_by_area.get(interest, [])
    if careers:
        print(f"\n{interest}:")
        for career in careers:
            print(f"  - {career}")
    else:
        print(f"\n{interest}: No careers found for this area.") 

# Display all careers with numbered list and allow selection to view details.
print("\n\033[1;33mAll available careers at Tecnologico de Monterrey:\033[1;37m")

# Build flattened list preserving order
all_careers = []
for area, careers in career_by_area.items():
    for career in careers:
        all_careers.append((career, area))

# Helper defaults and detail map builder
def _default_semesters_for(career_name: str) -> str:
    if "medico" in career_name.lower() or "odontologo" in career_name.lower():
        return "12"
    return "8"

def build_default_career_details():
    details = {}
    for career, area in all_careers:
        details[career] = {
            "Semestres": _default_semesters_for(career),
            "Descripcion": f"Programa orientado a formar profesionales en {area.lower()} con competencias teórico-prácticas relacionadas con {career}.",
            "Area": area
        }
    return details

career_details = build_default_career_details()

# Attempt to load Semestres/Descripcion/Area from careers.csv (case-insensitive column names)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "careers.csv")
if os.path.isfile(csv_path):
    try:
        df = pd.read_csv(csv_path)
        cols = {c.lower(): c for c in df.columns}
        career_col = next((cols[x] for x in ("career", "carrera", "name", "titulo") if x in cols), None)
        sem_col = next((cols[x] for x in ("semestres", "semesters", "duracion") if x in cols), None)
        desc_col = next((cols[x] for x in ("descripcion", "description", "descripcion_corta", "descripcion_larga") if x in cols), None)
        area_col = next((cols[x] for x in ("area", "facultad", "division") if x in cols), None)

        if career_col is None:
            print(f"\033[1;31mcareers.csv present but no career-name column found. Columns: {list(df.columns)}\033[0m")
        else:
            updated = 0
            for _, row in df.iterrows():
                name_val = str(row[career_col]).strip()
                if not name_val or name_val.lower() == "nan":
                    continue
                sem_val = str(row[sem_col]).strip() if sem_col and pd.notna(row[sem_col]) else _default_semesters_for(name_val)
                desc_val = str(row[desc_col]).strip() if desc_col and pd.notna(row[desc_col]) else f"Programa en {name_val}."
                area_val = str(row[area_col]).strip() if area_col and pd.notna(row[area_col]) else None
                if not area_val:
                    # infer area if possible
                    inferred = next((a for (c, a) in all_careers if c == name_val), None)
                    area_val = inferred if inferred else "Unknown"
                career_details[name_val] = {
                    "Semestres": sem_val,
                    "Descripcion": desc_val,
                    "Area": area_val
                }
                updated += 1
    except Exception as e:
        print("\033[1;31mFailed to read careers.csv:\033[0m", repr(e))
else:
    # keep generated defaults
    pass

# Print numbered careers
for idx, (career, area) in enumerate(all_careers, start=1):
    print(f"{idx}. {career}  ({area})")

# Selection loop: user can enter number to view details
while True:
    prompt = "\nIf you wish to see the details of an specific career, write the number of the career you want to view (or 'q' to quit): "
    choice = input(prompt).strip()
    if not choice:
        continue
    if choice.lower() in ("q", "quit", "exit"):
        print("\033[1;33mExiting career viewer.\033[0m")
        break
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(all_careers):
            career_name, _ = all_careers[idx]
            info = career_details.get(career_name)
            if not info:
                print("\033[1;31mCareer details not found for selected career.\033[0m")
            else:
                print("\n\033[1;33mCareer Details\033[0m")
                print(f"Career: {career_name}")
                print(f"Area: {info.get('Area', 'Unknown')}")
                print(f"Semestres: {info.get('Semestres', 'N/A')}")
                print(f"Descripcion: {info.get('Descripcion', 'No description available.')}")
            # after showing one career, allow selecting another or quitting
            continue
        else:
            print("\033[1;31mInvalid number. Please choose a number from the list.\033[0m")
            continue
    else:
        print("\033[1;31mPlease enter a career number or 'q' to quit.\033[0m")
        # Optionally provide fuzzy suggestions:
        suggestions = [c for (c, a) in all_careers if choice.lower() in c.lower()]
        if suggestions:
            print("\033[1;37mDid you mean:\033[0m")
            for s in suggestions[:10]:
                print(f"  - {s}")
areas={
    "Negocios":[
        "Licenciatura en Contaduria Publica y Finanzas",
        "Licenciatura en Desarrollo de Talento y Cultura Organizacional", 
        "Licenciatura en Emprendimiento",
        "Licenciatura en Estrategia y Transformacion de Negocios", 
        "Licenciatura en Inteligencia de Negocios",
        "Licenciatura en Mercadoctenia",
        "Licenciatura en Negocios Internacionales"
        ],
    "Salud":[
        "Licenciatura en Biociencias",
        "Licenciatura en Nutricion y Bienestar Integral", 
        "Licenciatura en Psicologia Clinica y de la Salud",
        "Medico Cirujano", 
        "Medico Cirujano Odontologo"
        ],
    "Estudios Creativos":[
        "Arquitectura",
        "Licenciatura en Comunicacion", 
        "Licenciatura en Design", 
        "Licenciatura en Letras Hispanicas",
        "Licenciatura en Tecnologia y Produccion Musical", 
        "Licenciatura en Arte Digital", 
        "Licenciatura en Innovacion Educativa"
        ],
    "Ambiente Construido":[
        "Arquitectura", 
        "Ingenieria Civil",
        "Licenciatura en Urbanismo"
        ],
    "Derecho, Economia y Relaciones Internacionales":[
        "Licenciatura en Derecho", 
        "Licenciatura en Economia", 
        "Licenciatura en Gobierno y Transformacion Publica", 
        "Licenciatura en Relaciones Internacionales"
        ],
    "Innovacion y Transformacion": [
        "Ingenieria Biomedica",
        "Ingenieria Civil",
        "Ingenieria en Electronica",
        "Ingenieria Industrial y de Sistemas", 
        "Ingenieria en Innovacion y Desarrollo",
        "Ingenieria Mecanica", 
        "Ingenieria en Mecatronica"
        ],
    "Computacion y Tecnologias de Informacion": [
        "Ingenieria en Robotica y Sistemas Digitales", 
        "Ingenieria en Tecnologias Computacionales",
        "Ingenieria en Transformacion Digital de Negocios"
       ],
     "Bioingenieria y Procesos Quimicos": [
        "Ingenieria en Alimentos" ,
        "Ingenieria en Biosistemas Agroalimentarios",
        "Ingenieria en Biotecnologia",
        "Ingenieria en Desarrollo Sustentable",
        "Ingenieria Quimica"
     ],
      "Ciencias Aplicadas": [
        "Ingenieria en Ciencia de Datos y Matematicas" ,
        "Ingenieria en Fisica Industrial", 
        "Ingenieria en Nanotecnologia"
         ],
    }

print(areas["Negocios"])
