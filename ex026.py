frase = str(input('Digite uma frase qualquer: ')).lower().strip()
print(f'Esse é o número de vezes que aparece a letra -a- em sua frase: {frase.count("a")}'
      f'\nA primeira letra -A- apareceu na seguinte posição: {frase.find("a")+1}'
      f'\nA última letra -A- apareceu na seguinte posição: {frase.rfind("a")+1}')
