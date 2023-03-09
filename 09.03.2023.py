import main

choose = int(input("Чего вы хотите? Сумма Геометрической и Арифметрической прогрессии(1) Если хотите чтобы что то вывелось(2)"))

match choose:
    case 1:

        main.mathem()
    case 2:
        a = input("Введите что-то:")
        print(a)

