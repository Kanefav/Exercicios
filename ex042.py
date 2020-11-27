s1 = input('Primeiro segmento: ')
s2 = input('Segundo segmento: ')
s3 = input('Terceiro segmento: ')
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Podem formar um triângulo, podem formar um triângulo ', end='')
    if s1 == s2 == s3:                          # end='' significa final do print igual a 0#
        print('EQUILATERO')
    elif s1 != s2 != s3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Não podem formar um triângulo')