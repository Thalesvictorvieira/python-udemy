# Try,execept else e finally 
try:
    print('1')
    8/0
    print('2')
except ZeroDivisionError as e:
    print('Dividiu por zero')
    print(e)

finally:
    print('3')

