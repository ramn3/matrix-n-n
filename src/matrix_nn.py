def main():
    a = open('24.txt').readlines()
    matrix = []
    m = []
    for i in range(len(a)):
        matrix.append(list(map(int, a[i].split(', '))))
    opr = 0
    q = 1
    for k in range(3):
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j != k:
                    m.append(matrix[i][j])
        opr += q * matrix[0][k] * (m[0] * m[3] - m[1] * m[2])
        m.clear()
        q *= -1
    print(opr)


if __name__ == '__main__':
    main()

