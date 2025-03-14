import random

# Definición de personajes jugables
personajes_jugables = {
    "Ramses": {
        "nombre": "Ramses",
        "salud": 100,
        "nivel": 1,
        "experiencia": 0,
        "inventario": ["Piedra", "Poción de Cura"]
    },
    "Perseo": {
        "nombre": "Perseo",
        "salud": 100,
        "nivel": 1,
        "experiencia": 0,
        "inventario": ["Piedra", "Poción de Cura"]
    }
}

# Definición de NPCs
npcs = {
    "Hector": {"nombre": "Hector", "salud": 50, "nivel": 1},
    "César": {"nombre": "César", "salud": 50, "nivel": 1},
    "Miguelon": {"nombre": "Miguelon", "salud": 50, "nivel": 1},
    "Felipon": {"nombre": "Felipon", "salud": 50, "nivel": 1},
    "Diana": {"nombre": "Diana", "salud": 50, "nivel": 1},
    "Cicerón": {"nombre": "Cicerón", "salud": 50, "nivel": 1},
    "Séneca": {"nombre": "Séneca", "salud": 50, "nivel": 1},
    "Hera": {"nombre": "Hera", "salud": 50, "nivel": 1},
    "Antígona": {"nombre": "Antígona", "salud": 50, "nivel": 1}
}

# Sistema de combate
def combate(jugador, enemigo):
    print(f"¡Comienza el combate entre {jugador['nombre']} y {enemigo['nombre']}!")
    while jugador['salud'] > 0 and enemigo['salud'] > 0:
        # Turno del jugador
        print("\nTu turno:")
        print("1. Atacar")
        print("2. Usar Poción de Cura")
        print("3. Huir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            daño_jugador = max(0, random.randint(10, 20) - random.randint(0, 5))
            enemigo['salud'] -= daño_jugador
            print(f"{jugador['nombre']} causa {daño_jugador} de daño a {enemigo['nombre']}. Salud de {enemigo['nombre']}: {enemigo['salud']}")
        elif opcion == "2" and "Poción de Cura" in jugador['inventario']:
            jugador['salud'] = min(100, jugador['salud'] + 20)
            jugador['inventario'].remove("Poción de Cura")
            print(f"{jugador['nombre']} usa una Poción de Cura. Salud de {jugador['nombre']}: {jugador['salud']}")
        elif opcion == "3":
            if random.random() < 0.5:
                print(f"{jugador['nombre']} ha logrado huir del combate.")
                return
            else:
                print(f"{jugador['nombre']} no ha podido huir del combate.")
        else:
            print("Opción no válida o no tienes pociones de cura.")
        
        if enemigo['salud'] <= 0:
            break

        # Turno del enemigo
        daño_enemigo = max(0, random.randint(5, 15) - random.randint(0, 5))
        jugador['salud'] -= daño_enemigo
        print(f"{enemigo['nombre']} causa {daño_enemigo} de daño a {jugador['nombre']}. Salud de {jugador['nombre']}: {jugador['salud']}")
        
    if jugador['salud'] > 0:
        print(f"{jugador['nombre']} ha ganado el combate!")
        jugador['experiencia'] += 10
        if jugador['experiencia'] >= 100:
            jugador['nivel'] += 1
            jugador['experiencia'] = 0
            print(f"{jugador['nombre']} ha subido de nivel! Ahora es nivel {jugador['nivel']}")
        return True
    else:
        print(f"{enemigo['nombre']} ha ganado el combate!")
        return False

# Sistema de inventario
def mostrar_inventario(jugador):
    print(f"Inventario de {jugador['nombre']}: {jugador['inventario']}")

def añadir_al_inventario(jugador, item):
    jugador['inventario'].append(item)
    print(f"{item} ha sido añadido al inventario de {jugador['nombre']}")

# Interacción y diálogos
def diálogo_con_npc(npc, texto):
    print(f"{npc['nombre']}: {texto}")

# Funciones principales del juego
def elegir_personaje():
    print("Elige tu personaje:")
    for nombre in personajes_jugables:
        print(nombre)
    eleccion = input("Escribe el nombre de tu personaje: ")
    if eleccion in personajes_jugables:
        return personajes_jugables[eleccion]
    else:
        print("Personaje no válido, eligiendo Ramses por defecto.")
        return personajes_jugables["Ramses"]

def misión(jugador, misión_num):
    diálogos = [
        {
            "npc": "Hector", 
            "texto": "Necesito que vayas a la cueva y consigas una piedra especial.",
            "decisiones": [
                {
                    "texto": "Llegas a un río. ¿Cómo deseas cruzarlo?",
                    "opciones": {
                        "1": {"texto": "Nadar", "resultado": "Lograste cruzar el río nadando sin problemas.", "fallo": "Fuiste arrastrado por la corriente y perdiste salud.", "probabilidad": 0.7, "daño": 20},
                        "2": {"texto": "Usar un puente", "resultado": "Cruzaste el puente sin problemas.", "fallo": "El puente se derrumbó y caíste al río, perdiendo salud.", "probabilidad": 0.9, "daño": 30}
                    }
                }
            ]
        },
        {
            "npc": "César", 
            "texto": "Enfréntate a Miguelon en combate y trae su arma.",
            "decisiones": [
                {
                    "texto": "Te encuentras con un grupo de enemigos. ¿Cómo deseas proceder?",
                    "opciones": {
                        "1": {"texto": "Atacar de frente", "resultado": "Lograste derrotar a los enemigos.", "fallo": "Fuiste herido gravemente.", "probabilidad": 0.6, "daño": 40},
                        "2": {"texto": "Rodearlos y atacarlos por sorpresa", "resultado": "Los tomaste por sorpresa y los derrotaste fácilmente.", "fallo": "Fueron alertados y te hirieron.", "probabilidad": 0.8, "daño": 20}
                    }
                }
            ]
        },
        {
            "npc": "Diana", 
            "texto": "Encuentra la planta curativa en el bosque.",
            "decisiones": [
                {
                    "texto": "El camino se divide en dos. ¿Cuál eliges?",
                    "opciones": {
                        "1": {"texto": "El camino de la derecha", "resultado": "Encontraste la planta curativa.", "fallo": "Te perdiste en el bosque y perdiste salud.", "probabilidad": 0.7, "daño": 15},
                        "2": {"texto": "El camino de la izquierda", "resultado": "Llegaste a un claro y encontraste la planta curativa.", "fallo": "Caminaste en círculos y te agotaste.", "probabilidad": 0.7, "daño": 15}
                    }
                }
            ]
        },
        {
            "npc": "Cicerón", 
            "texto": "Ayúdame a defender el campamento de los enemigos.",
            "decisiones": [
                {
                    "texto": "Los enemigos se acercan. ¿Qué haces?",
                    "opciones": {
                        "1": {"texto": "Defender la entrada principal", "resultado": "Defendiste el campamento con éxito.", "fallo": "Fueron demasiados y te hirieron.", "probabilidad": 0.6, "daño": 30},
                        "2": {"texto": "Atacar desde los flancos", "resultado": "Los derrotaste desde los flancos.", "fallo": "Te emboscaron y te hirieron.", "probabilidad": 0.7, "daño": 25}
                    }
                }
            ]
        },
        {
            "npc": "Séneca", 
            "texto": "Recoge madera para construir herramientas.",
            "decisiones": [
                {
                    "texto": "Encuentras un árbol grande. ¿Cómo lo derribas?",
                    "opciones": {
                        "1": {"texto": "Usar tus herramientas", "resultado": "Derribaste el árbol y recogiste madera.", "fallo": "La herramienta se rompió y te lastimaste.", "probabilidad": 0.8, "daño": 10},
                        "2": {"texto": "Empujarlo con fuerza", "resultado": "Lograste derribar el árbol con tu fuerza.", "fallo": "Te cayó una rama encima y te hirió.", "probabilidad": 0.5, "daño": 20}
                    }
                }
            ]
        },
        {
            "npc": "Hera", 
            "texto": "Busca agua en el río cercano.",
            "decisiones": [
                {
                    "texto": "El río está lleno de piedras. ¿Cómo cruzas?",
                    "opciones": {
                        "1": {"texto": "Saltar de piedra en piedra", "resultado": "Cruzaste el río sin problemas.", "fallo": "Resbalaste y te golpeaste.", "probabilidad": 0.7, "daño": 15},
                        "2": {"texto": "Caminar por el agua", "resultado": "Cruzaste el río, aunque te mojaste.", "fallo": "Te caíste y te lastimaste.", "probabilidad": 0.8, "daño": 10}
                    }
                }
            ]
        },
        {
            "npc": "Antígona", 
            "texto": "Derrota al jefe final en la montaña.",
            "decisiones": [
                {
                    "texto": "El jefe final te espera. ¿Cómo lo enfrentas?",
                    "opciones": {
                        "1": {"texto": "Atacar de frente", "resultado": "Lo derrotaste en un combate épico.", "fallo": "Fuiste herido gravemente.", "probabilidad": 0.5, "daño": 50},
                        "2": {"texto": "Usar una estrategia de emboscada", "resultado": "Lo derrotaste con astucia.", "fallo": "Te descubrió y te hirió.", "probabilidad": 0.7, "daño": 30}
                    }
                }
            ]
        }
    ]

    if misión_num < len(diálogos):
        misión = diálogos[misión_num]
        npc = misión["npc"]
        texto = misión["texto"]
        diálogo_con_npc(npcs[npc], texto)
        
        for decisión in misión["decisiones"]:
            print(decisión["texto"])
            for opcion, detalles in decisión["opciones"].items():
                print(f"{opcion}. {detalles['texto']}")
            eleccion = input("Elige una opción: ")
            if eleccion in decisión["opciones"]:
                detalles = decisión["opciones"][eleccion]
                if random.random() < detalles["probabilidad"]:
                    print(detalles["resultado"])
                else:
                    print(detalles["fallo"])
                    jugador["salud"] -= detalles["daño"]
            else:
                print("Opción no válida.")
        
        enemigo = npcs[random.choice(list(npcs.keys()))]
        if combate(jugador, enemigo):
            añadir_al_inventario(jugador, "Poción de Cura")
        diálogo_con_npc(npcs[npc], "¡Gracias por completar la misión!")

def introducción():
    print("Bienvenido a 'Ancestors', un juego de rol ambientado en la prehistoria.")
    print("Te encontrarás en un mundo lleno de aventuras y peligros.")
    print("Tu objetivo es completar misiones, mejorar a tu personaje y derrotar al jefe final.")
    print("Buena suerte, valiente guerrero.")

def juego():
    introducción()
    jugador = elegir_personaje()
    print(f"Bienvenido al juego, {jugador['nombre']}!")
    misión_num = 0
    while misión_num < 7:
        misión(jugador, misión_num)
        if jugador['salud'] <= 0:
            print("Has muerto, regresando al último checkpoint...")
            jugador['salud'] = 100
        misión_num += 1
    print("¡Felicidades! Has completado todas las misiones y derrotado al jefe final.")

# Iniciar el juego
juego()