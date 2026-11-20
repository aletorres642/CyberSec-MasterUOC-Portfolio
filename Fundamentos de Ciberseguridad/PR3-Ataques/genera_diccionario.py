#!/usr/bin/env python3
"""Genera un diccionario con todas las permutaciones de una cadena (PR3 - Ataques).

Se usó para atacar por diccionario un .zip cuya clave era una permutación de los
8 primeros caracteres de un usuario académico (laboratorio controlado).

Uso: python3 genera_diccionario.py atorresa dict_zip.txt
"""
import itertools
import sys


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(f"Uso: {sys.argv[0]} <cadena> <fichero_salida>")
    cadena, salida = sys.argv[1], sys.argv[2]
    with open(salida, "w") as f:
        f.write("\n".join("".join(p) for p in itertools.permutations(cadena)))


if __name__ == "__main__":
    main()
