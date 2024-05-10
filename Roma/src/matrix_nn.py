def main():
    matrix = [[2, -5, 3],
              [1, 4, 0],
              [-3, 7, 5]]
    m = []
    opr = 0
    for k in range(3):
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j != k:
                    m.append(matrix[i][j])
        print((-1)**k)
        opr += (-1)**k * matrix[0][k] * (m[0] * m[3] - m[1] * m[2])
        m.clear()
    print(opr)


if __name__ == '__main__':
    main()


def main():
    a = open('24.txt').readlines()
    matrix = []
    m = []
    for i in range(len(a)):
        matrix.append(list(map(int, a[i].split(', '))))
    k = opr = 0
    while k != len(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i > 0 and j != k:
                    m.append(matrix[i][j])
        if len(m) == 4:
            # print(matrix[0][k])
            # print((m[0]*m[3]-m[1]*m[2]))
            opr = opr + abs(matrix[0][k]) * (m[0] * m[3] - m[1] * m[2])
            m.clear()
        k = k + 1
    print(opr)


if __name__ == '__main__':
    main()
