import random
import time
hqw = 0
h = ["random", "manual"]
e = 0
s = e - 1
sh = s + 2
ga = ["1", "0"]
mnh = [2, 3]
hqw = 0
# Функция для вывода поля на экран
def print_board(board):
    for row in board:  # Перебираем строки поля
        m = ["*" if cell else " " for cell in row]
        k = "".join(m)
        print(k)  # Выводим символы '#' для живых клеток и '.' для мертвых
    print()  # Пустая строка после вывода поля
# Функция для подсчета количества живых соседей клетки
def get_neighbours_count(board, x, y):
    count = 0  # Начальное количество живых соседей
    for i in range(s, sh):  # Перебираем окрестности клетки (-1, 0, 1) по вертикали
        for j in range(s, sh):  # Перебираем окрестности клетки (-1, 0, 1) по горизонтали
            if i == 0 and j == 0:  # Пропускаем саму клетку
                continue
            awe = len(board)
            aws = len(board[0])
            awd = x + i + awe
            awr = y + j + aws
            qwr = awd % awe
            qwn = awr % aws
            count = count + board[qwr][qwn]  # Добавляем количество живых соседей, учитывая цикличность поля
    return count
# Функция для расчета следующего поколения
def next_generation(board):
    nbg = len(board[0])
    azs = [0 for mk in range(nbg)]
    new_board = [[0 for mkv in range(nbg)] for joy in range(nbg)]  # Создаем новое поле
    for i in range(len(board)):  # Перебираем строки поля
        for j in range(nbg):  # Перебираем столбцы поля
            count = get_neighbours_count(board, i, j)  # Получаем количество живых соседей
            if board[i][j] and count in mnh:  # Если клетка живая и количество живых соседей 2 или 3
                new_board[i][j] = 1  # Клетка остается живой
            elif not board[i][j] and count == 3:  # Если клетка мертва и количество живых соседей 3
                new_board[i][j] = 1  # Клетка становится живой
    return new_board
# Главная функция
def main():
    hqw = 0
    print("Введите размер поля:")
    size = input()
    while True:
        if size.isdigit():
            break
        else:
            print("Введите размер поля:")
            size = input()
    size = int(size)
    print("Выберите способ генерации начального состояния:random или manual:")
    choice = input()
    while choice.lower() not in h:
            print("Выберите способ генерации начального состояния:random или manual:")
            choice = input()
    if choice.lower() == "random":  # Генерация случайного начального состояния
        pi = random.randint(0, 1)
        p = [random.randint(0, 1) for qw in range(size)]
        board = [[random.randint(0, 1) for qw in range(size)] for qwc in range(size)]
    elif choice.lower() == "manual":  # Ручное введение начального состояния
        board = [[0 for qw in range(size)] for qw in range(size)]
        for nji in range(size):
            e = 0
            while True:
                print("введите", (nji + 1), "строку:")
                o = input()
                hqw = hqw + 1
                if hqw == 1:
                    leu = len(o)
                for kop in o:
                    if kop not in ga:
                        e = 1
                if len(o) != leu:
                    print("введите строку такой же длины как и прошлая")
                if e == 0 and len(o) == leu:
                    break      
            o = o.replace(" ", "")
            o = list(o)
            leu = len(o)
            u = map(int, o)
            row = list(u)
            board[nji] = row
    while True:  # Основной цикл программы
        e = 0
        print_board(board)
        board = next_generation(board)
        time.sleep(0.4)
        for i in next_generation(board):
            for j in i:
                if j == 1:
                    e = 1
                    break
        if e == 0:
            t = input()
main()  # Запуск программы
