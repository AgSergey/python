
print("Hi")
print('hello', 'world', sep=' ,* ')

a = 'spam'
b = 12.98
c = 'Flow'
print(a, b, c,)
print(a, b, c, sep=None)
print(a, b, c, sep='\n')
print(a, b, c, sep=None, end='....!'); print(a, b, c,)
print(a, b, c, sep='\n', end='....!'); print(a, b, c,)


print(10, 235)
print(1000, 50)

print("%5d, 'number', %7d" % (10, 235), sep='*') # sep не работает
print("%5d%7d" % (31000, 50))

n = 1357
m = 'Sergey'
print(f'{250 / 3:.5f}')
print(f'{250 / 3:.5}')
print(f'{250 / 3:.5f}')
print(f'{1:05d}')
print(f'{7:02d}')
print(f'{n:>35}')
print(f'{n:=35}')
print(f'{n:^13}')
print(f'{m:>60}', end='....!')
print(f'{m:>15}')




a = True
b = False
c = a and b
print(c, type(a))
