worker_num = int(input("Введите количество сотрудников: "))
path = list(int(i) for i in input("Введите расстояния в километрах до дома через пробелы: ").split())
taxi = [int(i) for i in input("Введите тарифы в за проезд одного километра через пробелы: ").split()]
path1 = list(0 for i in range(0, worker_num))
for i in range(worker_num):
    try:
        path1[i] = (path[i])
    except IndexError:
        break
path1.sort()
taxi1 = list(0 for i in range(0, worker_num))
for i in range(worker_num):
    try:
        taxi1[i] = taxi[i]
    except IndexError:
        break
taxi1.sort(reverse=True)
for i in range(worker_num):
    print("Работник, которому до дома", path1[i], "км должен ехать на такси с тарифом", taxi1[i], "руб/км")