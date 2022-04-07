from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
alistar = anoatual - nascimento
if alistar == 18:
    print('Você deve se alistar')
elif alistar > 18:
    saldo = alistar - 18
    print(f'Já passou {saldo} anos para você se alistar no Exército Brasileiro')
else:
    saldo = 18 - alistar
    print(f'Você tem {saldo} anos até que sua hora chegue para se alistar')
