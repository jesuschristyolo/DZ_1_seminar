#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
##Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
#что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

number = int(input("Введите итоговое число журавликов: "))
S = number // 2
Kate = number - S
Petya = S // 2
Sergey = S // 2
print("Катя сделала:", Kate, "Журавликов.", "Петя сделал:", Petya, "Журавликов.", "Sergey сделал:", Sergey, "Журавликов." )