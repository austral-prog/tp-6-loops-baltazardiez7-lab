# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    m=matrix
    fl=[]
    for elemento in m:
        for el in elemento:
            fl.append(el)
    return fl



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    m= matrix
    lst = []
    for elemento in m:
        t1 = 0
        for el in elemento:
            t1 += el
        lst.append(t1)
    return lst



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """

    resultado = []

    for col in range(len(matrix[0])):  
        suma = 0
        for fila in range(len(matrix)):  
            suma += matrix[fila][col]
        resultado.append(suma)

    return resultado

