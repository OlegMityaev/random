import random

global game
global go

go = input('Сыграем? ')

while go != 'нет':

    game = input('В какую игру сыграем? На выбор: монетка, кости или случ число. (Вы можете завершить игру, написав: стоп) ')

    if game == 'стоп':
        print('До связи')
        break

    def oorr():
        bet = input('Выбери: орел или решка? ')
        seq = ['орел', 'решка']
        if bet not in seq:
            print('Выбери: орел или решка')
        coin = random.choice(seq)
        if bet == coin:
            print('Ты выиграл')
            print('Выпал', coin)
        else:
            print('Ты проиграл')
            print('Выпал ', coin)

    def kosti():
        print(random.randint(1, 6))
        print(random.randint(1, 6))

    def randorg():
        f, l = map(int, input('Напишите диапазон чисел. Например: 1 100 (от 1 до 100) ').split())
        print(random.randint(f, l))

    if game == 'монетка':
        oorr()
    elif game == 'кости':
        kosti()
    elif game == 'случ число':
        randorg()