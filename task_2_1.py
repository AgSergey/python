# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

sec_per_hour = 3600
min_per_hour = 60
sec_per_min = 60

sec_in = int(input('Введите кол-во секуднд: '))
print(f"Уважемый, ты ввел для перевода {sec_in} секунд \n")

hour = sec_in // sec_per_hour
minutes = (sec_in - hour * sec_per_hour) // min_per_hour
sec = sec_in - hour * sec_per_hour - minutes * sec_per_min

print(f"Перевод секунд в чч:мм:сс \n{hour:02d}:{minutes:02d}:{sec:02d}")
