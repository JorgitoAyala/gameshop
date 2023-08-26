Proceso Tic_Tac_Toe
	Definir x,n,jugador Como Entero
	Definir vector Como Caracter
	Dimension vector[9]
	para x = 1 Hasta 9 Con Paso 1 Hacer
		vector(x) = " "
	FinPara
	x = 1
	jugador = azar(2)+1
	Mientras x <= 9 Hacer
		Escribir "Ingresa una posicion jugador ", jugador
		Escribir "1,2,3","        ",vector(1),",",vector(2),",",vector(3)
		Escribir "4,5,6","        ",vector(4),",",vector(5),",",vector(6)
		Escribir "7,8,9","        ",vector(7),",",vector(8),",",vector(9)
		Leer n
		si n > 0 y n < 10 Entonces
			si jugador == 1 Entonces
				si vector(n) == " " Entonces
					vector(n) = "x"
					jugador = 2
					si vector(1) == "x" y vector(3) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(4) == "x" y vector(5) == "x" y vector(6) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(7) == "x" y vector(8) == "x" y vector(9) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(1) == "x" y vector(4) == "x" y vector(7) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(2) == "x" y vector(5) == "x" y vector(8) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(3) == "x" y vector(6) == "x" y vector(9) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
					FinSi
					si vector(1) == "x" y vector(5) == "x" y vector(9) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
					si vector(3) == "x" y vector(5) == "x" y vector(7) == "x" Entonces
						Escribir "El jugador 1 ha ganado"
						x = 9
					FinSi
				SiNo
					Escribir "Esa posicion esta ocupada"
				FinSi
			SiNo
				si vector(n) == " " Entonces
					vector(n) = "o"
					jugador = 1
					si vector(1) == "o" y vector(3) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(4) == "o" y vector(5) == "o" y vector(6) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(7) == "o" y vector(8) == "o" y vector(9) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(1) == "o" y vector(4) == "o" y vector(7) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(2) == "o" y vector(5) == "o" y vector(8) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(3) == "o" y vector(6) == "o" y vector(9) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
					FinSi
					si vector(1) == "o" y vector(5) == "o" y vector(9) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
					si vector(3) == "o" y vector(5) == "o" y vector(7) == "o" Entonces
						Escribir "El jugador 2 ha ganado"
						x = 9
					FinSi
				SiNo
					Escribir "Esa posicion esta ocupada"
				FinSi
			FinSi
		SiNo
			Escribir "Posicion incorrecta"
		FinSi
		x = x + 1
	FinMientras
	Escribir "1,2,3","        ",vector(1),",",vector(2),",",vector(3)
	Escribir "4,5,6","        ",vector(4),",",vector(5),",",vector(6)
	Escribir "7,8,9","        ",vector(7),",",vector(8),",",vector(9)
FinProceso
