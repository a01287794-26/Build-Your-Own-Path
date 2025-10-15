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

# Display all careers
print("\n\033[1;33mAll available careers at Tecnologico de Monterrey:\033[0m")
for area, careers in career_by_area.items():
    print(f"{area}:")
    for career in careers:
        print(f"  - {career}")
