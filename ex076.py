expr = str(input('Digite uma expressão que utileza parenteses: '))
lista = []
for simbolos in expr:
 if simbolos == '(':
    lista.append('(')
 elif simbolos == ')':
  if len(lista) > 0:
     lista.pop()
  else:
      lista.append(')')
      break
if len(lista) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta inválida')