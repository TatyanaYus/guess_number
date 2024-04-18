from random import randint


number = randint(1, 100) # Получаем случайное число в диапазоне от 1 до 100 включительно.
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Введите число: ')) # Получаем число от пользователя и сохраняем его в переменную guess.

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    if guess > number:
        print('Ваше число больше того, что загадано.')
    if guess == number:
        break                                          # Прерываем выполнение программы

print('Отличная интуиция! Вы угадали число :)')