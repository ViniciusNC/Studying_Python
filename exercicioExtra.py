from random import choice
pontos = 4
print('SEJAM BEM VINDOS AMIGOS IMÁGINARIOS'
      '\n'
      '\n Este será um QUIZZ sobre os nossos comandantes, tente adivinhar! (Regras):'
      '\n A cada dica pedida é um ponto a menos: '
      '\n Você terá direito até 3 dicas para adivinhar o comandante'
      '\n Quem fizer mais pontos será o vencedor (aqui não terá aba anônima rsrs) '
      '\n ')  # Apresentação
input('Pressione Enter para continuar...')
print('')
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
comandante = choice(lista2)
dicatroll = str(input('E lá vamos nós!!!'
                      '\n Você deseja uma dica de graça? '
                      '\n Digite Sim caso queira e Não caso você não precise: ')).strip().lower()  # Dica troll
if dicatroll == 'sim':
    print(' ')
    print('O comandante é uma carta LENDÁRIA :D'
          '\n ')
else:
    print(' '
          '\nVocê realmente deve ser bom...')
    print('')
input(' '
      'Agora realmente vamos começar o jogo, por gentileza aperte enter para continuar...'
      '\n ')
if comandante == 1:
    dicakogla0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicakogla0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicakogla1 = str(input('O artista da carta se chama Chris Rahn, precisa de mais dicas? S/N ')).upper().strip()
        if dicakogla1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicakogla2 = str(input('O comandante precisa da cor verde para ser castado, precisa de mais dicas? S/N '
                                   )).upper().strip()
            if dicakogla2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O comandante custa 6 manas')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora dê sua resposta, quais dos comandantes a seguir é o correto? '))
                if resposta0 == 1:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Kogla, O Símio Titânico e você ficou com '
                          f'{pontos} '
                          f'pontos')
                else:
                    print('Você errou')
            elif dicakogla2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 == 1:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Kogla, O Símio Titânico e você ficou com '
                          f'{pontos} '
                          f'pontos')
        elif dicakogla1 == 'N':
            print('Estes são os nosos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta1 = int(input('Agora digite sua resposta de acordo com o número de cada comandante:'))
            if resposta1 == 1:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Kogla, O Símio Titânico e ficou com '
                      f'{pontos} pontos')
            else:
                print('Você errou')
    elif dicakogla0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora dê sua resposta, qual é o comandante correto? '))
        if resposta0 != 1:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Kogla, O Símio Titânico e'
                  f' você ficou com {pontos} pontos')
elif comandante == 2:
    dicaomnath0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicaomnath0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicaomnath1 = str(input('O artista da carta é: Mike Bierek, precisa de mais dicas? S/N ')).upper().strip()
        if dicaomnath1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicaomnath2 = str(input('O comandante precisa de uma mana verde para ser castado, precisa de mais dicas? '
                                    'S/N ')).upper().strip()
            if dicaomnath2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O comandante custa 3 manas')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora dê sua resposta, quais dos comandantes a seguir é o correto? '))
                if resposta0 != 2:
                    print('Você errou')
                else:
                    print(''
                          f'\nParabéns você acertou o comandante correto é o Omanth, Locus of Mana e ficou com {pontos} '
                          f'pontos')
            elif dicaomnath2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Mere')
                resposta0 = int(input('Agora dê sua resposta de acordo com o número de cada comandante, '
                                      'qual é o comandante correto? '))
                if resposta0 != 2:
                    print('Você errou')
                else:
                    print(''
                          f'\nParabéns você acertou o comandante correto é o Omnath, Locus of Mana e ficou com {pontos} pontos')
        elif dicaomnath1 == 'N':
            print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Mere')
            resposta0 = int(input('Agora dê sua resposta de acordo com o número de cada comandante, '
                                  'qual é o comandante correto? '))
            if resposta0 != 2:
                print('Você errou')
            else:
                print(''
                      f'\nParabéns você acertou o comandante correto é o {comandante} e ficou com {pontos} pontos')
    elif dicaomnath0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 2:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Omnath, Locus of Mana e ficou com {pontos} pontos')
elif comandante == 3:
    dicagired0 = str(input(' O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicagired0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicagired1 = str(input(' O artista da carta é Yongjae Choi, precisa de mais dicas? S/N ')).upper().strip()
        if dicagired1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicagired2 = str(input(' O comandante precisa de no minímo 3 de cores diferentes para ser conjurado, '
                                  'precisa de mais dicas? S/N ')).upper().strip()
            if dicagired2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O comandante custa 6 manas')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 3:
                    print('Você errou')
                else:
                    print(f'Parabéns o comandante correto é o Ghired, Exilado do Conclave, você ficou com {pontos} '
                          f'pontos')
            elif dicagired2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 3:
                    print('Você errou')
                else:
                    print(f'Parabéns o comandante correto é o Ghired, Exilado do Conclave, você ficou com {pontos} '
                          f'pontos')
        elif dicagired1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 3:
                print('Você erou')
            else:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Ghired, Exilado do Conclave e'
                      f' você ficou com {pontos} pontos')
    elif dicagired0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 3:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Ghired, Exilado do Conclave e'
                  f' você ficou com {pontos} pontos')
elif comandante == 4:
    dicasai0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicasai0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicasai1 = str(input('O artista da cart é Adam Paquette, precisa de mais dicas? S/N ')).upper().strip()
        if dicasai1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicasai2 = str(input('Segue o flavor do comandante: A perícia sem o talento artístico é só uma forma sofisticada de encher o ferro-velho, '
                                 'precisa de mais dicas? S/N ')).upper().strip()
            if dicasai2 == 'S':
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O comandante custa 3 manas')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante:'))
                if resposta0 != 4:
                   print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Sai, Topterista Mestre e'
                          f' você ficou com {pontos} pontos')
            elif dicasai2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante:'))
                if resposta0 != 4:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Sai, Topterista Mestre e'
                          f' você ficou com {pontos} pontos')
        elif dicasai1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 4:
                print('Você errou')
            else:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Sai, Topterista Mestre e'
                      f' você ficou com {pontos} pontos')
    elif dicasai0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante:'))
        if resposta0 != 4:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Sai, Topterista Mestre e'
                  f' você ficou com {pontos} pontos')
elif comandante == 5:
    dicaobeka0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicaobeka0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicaobeka1 = str(input('O artista da carta é Jesper Ejsing, precisa de mais dicas? S/N ')).upper().strip()
        if dicaobeka1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicaobeka2 = str(input('O comandante custa 4 manas, precisa de mais dicas? S/N ')).upper().strip()
            if dicaobeka2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O flavor da carta é: Estou entendiada com o agora')
                print(' ')
                print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 5:
                 print('Você ERROU')
                else:
                 print(' '
                      f'\nParabéns você acertou o comandante correto é o Obeka, Cronologista Bruta e'
                      f' você ficou com {pontos} pontos')
            elif dicaobeka2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 5:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é a Obeka, Cronologista Bruta e'
                          f' você ficou com {pontos} pontos')
        elif dicaobeka1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 5:
                print('Você errou')
            else:

                print(' '
                      f'\nParabéns você acertou o comandante correto é o Obeka, Cronologista Bruta e'
                      f' você ficou com {pontos} pontos')
    elif dicaobeka0 == 'N':
        print(' ')
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input(' Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 5:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Obeka, Cronologista Bruta e'
                  f' você ficou com {pontos} pontos')
elif comandante == 6:
    dicamirko0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicamirko0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicamirko1 = str(input('O artista da carta é Chase Stone, precisa de mais dicas? S/N ')).upper().strip()
        if dicamirko1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicamirko2 = str(input('É necessário no mínimo 1 de mana azul para ser castado, precisa de mais dicas? S/N '
                                   '')).upper().strip()
            if dicamirko2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O comandante custa 5 manas')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 6:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Mirko Vosk, Sugador de Mentes e'
                          f' você ficou com {pontos} pontos')
            elif dicamirko2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 6:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Mirko Vosk, Sugador de Mentes e'
                          f' você ficou com {pontos} pontos')
        elif dicamirko1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 6:
                print('Você errou')
            else:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Mirko Vosk, Sugador de Mentes e'
                      f' você ficou com {pontos} pontos')
    elif dicamirko0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 6:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Mirko Vosk, Sugador de Mentes e'
                  f' você ficou com {pontos} pontos')
elif comandante == 7:
    dicakadena0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicakadena0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicakadena1 = str(input('O artista da carta é Chase Stone, precisa de mais dicas? S/N ')).upper().strip()
        if dicakadena1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicakadena2 = str(input('É necessário no mínimo 1 de mana azul para ser castado, precisa de mais dicas? S/N '
                                   '')).upper().strip()
            if dicakadena2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('O flavor do comandante é o seguinte: A única coisa constante na vida é o desconhecido')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 7:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Kadena, Feiticeira Serpentil e'
                          f' você ficou com {pontos} pontos')
            elif dicakadena2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 7:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Kadena, Feiticeira Serpentil e'
                          f' você ficou com {pontos} pontos')
        elif dicakadena1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 7:
                print('Você errou')
            else:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Kadena, Feiticeira Serpentil e'
                      f' você ficou com {pontos} pontos')
    elif dicakadena0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 7:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Kadena, Feiticeira Serpentil e'
                  f' você ficou com {pontos} pontos')
elif comandante == 8:
    dicameren0 = str(input('O comandante é uma criatura, precisa de mais dicas? S/N ')).upper().strip()
    if dicameren0 == 'S':
        pontos = pontos - 1
        print(' ')
        dicameren1 = str(input('O artista da carta é Mark Winters, precisa de mais dicas? S/N ')).upper().strip()
        if dicameren1 == 'S':
            pontos = pontos - 1
            print(' ')
            dicameren2 = str(input('É necessário no mínimo 1 de mana preta para ser castado, precisa de mais dicas? S/N '
                                   '')).upper().strip()
            if dicameren2 == 'S':
                pontos = pontos - 1
                print('')
                print('**ATENÇÃO!! ÚLTIMA DICA!**')
                print(' ')
                print('Custa 4 de manas para ser conjurado')
                print(' ')
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 8:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Meren of Clan Nel Toth e'
                          f' você ficou com {pontos} pontos')
            elif dicameren2 == 'N':
                print('Estes são os nossos comandantes:  '
                      '\n1 - Kogla, O Símio Titânico'
                      '\n2 - Omnath, Locus of Mana'
                      '\n3 - Ghired, Exilado do Conclave'
                      '\n4 - Sai, Topterista Mestre'
                      '\n5 - Obeka, Cronologista Bruta'
                      '\n6 - Mirko Vosk, Sugador de Mentes'
                      '\n7 - Kadena - Feiticeira Serpentil'
                      '\n8 - Meren of Clan Nel Toth'
                      '\n ')
                resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
                if resposta0 != 8:
                    print('Você errou')
                else:
                    print(' '
                          f'\nParabéns você acertou o comandante correto é o Meren of Clan Nel Toth e'
                          f' você ficou com {pontos} pontos')
        elif dicameren1 == 'N':
            print('Estes são os nossos comandantes:  '
                  '\n1 - Kogla, O Símio Titânico'
                  '\n2 - Omnath, Locus of Mana'
                  '\n3 - Ghired, Exilado do Conclave'
                  '\n4 - Sai, Topterista Mestre'
                  '\n5 - Obeka, Cronologista Bruta'
                  '\n6 - Mirko Vosk, Sugador de Mentes'
                  '\n7 - Kadena - Feiticeira Serpentil'
                  '\n8 - Meren of Clan Nel Toth'
                  '\n ')
            resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
            if resposta0 != 8:
                print('Você errou')
            else:
                print(' '
                      f'\nParabéns você acertou o comandante correto é o Meren of Clan Nel Toth e'
                      f' você ficou com {pontos} pontos')
    elif dicameren0 == 'N':
        print('Estes são os nossos comandantes:  '
              '\n1 - Kogla, O Símio Titânico'
              '\n2 - Omnath, Locus of Mana'
              '\n3 - Ghired, Exilado do Conclave'
              '\n4 - Sai, Topterista Mestre'
              '\n5 - Obeka, Cronologista Bruta'
              '\n6 - Mirko Vosk, Sugador de Mentes'
              '\n7 - Kadena - Feiticeira Serpentil'
              '\n8 - Meren of Clan Nel Toth'
              '\n ')
        resposta0 = int(input('Agora digite sua resposta de acordo com o número de cada comandante: '))
        if resposta0 != 8:
            print('Você errou')
        else:
            print(' '
                  f'\nParabéns você acertou o comandante correto é o Meren of Clan Nel Toth  e'
                  f' você ficou com {pontos} pontos')