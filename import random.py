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
    print(f"\n¡Comienza el combate entre {jugador['nombre']} y {enemigo['nombre']}!")
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
            print(f"\n{jugador['nombre']} causa {daño_jugador} de daño a {enemigo['nombre']}.")
            print(f"Salud de {enemigo['nombre']}: {enemigo['salud']}")
        elif opcion == "2" and "Poción de Cura" in jugador['inventario']:
            jugador['salud'] = min(100, jugador['salud'] + 20)
            jugador['inventario'].remove("Poción de Cura")
            print(f"\n{jugador['nombre']} usa una Poción de Cura.")
            print(f"Salud de {jugador['nombre']}: {jugador['salud']}")
        elif opcion == "3":
            if random.random() < 0.5:
                print(f"\n{jugador['nombre']} ha logrado huir del combate.")
                return False
            else:
                print(f"\n{jugador['nombre']} no ha podido huir del combate.")
        else:
            print("\nOpción no válida o no tienes pociones de cura.")
        
        if enemigo['salud'] <= 0:
            break

        # Turno del enemigo
        daño_enemigo = max(0, random.randint(5, 15) - random.randint(0, 5))
        jugador['salud'] -= daño_enemigo
        print(f"\n{enemigo['nombre']} causa {daño_enemigo} de daño a {jugador['nombre']}.")
        print(f"Salud de {jugador['nombre']}: {jugador['salud']}")
        
    if jugador['salud'] > 0:
        print(f"\n¡{jugador['nombre']} ha ganado el combate!")
        jugador['experiencia'] += 10
        if jugador['experiencia'] >= 100:
            jugador['nivel'] += 1
            jugador['experiencia'] = 0
            print(f"\n¡{jugador['nombre']} ha subido de nivel! Ahora es nivel {jugador['nivel']}")
        return True
    else:
        print(f"\n¡{enemigo['nombre']} ha ganado el combate!")
        return False

# Sistema de inventario
def mostrar_inventario(jugador):
    print(f"\nInventario de {jugador['nombre']}: {jugador['inventario']}")

def añadir_al_inventario(jugador, item):
    jugador['inventario'].append(item)
    print(f"\n{item} ha sido añadido al inventario de {jugador['nombre']}")

# Interacción y diálogos
def diálogo_con_npc(npc, texto):
    print(f"\n{npc['nombre']}: {texto}")

# Funciones principales del juego
def elegir_personaje():
    print("Elige tu personaje:")
    for nombre in personajes_jugables:
        print(f"- {nombre}")
    eleccion = input("Escribe el nombre de tu personaje: ")
    if eleccion in personajes_jugables:
        return personajes_jugables[eleccion]
    else:
        print("\nPersonaje no válido, eligiendo Ramses por defecto.")
        return personajes_jugables["Ramses"]

def misión(jugador, misión_num):
    diálogos = [
        {
            "npc": "Hector", 
            "texto": "Necesito que vayas a la cueva y consigas una piedra especial. Este recurso nos ayudará a fabricar herramientas vitales para sobrevivir.",
            "decisiones": [
                {
                    "texto": "Al salir de tu aldea, te encuentras con un ancho río. ¿Cómo deseas cruzarlo?",
                    "opciones": {
                        "1": {"texto": "Nadar", "resultado": "Lograste cruzar el río nadando sin problemas.", "fallo": "La corriente te arrastró y perdiste salud.", "probabilidad": 0.7, "daño": 20},
                        "2": {"texto": "Buscar un puente natural", "resultado": "Encontraste un puente formado por raíces y rocas y lo cruzaste con seguridad.", "fallo": "El puente se resbaló y caíste al agua, perdiendo salud.", "probabilidad": 0.9, "daño": 30}
                    }
                },
                {
                    "texto": "Más adelante, encuentras una bifurcación: un sendero seguro pero largo, y otro corto pero peligroso. ¿Qué camino tomas?",
                    "opciones": {
                        "1": {"texto": "El camino seguro", "resultado": "Llegaste a la cueva sin incidentes, aunque te tomó más tiempo.", "fallo": "Te topaste con una bestia salvaje y sufriste heridas leves.", "probabilidad": 0.8, "daño": 15},
                        "2": {"texto": "El camino peligroso", "resultado": "Llegaste rápidamente a la cueva.", "fallo": "Caíste en una trampa oculta y te lesionaste.", "probabilidad": 0.6, "daño": 25}
                    }
                },
                {
                    "texto": "Dentro de la oscura cueva, un resplandor ilumina una esquina. ¿Cómo procedes?",
                    "opciones": {
                        "1": {"texto": "Acercarte con cautela", "resultado": "Descubriste la piedra especial oculta tras un muro de roca.", "fallo": "Un murciélago gigante te atacó y te hirió.", "probabilidad": 0.7, "daño": 20},
                        "2": {"texto": "Correr hacia el brillo", "resultado": "Recogiste la piedra rápidamente.", "fallo": "Tropezaste en la oscuridad y sufriste heridas leves.", "probabilidad": 0.5, "daño": 15}
                    }
                }
            ]
        },
        {
            "npc": "César", 
            "texto": "Tu siguiente tarea es enfrentarte a Miguelon y recuperar su arma, esencial para la defensa de la tribu.",
            "decisiones": [
                {
                    "texto": "En el camino, te topas con un grupo de enemigos. ¿Cómo decides proceder?",
                    "opciones": {
                        "1": {"texto": "Atacar de frente", "resultado": "Nuestros ataques coordinados derribaron a los enemigos.", "fallo": "Recibiste un golpe crítico y resultaste herido.", "probabilidad": 0.6, "daño": 40},
                        "2": {"texto": "Rodearlos para atacar por sorpresa", "resultado": "Sorprendiste al grupo y los eliminaste antes de que reaccionaran.", "fallo": "El plan falló y fuiste atacado sorpresivamente.", "probabilidad": 0.8, "daño": 20}
                    }
                },
                {
                    "texto": "Finalmente, ves a Miguelon, quien descansa en un claro. ¿Qué haces?",
                    "opciones": {
                        "1": {"texto": "Desafiarlo a un duelo singular", "resultado": "Lograste derrotarlo en un combate justo y recuperaste su arma.", "fallo": "Subestimaste su fuerza y salieron herido ambos.", "probabilidad": 0.7, "daño": 30},
                        "2": {"texto": "Atacar sigilosamente", "resultado": "Sorprendiste a Miguelon y le arrebataste el arma sin ser detectado.", "fallo": "No logró darte tiempo para actuar y te contraatacó.", "probabilidad": 0.5, "daño": 25}
                    }
                }
            ]
        },
        {
            "npc": "Diana", 
            "texto": "La salud de nuestra tribu depende de una planta curativa que se encuentra en el denso bosque. Encuéntrala para poder curar a los heridos.",
            "decisiones": [
                {
                    "texto": "Al adentrarte en el bosque, el camino se divide. ¿Qué ruta eliges?",
                    "opciones": {
                        "1": {"texto": "El camino de la derecha, rodeado de altos árboles", "resultado": "Descubriste la planta curativa en un claro iluminado por el sol.", "fallo": "Te perdiste en el bosque y sufriste un leve ataque de los elementos.", "probabilidad": 0.7, "daño": 15},
                        "2": {"texto": "El camino de la izquierda, más agreste y sombrío", "resultado": "Encontraste una pequeña pradera donde crece la planta curativa.", "fallo": "El sendero te confundió y te agotaste, perdiendo algo de salud.", "probabilidad": 0.7, "daño": 15}
                    }
                },
                {
                    "texto": "De repente, escuchas un ruido extraño en los arbustos. ¿Qué decides hacer?",
                    "opciones": {
                        "1": {"texto": "Investigar el ruido", "resultado": "Descubriste hierbas medicinales adicionales que fortalecieron tu inventario.", "fallo": "Un animal salvaje salió de entre los arbustos y te atacó.", "probabilidad": 0.6, "daño": 20},
                        "2": {"texto": "Ignorar el ruido y continuar", "resultado": "Llegaste a tu destino sin incidentes.", "fallo": "La distracción te hizo caer en una pequeña trampa del bosque.", "probabilidad": 0.8, "daño": 10}
                    }
                }
            ]
        },
        {
            "npc": "Cicerón", 
            "texto": "La seguridad de nuestro campamento pende de un hilo. Ayúdame a defenderlo contra los enemigos que atacan en oleadas.",
            "decisiones": [
                {
                    "texto": "Los enemigos comienzan a llegar. ¿Cuál es tu estrategia?",
                    "opciones": {
                        "1": {"texto": "Defender la entrada principal con tus compañeros", "resultado": "Con una defensa sólida, lograste repeler el ataque.", "fallo": "Fueron demasiados y sufriste heridas importantes.", "probabilidad": 0.6, "daño": 30},
                        "2": {"texto": "Atacar desde los flancos para sorprenderlos", "resultado": "Con táctica y rapidez, eliminaste a varios enemigos.", "fallo": "El ataque por sorpresa falló y fuiste emboscado.", "probabilidad": 0.7, "daño": 25}
                    }
                },
                {
                    "texto": "Tras la batalla, identificas al líder enemigo. ¿Qué decides hacer?",
                    "opciones": {
                        "1": {"texto": "Enfrentar al líder directamente", "resultado": "Lo derrotaste tras un combate intenso, protegiendo al campamento.", "fallo": "El líder demostró ser más fuerte de lo esperado.", "probabilidad": 0.5, "daño": 40},
                        "2": {"texto": "Reunir a tus aliados para un ataque coordinado", "resultado": "La estrategia colaborativa resultó en la victoria contra el líder.", "fallo": "La coordinación falló y varios resultaron heridos.", "probabilidad": 0.7, "daño": 30}
                    }
                }
            ]
        },
        {
            "npc": "Séneca", 
            "texto": "Para construir nuestras herramientas y armas, necesitamos recolectar madera. Dirígete al bosque y recoge suficiente material.",
            "decisiones": [
                {
                    "texto": "Encuentras un robusto árbol. ¿Cómo lo derribas?",
                    "opciones": {
                        "1": {"texto": "Utilizar tus herramientas adecuadas", "resultado": "Con precisión, derribaste el árbol y recogiste buena madera.", "fallo": "La herramienta cedió y sufriste un pequeño accidente.", "probabilidad": 0.8, "daño": 10},
                        "2": {"texto": "Empujar el árbol con tu fuerza", "resultado": "Con tu fuerza, lograste derribarlo y recoger la madera necesaria.", "fallo": "Una rama cayó sobre ti, causándote daño.", "probabilidad": 0.5, "daño": 20}
                    }
                },
                {
                    "texto": "Mientras trabajas, escuchas un ruido en el bosque. ¿Qué haces?",
                    "opciones": {
                        "1": {"texto": "Investigar el origen del ruido", "resultado": "Descubriste una reserva de recursos naturales adicionales.", "fallo": "Fuiste atacado por un animal territorial.", "probabilidad": 0.6, "daño": 15},
                        "2": {"texto": "Ignorar el ruido y continuar con la recolección", "resultado": "Recolectaste madera suficiente sin interrupciones.", "fallo": "El ruido se convirtió en un peligro inesperado y fuiste herido.", "probabilidad": 0.7, "daño": 20}
                    }
                }
            ]
        },
        {
            "npc": "Hera", 
            "texto": "El agua es esencial para nuestra supervivencia. Dirígete al río y recoge agua limpia.",
            "decisiones": [
                {
                    "texto": "Te encuentras con un río lleno de piedras y rápidos. ¿Cómo cruzas?",
                    "opciones": {
                        "1": {"texto": "Saltar de piedra en piedra", "resultado": "Con agilidad, alcanzaste la otra orilla sin incidentes.", "fallo": "Resbalaste, cayendo y perdiendo salud.", "probabilidad": 0.7, "daño": 15},
                        "2": {"texto": "Caminar por las rocas hasta encontrar un paso seguro", "resultado": "Con cuidado, cruzaste el río, aunque te mojaste todo.", "fallo": "Despistado, tropezaste en las rocas y te lesionaste.", "probabilidad": 0.8, "daño": 10}
                    }
                },
                {
                    "texto": "Al llegar, descubres una fuente de agua cristalina. ¿Qué haces?",
                    "opciones": {
                        "1": {"texto": "Recolectar agua de inmediato", "resultado": "Llenaste tus ánforas con agua fresca.", "fallo": "La fuente resultó tener impurezas y te afectó la salud.", "probabilidad": 0.6, "daño": 20},
                        "2": {"texto": "Inspeccionar cuidadosamente la fuente antes de recolectar", "resultado": "Confirmaste que el agua era segura y la recogiste sin problemas.", "fallo": "La inspección demoró demasiado y perdiste algo de tiempo vital.", "probabilidad": 0.8, "daño": 10}
                    }
                }
            ]
        },
        {
            "npc": "Antígona", 
            "texto": "El destino de nuestra tribu depende de que derrotes al jefe final en la montaña. Esta victoria nos abrirá el camino hacia una nueva era de libertad.",
            "decisiones": [
                {
                    "texto": "En la cumbre, el jefe final te espera con fiereza. ¿Cómo lo enfrentas?",
                    "opciones": {
                        "1": {"texto": "Atacar frontalmente sin temerle", "resultado": "En un combate épico, lograste derribarlo derrotando a la bestia.", "fallo": "El jefe final mostró una fuerza descomunal y sufriste graves heridas.", "probabilidad": 0.5, "daño": 50},
                        "2": {"texto": "Planificar una emboscada desde las sombras", "resultado": "Con astucia, utilizaste el terreno a tu favor y lo eliminaste.", "fallo": "Tu estrategia fue descubierta y el contraataque te lastimó.", "probabilidad": 0.7, "daño": 30}
                    }
                },
                {
                    "texto": "Tras la victoria, encuentras un antiguo cofre lleno de tesoros. ¿Qué decides hacer?",
                    "opciones": {
                        "1": {"texto": "Abrir el cofre inmediatamente para tomar el botín", "resultado": "Obtienes ricos recursos para fortalecer a la tribu.", "fallo": "Una trampa oculta en el cofre te lanzó al suelo, causándote daño.", "probabilidad": 0.6, "daño": 20},
                        "2": {"texto": "Inspeccionar cuidadosamente el cofre antes de abrirlo", "resultado": "Desactivas la trampa y recoges el tesoro sin peligro.", "fallo": "La inspección te tomó demasiado tiempo y perdiste concentración.", "probabilidad": 0.8, "daño": 10}
                    }
                }
            ]
        }
    ]

    if misión_num < len(diálogos):
        misión_actual = diálogos[misión_num]
        npc_nombre = misión_actual["npc"]
        texto = misión_actual["texto"]
        diálogo_con_npc(npcs[npc_nombre], texto)
        
        for decisión in misión_actual["decisiones"]:
            print("\n" + decisión["texto"])
            for opcion, detalles in decisión["opciones"].items():
                print(f"{opcion}. {detalles['texto']}")
            eleccion = input("Elige una opción: ")
            if eleccion in decisión["opciones"]:
                detalles = decisión["opciones"][eleccion]
                if random.random() < detalles["probabilidad"]:
                    print(f"\n{detalles['resultado']}")
                else:
                    print(f"\n{detalles['fallo']}")
                    jugador["salud"] -= detalles["daño"]
            else:
                print("\nOpción no válida. Pierdes una oportunidad y avanzas con cierto riesgo.")
        
        # Combate final para la misión
        enemigo = npcs[random.choice(list(npcs.keys()))]
        if combate(jugador, enemigo):
            añadir_al_inventario(jugador, "Poción de Cura")
        diálogo_con_npc(npcs[npc_nombre], "¡Gracias por completar la misión!")
    else:
        print("\nNo hay más misiones disponibles.")

def introducción():
    print("\nBienvenido a 'Ancestors', un juego de rol ambientado en la prehistoria.")
    print("Te encontrarás en un mundo salvaje lleno de aventuras, desafíos y decisiones cruciales.")
    print("Tu objetivo es sobrevivir, completar misiones, mejorar a tu personaje y construir un futuro para nuestra tribu.")
    print("¡Buena suerte, valiente guerrero!")

def juego():
    introducción()
    jugador = elegir_personaje()
    print(f"\nBienvenido al juego, {jugador['nombre']}!")
    misión_num = 0
    while misión_num < len(npcs):  # Puedes ajustar el número de misiones
        print(f"\n--- Misión {misión_num + 1} ---")
        éxito = misión(jugador, misión_num)
        if jugador['salud'] <= 0:
            print("\nHas caído en la batalla, pero tu espíritu perdura. Regresando al último checkpoint...")
            jugador['salud'] = 100
        misión_num += 1
    print("\n¡Felicidades! Has completado las pruebas de Ancestors y conducido a tu tribu hacia un nuevo amanecer.")

# Iniciar el juego
if __name__ == "__main__":
    juego()