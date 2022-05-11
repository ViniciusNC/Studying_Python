# teste = list()
# teste.append('Gustavo')
# teste.append(59)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'jose'
# teste[1] = 13
# galera.append(teste[:])
# print(galera)
pessoa = list()
lista = list()
for c in range(0, 4):
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(int(input('Digite a idade da pessoa: ')))
    lista.append(pessoa[:])
    pessoa.clear()
print(lista)
