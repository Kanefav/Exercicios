total = 0
num = int(input('Digite Um Número: '))
for c in range(1, num+1):
    print(c, end=' ')
    if num % c == 0:
        total += 1
print(f'O Número {num} Foi Divisivel {total} Vezes')
if total == 2:
    print('O Número é Primo')
else:
    print('O Número não é Primo')