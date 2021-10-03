'''
Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой
'''


def man(name, ser_name, year_born, town, email, phone):
    '''
    Функция man() принимает данные, описывающие пользователя как именованные аргументы.
    :param name: имя
    :param ser_name: фамилия
    :param year_born: год рождения
    :param town: город проживания
    :param email: email
    :param phone: телефон
    :return: вывод данных о пользователе одной строкой

    >>>man(name, ser_name, year_born, town, email, phone)

    '''

    a_str = 'name: ' + name + ', sername: ' + ser_name + ', year_born: ' + str(year_born)
    b_str = ', town: ' + town + ', Email: ' + email + ', phone: ' + phone
    c_str = a_str + b_str # a_str, b_str для лучшей читаемости кода, можно было в одну строу
    return c_str


print(f'\nInformation of VIP man from Russian Federation:')
print(man(name='Sergey', ser_name='Agnerubov',
          year_born=1971, town='Voronezh',
          email='agnerubov@mail.ru', phone='+7(904) 212-98-19'))
