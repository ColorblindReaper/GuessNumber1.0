import random as r


print("Добро пожаловать в числовую угадайку")
print("Выберите верхнюю границу загаданного числа не ниже единицы, например 100")
n = int(input())
answer = r.randint(1, n)

def is_valid(s):
    return s.isdigit() and 1 <= int(s)

def game():
    guess, counter = 0, 0  # ответное число + колличество попыток
    while True:
        print("Введите число от 1 до", n)
        guess = input()
        counter += 1
        if is_valid(guess) == True:
            if int(guess) < answer:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                continue
            elif int(guess) > answer:
                print("Ваше число больше загаданного, попробуйте еще разок")
                continue
            elif int(guess) == answer:
                break
        elif is_valid(guess) == False:
            print("А может быть все-таки введем целое число от 1?")
            continue
    print("Вы угадали, поздравляем! Ваше число попыток:", counter)

while True:
    game()
    print("Хорошая игра, не желаете ещё разок?")
    print("Да(Д) или Yes(Y) если желаете продолжить:")
    ans = input()
    if ans.lower() in ("д", "да", "yes", "y"):
        print("Выберите верхнюю границу загаданного числа не ниже единицы, например 100")
        n = int(input())
        answer = r.randint(1, n)
        continue
    else:
        break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
