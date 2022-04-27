import random

global game
global go

go = input('Сыграем? ')

while go != 'нет':

    game = input('В какую игру сыграем? На выбор: монетка, кости, случ число или угадайка. (Вы можете завершить игру, написав: стоп) ')

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

    def uga():
        kto = input('Я угадываю ваше число или наоборот? (я - вы угадываете, ты - я угадываю) ')
        if kto == 'я':
            f, l = map(int, input('Напишите диапазон чисел. Например: 1 100 (от 1 до 100) ').split())
            num = random.randint(f, l)
            print('Угадывай')
            while True:
                ans = int(input())
                if ans == num:
                    print('Ты угадал!')
                    break
                elif ans < num:
                    print('Мое число больше!')
                    continue
                else:
                    print('Мое число меньше!')
                    continue
        elif kto == 'ты':
            f, l = map(int, input('Напишите диапазон чисел. Например: 1 100 (от 1 до 100) ').split())
            left = f
            right = l
            e = input('Загадал число?')
            step = 0
            if e == 'да':
                while True:
                    step += 1
                    myans = (left + right) // 2
                    print(myans)
                    mol = input('Твое число меньше(<) или больше(>)? Или я угадал(=)? ')
                    if mol == '<':
                        right = myans - 1
                        continue
                    elif mol == '>':
                        left = myans + 1
                        continue
                    else:
                        print('Ура победа!')
                        print('Я угадал за', step, 'шагов')
                        break
            else:
                print('Я жду')

    if game == 'монетка':
        oorr()
    elif game == 'кости':
        kosti()
    elif game == 'случ число':
        randorg()
    elif game == 'угадайка':
        uga()