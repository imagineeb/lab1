print('Введите размерность матрицы 1: ')
razmer = str(input())

m1 = []
m2 = []
m31 = []
m32 = []
m4 = []
m5 = []
m61 = []
m62 = []

if razmer == '2x1':
    for i in range(2):
        m1.append(float(input()))
    print(m1[0])
    print(m1[1])

if razmer == '1x2':
    for i in range(2):
        m2.append(float(input()))
    print(m2[0], m2[1])


if razmer == '2x2':
    for i in range(4):
        m31.append(float(input()))
    print(m31[0], m31[1])
    print(m31[2], m31[3])


if razmer == '1x3':
    for i in range(3):
        m4.append(float(input()))
    print(m4[0], m4[1], m4[2])


if razmer == '3x1':
    for i in range(3):
        m5.append(float(input()))
    print(m5[0])
    print(m5[1])
    print(m5[2])


if razmer == '3x3':
    for i in range(9):
        m61.append(float(input()))
    print(m61[0], m61[1], m61[2])
    print(m61[3], m61[4], m61[5])
    print(m61[6], m61[7], m61[8])

print('Выберите нужное действие')
move = str(input())
if move == 'Транспорирование':
    if razmer == '2x1':
        m1T = (m1[1], m1[0])
        print(m1T)

    if razmer == '1x2':
        m2T1 = (m2[1])
        m2T2 = (m2[0])
        print(m2T1)
        print(m2T2)

    if razmer == '2x2':
        m31T1 = (m31[0], m31[2])
        m31T2 = (m31[1], m31[3])
        print(m31T1)
        print(m31T2)

    if razmer == '1x3':
        m4T1 = (m4[2])
        m4T2 = (m4[1])
        m4T3 = (m4[0])
        print(m4T1)
        print(m4T2)
        print(m4T3)

    if razmer == '3x1':
        m5T = (m5[2], m5[1], m5[0])
        print(m5T)

    if razmer == '3x3':
        m61T1 = (m61[0], m61[3], m61[6])
        m61T2 = (m61[1], m61[4], m61[7])
        m61T3 = (m61[2], m61[5], m61[8])
        print(m61T1)
        print(m61T2)
        print(m61T3)

if move == 'Умножение':
    print('Введите размерность 2 матрицы: ')
    razmer2 = str(input())

    if razmer2 == '2x1':
        for i in range(2):
            m1.append(float(input()))
        print(m1[0])
        print(m1[1])
    if razmer2 == '1x2':
        for i in range(2):
            m2.append(float(input()))
        print(m2[0], m2[1])

    if razmer2 == '2x2':
        for i in range(4):
            m32.append(float(input()))
        print(m32[0], m32[1])
        print(m32[2], m32[3])
    if razmer2 == '1x3':
        for i in range(3):
            m4.append(float(input()))
        print(m4[0], m4[1], m4[2])
    if razmer2 == '3x1':
        for i in range(3):
            m5.append(float(input()))
        print(m5[0])
        print(m5[1])
        print(m5[2])
    if razmer2 == '3x3':
        for i in range(9):
            m62.append(float(input()))
        print(m62[0], m62[1], m62[2])
        print(m62[3], m62[4], m62[5])
        print(m62[6], m62[7], m62[8])
    if razmer == '2x1' and razmer2 == '2x1':
        print('Math error')

    if razmer == '2x1' and razmer2 == '1x2':
        H11 = (m1[0]*m2[0])
        H12 = (m1[0]*m2[1])
        H21 = (m1[1]*m2[0])
        H22 = (m1[1]*m2[1])
        print((H11, H12))
        print((H21, H22))

    if razmer == '2x1' and razmer2 == '2x2':
        print('Math error')

    if razmer == '2x1' and razmer2 == '1x3':
        I11 = (m1[0]*m4[0])
        I12 = (m1[0]*m4[1])
        I13 = (m1[0]*m4[2])
        I21 = (m1[1]*m4[0])
        I22 = (m1[1]*m4[1])
        I23 = (m1[1]*m4[2])
        print((I11, I12, I13))
        print((I21, I22, I23))

    if razmer == '2x1' and razmer2 == '3x1':
        print('Math error')

    if razmer == '2x1' and razmer2 == '3x3':
        print('Math error')

    if razmer == '1x2' and razmer2 == '2x1':
        J11 = (m2[0]*m1[0]+m2[1]*m1[1])
        print(''',\n,J11''')

    if razmer == '1x2' and razmer2 == '1x2':
        print('Math error')

    if razmer == '1x2' and razmer2 == '2x2':
        K11 = (m2[0]*m32[0]+m2[1]*m32[2])
        K12 = (m2[0]*m32[1]+m2[1]*m32[3])
        print((K11, K12))

    if razmer == '1x2' and razmer2 == '1x3':
        print('Math error')

    if razmer == '1x2' and razmer2 == '3x1':
        print('Math error')

    if razmer == '1x2' and razmer2 == '3x3':
        print('Math error')

    if razmer == '2x2' and razmer2 == '1x2':
        print('Math error')

    if razmer == '2x2' and razmer2 == '2x1':
        L11 = (m31[0]*m1[0]+m31[1]*m1[1])
        L21 = (m31[2]*m1[0]+m31[3]*m1[1])
        print((L11))
        print((L21))

    if razmer == '2x2' and razmer2 == '2x2':
        M11 = (m31[0]*m32[0]+m31[1]*m32[2])
        M12 = (m31[0]*m32[1]+m31[1]*m32[3])
        M21 = (m31[2]*m32[0]+m31[3]*m32[2])
        M22 = (m31[2]*m32[1]+m31[3]*m32[3])
        print((M11, M12))
        print((M21, M22))

    if razmer == '2x2' and razmer2 == '1x3':
        print('Math error')

    if razmer == '2x2' and razmer2 == '3x1':
        print('Math error')

    if razmer == '2x2' and razmer2 == '3x3':
        print('Math error')
