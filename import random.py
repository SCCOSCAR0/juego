import random

# Datos iniciales de personajes y NPCs
personajes_jugables = {
    "Ramses": {"salud": 100, "nivel": 1, "experiencia": 0, "inventario": [], "ataque": 20, "defensa": 5, "armas": []},
    "Perseo": {"salud": 100, "nivel": 1, "experiencia": 0, "inventario": [], "ataque": 18, "defensa": 7, "armas": []}
}

npcs = {
    "Hector": {"salud": 50, "ataque": 10, "defensa": 3, "armas": ["Espada Rústica"]},
    "César": {"salud": 60, "ataque": 15, "defensa": 5, "armas": ["Hacha de Piedra"]},
    "Miguelon": {"salud": 45, "ataque": 12, "defensa": 4, "armas": ["Cuchillo de Roca"]},
    "Felipon": {"salud": 55, "ataque": 14, "defensa": 6, "armas": ["Piedra afilada"]},
    "Diana": {"salud": 40, "ataque": 8, "defensa": 3, "armas": ["Daga de Piedra"]},
    "Cicerón": {"salud": 70, "ataque": 20, "defensa": 7, "armas": ["Lanza de Madera"]},
    "Séneca": {"salud": 50, "ataque": 10, "defensa": 4, "armas": ["Espada Cortante"]},
    "Hera": {"salud": 60, "ataque": 16, "defensa": 5, "armas": ["Hacha de Guerra"]},
    "Antígona": {"salud": 45, "ataque": 12, "defensa": 4, "armas": ["Cuchillo de Piedra"]},
}

# Función de combate entre jugador y NPC
def atacar(jugador, enemigo):
    print(f"\n{jugador} ha iniciado un combate contra {enemigo}!\n")
    
    while jugador["salud"] > 0 and enemigo["salud"] > 0:
        print(f"\n{jugador} tiene {jugador['salud']} salud.")
        print(f"{enemigo} tiene {enemigo['salud']} salud.")
        
        # Elegir acción
        print("\n¿Qué ataque quieres hacer?")
        print("1. Ataque básico")
        print("2. Ataque fuerte")
        print("3. Defensa")
        eleccion = input("Elige tu acción (1-3): ")
        
        if eleccion == "1":
            daño = jugador["ataque"] - enemigo["defensa"]
            daño = max(daño, 0)  # Evitar daño negativo
            enemigo["salud"] -= daño
            print(f"\n{jugador} realiza un ataque básico a {enemigo}, causando {daño} de daño.")
        elif eleccion == "2":
            daño = (jugador["ataque"] * 1.5) - enemigo["defensa"]
            daño = max(daño, 0)  # Evitar daño negativo
            enemigo["salud"] -= daño
            print(f"\n{jugador} realiza un ataque fuerte a {enemigo}, causando {daño} de daño.")
        elif eleccion == "3":
            jugador["defensa"] += 5
            print(f"\n{jugador} se prepara para defenderse el próximo turno.")
        else:
            print("\nOpción no válida, elige una acción entre 1 y 3.")
        
        # El enemigo también ataca
        if enemigo["salud"] > 0:
            daño = enemigo["ataque"] - jugador["defensa"]
            daño = max(daño, 0)  # Evitar daño negativo
            jugador["salud"] -= daño
            print(f"\n{enemigo} ataca a {jugador}, causando {daño} de daño.")
        
        # Verificar si alguno ha sido derrotado
        if jugador["salud"] <= 0:
            print(f"\n{jugador} ha sido derrotado... ¡Game Over!")
            return False
        if enemigo["salud"] <= 0:
            print(f"\n{enemigo} ha sido derrotado.")
            # El jugador gana experiencia y roba armas
            jugador["experiencia"] += 10
            jugador["inventario"].append(random.choice(enemigo["armas"]))
            print(f"{jugador} ha ganado 10 de experiencia y ha robado un arma: {jugador['inventario'][-1]}")
            return True

# Misiones y diálogos
def dialogo_mision(mision):
    if mision == "explorar_cueva":
        print("\nTe encuentras con una cueva oscura. Un anciano te dice: 'Dentro de esta cueva habitan tribus que pueden ser peligrosas, ¿quieres aventurarte?'")
        respuesta = input("Responde (Sí/No): ").lower()
        if respuesta == "sí":
            print("\nDecides entrar. Estás listo para enfrentarte a lo que venga.")
            return True
        else:
            print("\nDecides no entrar en la cueva y regresas a tu aldea.")
            return False
    elif mision == "fabricar_armas":
        print("\nUn sabio en el poblado te dice: 'Con piedras y cuchillos podrías fabricarte nuevas armas. ¿Te gustaría aprender a hacerlo?'")
        respuesta = input("Responde (Sí/No): ").lower()
        if respuesta == "sí":
            print("\nEl sabio te enseña a fabricar una lanza rudimentaria.")
            return True
        else:
            print("\nDecides no fabricar nada y dejas al sabio con sus herramientas.")
            return False
    # Agregar más misiones aquí
    return False

# Función para subir de nivel
def subir_nivel(personaje):
    if personaje["experiencia"] >= 100:  # 100 XP para subir de nivel
        personaje["nivel"] += 1
        personaje["experiencia"] = 0
        personaje["salud"] += 20  # Subir salud al subir de nivel
        personaje["ataque"] += 5   # Subir ataque al subir de nivel
        personaje["defensa"] += 3  # Subir defensa al subir de nivel
        print(f"\n¡{personaje} ha subido al nivel {personaje['nivel']}!")
    else:
        print(f"\n{personaje} aún no tiene suficiente experiencia para subir de nivel.")

# Juego principal
def jugar():
    print("Bienvenido a *Ancestors*: El Juego de Rol de la Prehistoria.")
    print("Tu aventura comienza...")

    personaje_actual = input("¿Qué personaje te gustaría jugar? (Ramses o Perseo): ").capitalize()

    if personaje_actual not in personajes_jugables:
        print("Personaje no válido. Saliendo...")
        return
    
    while personajes_jugables[personaje_actual]["nivel"] < 100:
        print(f"\n--- Tu personaje: {personaje_actual} ---")
        print(f"Salud: {personajes_jugables[personaje_actual]['salud']} | Nivel: {personajes_jugables[personaje_actual]['nivel']} | Experiencia: {personajes_jugables[personaje_actual]['experiencia']}")
        print("¿Qué quieres hacer?")
        print("1. Explorar la cueva")
        print("2. Fabricar armas")
        print("3. Combatir con un NPC")
        print("4. Ver inventario")
        print("5. Salir del juego")
        
        eleccion = input("Elige una opción (1-5): ")
        
        if eleccion == "1":
            if dialogo_mision("explorar_cueva"):
                npc = random.choice(list(npcs.keys()))
                print(f"\nTe encuentras con {npc}. ¡Es hora de combatir!")
                if atacar(personajes_jugables[personaje_actual], npcs[npc]):
                    personajes_jugables[personaje_actual]["experiencia"] += 10
                    subir_nivel(personajes_jugables[personaje_actual])
        elif eleccion == "2":
            if dialogo_mision("fabricar_armas"):
                personajes_jugables[personaje_actual]["inventario"].append("Lanza Rudimentaria")
                print("Has fabricado una lanza.")
        elif eleccion == "3":
            npc = random.choice(list(npcs.keys()))
            print(f"\nTe encuentras con {npc}. ¡Es hora de combatir!")
            if atacar(personajes_jugables[personaje_actual], npcs[npc]):
                personajes_jugables[personaje_actual]["experiencia"] += 10
                subir_nivel(personajes_jugables[personaje_actual])
        elif eleccion == "4":
            print("Inventario:", personajes_jugables[personaje_actual]["inventario"])
        elif eleccion == "5":
            print("¡Gracias por jugar!")
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__juego__":
    jugar()
