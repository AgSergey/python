# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369

#Код для сдачи

num_str = input('Введите целое число от 0 до 9: ')
summa1_num = int(num_str) + int(num_str * 2) +int(num_str * 3)
print(f"Сумма чисел n+nn+nnn = {summa1_num}\n\n")

