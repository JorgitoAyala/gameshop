import random

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def main():
    words = ["programacion", "peru", "amarillo", "rojo", "python", "perro", "gato", "dulces" ,"enero" ,"pollo","profesor" ,"vaca" ,"toro"]
    score = 0
    
    print("Bienvenido al juego de Palabras Desordenadas!")
    print("Desordena las letras para formar una palabra correcta.")
    
    while True:
        selected_word = random.choice(words)
        scrambled_word = scramble_word(selected_word)
        
        print(f"\nPalabra desordenada: {scrambled_word}")
        
        guess = input("Ingresa tu respuesta: ").strip().lower()
        
        if guess == selected_word:
            score += 1
            print(f"¡Correcto! Tu puntaje actual es: {score}")
        else:
            print(f"Incorrecto. La palabra correcta era: {selected_word}")
        
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if play_again != 's':
            print(f"¡Gracias por jugar! Tu puntaje final es: {score}")
            break

if __name__ == "__main__":
    main()
