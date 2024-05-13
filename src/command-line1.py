import argparse

parser = argparse.ArgumentParser(description="Элементы матрицы")
parser.add_argument("filename", help="Имя файла")

args = parser.parse_args()

print(f"Привет, {args.filename}!")


with open(args.filename, 'r') as file:
    b = file.readlines()
    matrix = []
    for i in range(len(b)):
        matrix.append(list(map(int, b[i].split(', '))))
    print(matrix)


import linalg
import numpy as np

A = np.matrix(matrix)
print(A)
print(np.linalg.det(A))


