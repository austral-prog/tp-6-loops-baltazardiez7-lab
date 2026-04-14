# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """

    if n <= 0:
        return 0
    numero = 0
    for entero in range(1, n+1):
        numero += entero
    return numero




def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """

    if n <= 0:
        return 0

    cero = 0
    for entero in range(0,n+1,2):
        cero += entero
    return (cero)


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """

    if n <= 0:
        return 1
    uno = 1
    for entero in range(1,n+1):

        uno *= entero
    return (uno)
    
