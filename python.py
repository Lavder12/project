text = input('Введите строку:')
a = int(input('Введите ширину:'))

if a % 2 == 0:
    res = text.center(a)
else: res = text.rjust(a)

print("Результат:")
print(f"'{res}'")