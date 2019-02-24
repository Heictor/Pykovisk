#Declare the variables as you wish
x = (float(input('Insira o valor de x: \n')))
y = (float(input('Insira o valor de y: \n')))

if x>y:
    print('x greatter than y')
elif x<y:
    print('x is minor than y')
elif x>=y:
    print('x is greater or equal to y')
elif x<=y:
    print('x is minor or equal to y')
elif x!=y:
    print('x is different to y')
elif x==y:
    print('x is equal to y')
else:
    print('nenhuma condição foi satisfeita')
