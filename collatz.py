# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """
    num=n
    lst = []
    if num == 1:
        return 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
            lst.append(num)
        elif num % 2 != 0:
            num = num * 3 + 1
            lst.append(num)
    return len(lst)


def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    num = n
    lst = [num]

    while num > 1:
        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        lst.append(num)
    return lst

