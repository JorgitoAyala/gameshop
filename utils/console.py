import os
from time import sleep

# Para pintar una linea de la consola de un determinado patrón
def drawUI(typeTable: int, phrase: str):

  length_const = 56
  chars = length_const - len(phrase)

  match typeTable:

    case 1:
      chars = chars // 2
      return f'|| {"=" * chars}{phrase}{"=" * chars} ||'
    
    case 2:
      return f'|| {phrase}{" " * chars} ||'
    
    case 3:
      return f'|| {phrase}{" " * chars}||'
    
    case _: return "Hay un error"

# Para crear un mensaje con retardo especifico
def lazyMessage(word: str, time: int):
  print(word, end=" ")

  for second in range(time, 0, -1):
    print(second, end=" ", flush=True)
    sleep(1)
  
  print("... => Listo 🙌 !", end="\n")

# Para limpiar la consola
def clear():
  if os.name == "nt": 
    os.system("cls")
  else: 
    os.system("clear")