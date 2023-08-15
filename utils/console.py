import os
from time import sleep

# Para pintar una linea de la consola de un determinado patrón
def drawUI(typeTable: int, phrase: str, length_const = 76):

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


def drawTables(typeTable: int, phrases: dict, length_const = 34):
  p1, p2 = phrases.values()
  alternatives = [1,2,3]

  r1 = drawUI(typeTable, p1, length_const)
  r2 = drawUI(typeTable, p2, length_const)

  if(typeTable in alternatives):
    return f'{r1}  {r2}'
  else:
    return "Hay un error"