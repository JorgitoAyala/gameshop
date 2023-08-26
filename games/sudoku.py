def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(tablero[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

def encontrar_vacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def es_valido(tablero, num, posicion):
    fila, columna = posicion
    
    for i in range(len(tablero)):
        if tablero[fila][i] == num and columna != i:
            return False
        
        if tablero[i][columna] == num and fila != i:
            return False
        
        fila_cuadro = fila // 3 * 3 + i // 3
        columna_cuadro = columna // 3 * 3 + i % 3
        if tablero[fila_cuadro][columna_cuadro] == num and (fila_cuadro, columna_cuadro) != posicion:
            return False
    
    return True

def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    
    fila, columna = vacio
    
    for num in range(1, 10):
        if es_valido(tablero, num, (fila, columna)):
            tablero[fila][columna] = num
            
            if resolver_sudoku(tablero):
                return True
            
            tablero[fila][columna] = 0
    
    return False

def jugar_sudoku():
    tablero = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    imprimir_tablero(tablero)
    while encontrar_vacio(tablero):
        fila = int(input("Ingresa la fila (0-8): "))
        columna = int(input("Ingresa la columna (0-8): "))
        numero = int(input("Ingresa el número (1-9): "))
        
        if es_valido(tablero, numero, (fila, columna)):
            tablero[fila][columna] = numero
            imprimir_tablero(tablero)
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")

    print("¡Felicidades! Has resuelto el Sudoku.")

jugar_sudoku()

