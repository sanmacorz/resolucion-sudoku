#!/usr/bin/env python3
def hallar_casilla_vacia(vector, posicion):
    for fila in range(9):
        for columna in range(9):
            if vector[fila][columna] == 0:
                posicion[0] = fila
                posicion[1] = columna
                return True
    return False


def verificar_usado_fila(vector, fila, numero):
    for i in range(9):
        if vector[fila][i] == numero:
            return True
    return False


def verificar_usado_columna(vector, columna, numero):
    for i in range(9):
        if vector[i][columna] == numero:
            return True
    return False


def verificar_usado_caja(vector, fila, columna, numero):
    for i in range(3):
        for j in range(3):
            if vector[i + fila][j + columna] == numero:
                return True
    return False


def verificar_ubicacion_posible(vector, fila, columna, numero):
    return not verificar_usado_fila(vector, fila, numero) and (
        not verificar_usado_columna(vector, columna, numero)
        and (
            not verificar_usado_caja(
                vector, fila - fila % 3, columna - columna % 3, numero
            )
        )
    )


def resolver_sudoku(matriz):
    posicion = [0, 0]

    if not hallar_casilla_vacia(matriz, posicion):
        return True

    fila = posicion[0]
    columna = posicion[1]

    for numero in range(1, 10):
        if verificar_ubicacion_posible(matriz, fila, columna, numero):
            matriz[fila][columna] = numero
            if resolver_sudoku(matriz):
                return True
            matriz[fila][columna] = 0
    return False
