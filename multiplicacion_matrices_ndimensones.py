
#matrices de entrada a multiplicar
a=[[2,4,6],[6,8,10],[10,12,9]]
b=[[1,3,5,4,6],[7,9,11,2,8],[5,7,4,6,3]]


#Definir longitud de las filas y columnas
filasa=len(a)
columnasa=len(a[0])
filasb=len(b)
columnasb=len(b[0])

#Crea la matriz inicial vacía
matrix=[[0 for x in range(columnasb)]for i in range(filasa)]

#Si el numero de columnas de a es igual al numero de filas de b, se pueden multiplicar
if columnasa == filasb:
   lisSuma=[]
   for i in range(filasa):
    for j in range(columnasb):
        for k in range(filasb):
            mult=(a[i][k] * b[k][j])
            lisSuma.append(mult)
            if k==columnasa-1:
                suma=sum(lisSuma)
                lisSuma=[]  
                matrix[i][j]=suma

else:
    print("No se pueden multiplicar")
    
#Imprime el resultado de la multiplicacion de ambas matrices
print(matrix)
