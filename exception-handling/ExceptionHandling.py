a=10
b=0
try:
    print(a/0)
    print('hi')
except:
    print('Division by zero not possible')
finally:
    print('finlly came')