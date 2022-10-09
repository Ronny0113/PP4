while True:
    while True:
        try:
            worker_num = int(input("Введите количество сотрудников или введите 0 чтобы закончить: "))
            break
        except ValueError:
            print("Введите цифру")
    if worker_num == 0:
        break
    while True:
        try:
            path = [int(i) for i in input("Введите расстояния в километрах до дома через пробелы: ").split()]
            break
        except ValueError:
            print("Введите ЦИФРЫ, через пробел")
    while True:
        try:
            taxi = [int(i) for i in input("Введите тарифы в за проезд одного километра через пробелы: ").split()]
            break
        except ValueError:
            print("Введите тарифы ЦИФРАМИ, через пробел")
    path1 = list(0 for i in range(0, worker_num))
    if worker_num != len(path) and worker_num != len(taxi):
        print("Введите по одному расстоянию и тарифу на каждого сотрудника")
        continue
    for i in range(worker_num):
        path1[i] = (path[i], i + 1)
    path1.sort()
    taxi1 = list(0 for i in range(0, worker_num))
    for i in range(worker_num):
        taxi1[i] = (taxi[i], i + 1)
    taxi1.sort(reverse=True)
    ans = [0] * (worker_num + 1)
    for i in range(worker_num):
        ans[path1[i][1]] = taxi1[i][1]
    for i in range(1, worker_num + 1):
        print(i, "работнику надо поехать на такси номер", ans[i])
    num = int(0)
    for i in range(len(path1)):
        num += (path1[i][0] * taxi1[i][0])

    W1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    W1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    W2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    W3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    W4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    W5 = ["тысяча", "тысячи", "тысяч"]
    W6 = ["рубль", "рубля", "рублей"]

    num1 = num // 100000
    num2 = (num // 10000) % 10
    num3 = (num // 1000) % 10
    num4 = (num // 100) % 10
    num5 = (num // 10) % 10
    num6 = num % 10

    poz = ""
    if num1 != 0:
        i1 = num1 - 1
        poz += W4[i1] + " "

    if num2 == 1 and num3 == 0:
        poz += W3[0] + " "

    if num2 != 1:
        if num2 != 0:
            i2 = num2 - 1
            poz += W3[i2] + " "

    if num3 != 0:
        if num2 == 1:
            i3 = num3 - 1
            poz += W2[i3] + " " + W5[2] + " "
        else:
            i3 = num3 - 1
            poz += W1b[i3] + " "
            if num3 == 1:
                poz += W5[0] + " "
            elif 1 < num3 < 5:
                poz += W5[1] + " "
            else:
                poz += W5[2] + " "

    if (num3 == 0) and (num2 or num1 != 0):
        poz += W5[2] + " "

    if num4 != 0:
        i4 = num4 - 1
        poz += W4[i4] + " "

    if num5 == 1 and num6 == 0:
        poz += W3[0] + " "

    if num5 != 1:
        if num5 != 0:
            i5 = num5 - 1
            poz += W3[i5] + " "

    if num6 != 0:
        if num5 == 1:
            i6 = num6 - 1
            poz += W2[i6] + " " + W6[2]
        else:
            i6 = num6 - 1
            poz += W1a[i6] + " "
            if num6 == 1:
                poz += W6[0] + " "
            elif 1 < num6 < 5:
                poz += W6[1]
            else:
                poz += W6[2]

    if (num6 == 0) and (num5 or num4 or num3 or num2 or num1 !=0):
        poz += W6[2]

    poz = poz.capitalize()
    print("Всего на дорогу придётся потратить", num, "(" + poz + ")\n")
