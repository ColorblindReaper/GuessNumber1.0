import random as r

answer = r.randint(1, 100)

print("Добро пожаловать в числовую угадайку")

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

while True:
    print("Введите число от 1 до 100")
    guess = input()
    if is_valid(guess) == True:
        if int(guess) < answer:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
        elif int(guess) > answer:
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
        elif int(guess) == answer:
            print("Вы угадали, поздравляем!")
            break
    elif is_valid(guess) == False:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")




