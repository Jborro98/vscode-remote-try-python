# necesito hacer un juego de rock paper o scissors de un jugador vs ia, el jugador debe colocar una de las 3 
# respuestas sino el programa volverá a pedir seleccionar una opcion, al jugador se le debe preguntar si desea 
# jugar otra ronda y en caso de ya no querer se mostrará la puntuacion final
import random

opciones = ['rock', 'paper', 'scissors']
puntuacion_jugador = 0
puntuacion_ia = 0
jugando = True

while jugando:
    # Paso 1
    jugador = input("Elige rock, paper o scissors: ").lower()
    while jugador not in opciones:
        print("Opción no válida, intente de nuevo")
        jugador = input("Elige rock, paper o scissors: ").lower()
    
    # Paso 2
    ia = random.choice(opciones)
    print(f"La IA eligió: {ia}")
    
    # Paso 3
    if jugador == ia:
        print("Empate!")
    elif jugador == "rock" and ia == "scissors" or jugador == "paper" and ia == "rock" or jugador == "scissors" and ia == "paper":
        print("¡Ganaste esta ronda!")
        puntuacion_jugador += 1
    else:
        print("Gana la IA esta ronda")
        puntuacion_ia += 1

    # Paso 4
    seguir_jugando = input("¿Quieres jugar otra ronda? (s/n)").lower()
    while seguir_jugando != 's' and seguir_jugando != 'n':
        print("Opción no válida, intente de nuevo")
        seguir_jugando = input("¿Quieres jugar otra ronda? (s/n)").lower()

    # Paso 5
    if seguir_jugando == 'n':
        jugando = False

# Paso 6
print(f"Puntuación final:\nJugador: {puntuacion_jugador}\nIA: {puntuacion_ia}")
