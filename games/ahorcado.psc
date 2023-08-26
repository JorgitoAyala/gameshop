Proceso AHORCADO
	Definir X,N,A,ERROR Como Entero
	Definir LETRA,SECRETA,VECTOR1,VECTOR2 Como Caracter
	
	Escribir  "INGRESA LA PALABRA SECRETA"
	Leer SECRETA
	
	N = Longitud(SECRETA)
	Dimension VECTOR1[N],VECTOR2[N]
	
	Para X = 1 Hasta N CON PASO 1 Hacer
		VECTOR1(X) = Subcadena(SECRETA,X,X)
		VECTOR2(X) = "_"
	FinPara
	
	A = 0
	Mientras A < 5 Hacer
		Para X = 1 Hasta N Con Paso 1 Hacer
			Escribir VECTOR2(X) Sin Saltar
		FinPara
		Escribir ""
		Escribir "INGRESA UNA LETRA"
		Leer LETRA
		
		ERROR = 1
		Para X = 1 Hasta N Con Paso 1 Hacer
			SI LETRA == VECTOR1(X) Entonces
				SI VECTOR2(X) == "_" Entonces
					VECTOR2(X) = LETRA
					C = C + 1
					ERROR = 0
				FinSi
			FinSi
		FinPara
		
		SI C == N Entonces
			Escribir "FELICIDADES HAS GANADO EL JUEGO"
			A = 6
		SiNo
			SI ERROR == 1 Entonces
				A = A + 1
			FinSi
			SI A == 1 Entonces
				Escribir "."
				Escribir "."
				Escribir "."
				Escribir "."
				Escribir "TE QUEDAN 4 INTENTOS"
			FinSi
			SI A == 2 Entonces
				Escribir "......"
				Escribir "."
				Escribir "."
				Escribir "."
				Escribir "TE QUEDAN 3 INTENTOS"
			FinSi
			SI A == 3 Entonces
				Escribir "......"
				Escribir ".    O"
				Escribir "."
				Escribir "."
				Escribir "TE QUEDAN 2 INTENTOS"
			FinSi
			SI A == 4 Entonces
				Escribir "......"
				Escribir ".    O"
				Escribir ".   **"
				Escribir "."
				Escribir "TE QUEDAN 1 INTENTO"
			FinSi
			SI A == 5 Entonces
				Escribir "......"
				Escribir ".    O"
				Escribir ".   **"
				Escribir ".   **"
				Escribir "ESTAS AHORCADO"
			FinSi
		FinSi
	FinMientras
FinProceso
