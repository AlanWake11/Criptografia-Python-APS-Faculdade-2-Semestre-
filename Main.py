from time import sleep
import os
import pygame

pygame.init()

def codigo_morse(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'Aa':
            tradutor += '.- '
        elif letra in 'Bb':
            tradutor += '-... '
        elif letra in 'Cc':
            tradutor += '-.-. '
        elif letra in 'Dd':
            tradutor += '-.. '
        elif letra in 'Ee':
            tradutor += '. '
        elif letra in 'Ff':
            tradutor += '..-. '
        elif letra in 'Gg':
            tradutor += '--. '
        elif letra in 'Hh':
            tradutor += '.... '
        elif letra in 'Ii':
            tradutor += '.. '
        elif letra in 'Jj':
            tradutor += '.--- '
        elif letra in 'Kk':
            tradutor += '-.- '
        elif letra in 'Ll':
            tradutor += '.-.. '
        elif letra in 'Mm':
            tradutor += '-- '
        elif letra in 'Nn':
            tradutor += '-. '
        elif letra in 'Oo':
            tradutor += '--- '
        elif letra in 'Pp':
            tradutor += '.--. '
        elif letra in 'Qq':
            tradutor += '--.- '
        elif letra in 'Rr':
            tradutor += '.-. '
        elif letra in 'Ss':
            tradutor += '... '
        elif letra in 'Tt':
            tradutor += '- '
        elif letra in 'Uu':
            tradutor += '..- '
        elif letra in 'Vv':
            tradutor += '...- '
        elif letra in 'Ww':
            tradutor += '.-- '
        elif letra in 'Xx':
            tradutor += '-..- '
        elif letra in 'Yy':
            tradutor += '-.-- '
        elif letra in 'Zz':
            tradutor += '--.. '
        elif letra in '0':
            tradutor += '----- '
        elif letra in '1':
            tradutor += '.---- '
        elif letra in '2':
            tradutor += '..--- '
        elif letra in '3':
            tradutor += '...-- '
        elif letra in '4':
            tradutor += '....- '
        elif letra in '5':
            tradutor += '..... '
        elif letra in '6':
            tradutor += '-.... '
        elif letra in '7':
            tradutor += '--... '
        elif letra in '8':
            tradutor += '---.. '
        elif letra in '9':
            tradutor += '----. '        
        elif letra in ' ':
            tradutor += ' '
        else:
            tradutor += letra
    return tradutor

def linha_cima():
    print('╔', end='')
    print('═' * 100, end='')
    print('╗')

def linha_cima2():
    print('╔', end='')
    print('═' * 170, end='')
    print('╗')

def linha_baixo():
    print('╚', end='')
    print('═' * 100, end='')
    print('╝')

def linha_baixo2():
    print('╚', end='')
    print('═' * 170, end='')
    print('╝')

def alfabeto_morse():
    print('{:^100}'.format('Alfabeto Morse'))
    print()
    lista1 = ['║', '.- = Aa ', '--. = Gg ', '-- = Mm ', '... = Ss ', '-.-- = Yy', '....- = 4', '║']
    print('   {:>1}   {:^6}   {:>14}   {:>12}   {:>13}   {:>11}   {:>13}   {:>1}'.format(*lista1))
    lista2 = ['║', '-... = Bb', '.... = Hh','-. = Nn','- = Tt','--.. = Zz','..... = 5', '║']
    print('   {:>1}   {:^6}   {:>13}   {:>11}   {:>11}   {:>14}   {:>13}   {:>1}'.format(*lista2))
    lista3 = ['║', '-.-. = Cc', '.. = Ii','--- = Oo','..- = Uu','----- = 0','-.... = 6', '║']
    print('   {:>1}   {:^6}   {:>11}   {:>14}   {:>12}   {:>12}   {:>13}   {:>1}'.format(*lista3))
    lista4 = ['║', '-.. = Dd', '.--- = Jj','.--. = Pp','...- = Vv','.---- = 1','--... = 7', '║']
    print('   {:>1}   {:^6}   {:>14}   {:>13}   {:>12}   {:>11}   {:>13}   {:>1}'.format(*lista4))
    lista5 = ['║', '. = Ee', '-.- = Kk','--.- = Qq','.-- = Ww','..--- = 2','---.. = 8', '║']
    print('   {:>1}   {:^6}   {:>15}   {:>14}   {:>11}   {:>12}   {:>13}   {:>1}'.format(*lista5))
    lista6 = ['║', '..-. = Ff', '.-.. = Ll','.-. = Rr','-..- = Xx','...-- = 3','----. = 9', '║']
    print('   {:>1}   {:^6}   {:>13}   {:>12}   {:>13}   {:>11}   {:>13}   {:>1} \n'.format(*lista6))
    

while True:
    os.system('cls')
    linha_cima()
    print('{:<}{:^110}{:>}'.format('║', '\033[1;34mSistema de Segurança AM\033[m', '║'))
    print('{:<}{:^20}{:>75}{:>6}'.format('║', 'CODIGO MORSE [ 1 ]', 'Criptografia AES [ 2 ]','║'))
    print('{:<}{:>101}'.format('║', '║'))
    print('{:<}{:^13}{:>88}'.format('║', 'SAIR [ 3 ]', '║'))
    linha_baixo()
    
    escolha = input('Selecione a opção: ')
    
    while escolha == '1':
        os.system('cls')
        linha_cima()
        print('{:<}{:^100}{:>}'.format('║', 'CÓDIGO MORSE', '║'))
        print('{:<}{:^20}{:>81}'.format('║', 'Criptografar [ 1 ]', '║'))
        print('{:<}{:>101}'.format('║', '║'))
        print('{:<}{:^24}{:>77}'.format('║', 'Descriptografar [ 2 ]', '║'))
        print('║ {:>100}'.format('║'))
        print('{:<}{:^22}{:>79}'.format('║', 'Alfabeto Morse [ 3 ]', '║'))
        print('║ {:>100}'.format('║'))
        print('{:<}{:^15}{:>86}'.format('║', 'Voltar [ 4 ]', '║'))
        linha_baixo()
        
        opção = input('Qual é a sua opção? ')

        if opção == '1':    
            os.system('cls')
            linha_cima2()
            print('║ {:^170}'.format('Escreva uma mensagem para tranforma-lá em MORSE'))
            print('║')
            frase = str(input('║ Digite sua mensagem: '))
            if len(frase) > 128:
                pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
                pygame.mixer.music.play()
                print('║ \033[3;31mExcedeu limite de caracteres [128]\033[m')
                print('║ Retornando ao começo do programa')
                sleep(1)
                break

            print('║ Criptografando mensagem...')
            sleep(5)
            pygame.mixer.music.load("Mario-coin-sound.mp3")
            pygame.mixer.music.play()
            print('║ \033[4;32mMensagem codificada!\033[m')
            sleep(1)
            print('║')
            print('║ Sua codificação é: ', end='')
            
            if len(codigo_morse(frase)) > 675:
                print(codigo_morse(frase)[:150])
                print(f'║ {codigo_morse(frase)[151:319]}')
                print(f'║ {codigo_morse(frase)[320:488]}')
                print(f'║ {codigo_morse(frase)[489:657]}')
                print(f'║ {codigo_morse(frase)[658:]}')

            elif len(codigo_morse(frase)) > 500:
                print(codigo_morse(frase)[:150])
                print(f'║ {codigo_morse(frase)[151:319]}')
                print(f'║ {codigo_morse(frase)[320:488]}')
                print(f'║ {codigo_morse(frase)[489:]}')

            elif len(codigo_morse(frase)) > 325:
                print(codigo_morse(frase)[:150])
                print(f'║ {codigo_morse(frase)[151:319]}')
                print(f'║ {codigo_morse(frase)[320:]}')
            
            elif len(codigo_morse(frase)) > 150:
                print(codigo_morse(frase)[:150])
                print(f'║ {codigo_morse(frase)[150:]}')
            else:
                print(codigo_morse(frase))
            
            linha_baixo2()
            input('\nPressione ENTER para voltar...')

        elif opção == '2':
            listmsg = []
            os.system('cls')
            linha_cima()
            print('║ {:^100}'.format('Escreva letra em MORSE para tranforma-lá em TEXTO!'))
            print('║')
            while True:
                msg = str(input('║ Digite a letra: '))
                if msg == '.-':
                    listmsg.append('A')
                elif msg == '-...':
                    listmsg.append('B')
                elif msg == '-.-.':
                    listmsg.append('C')
                elif msg == '-..':
                    listmsg.append('D')
                elif msg == '.':
                    listmsg.append('E')
                elif msg == '..-.':
                    listmsg.append('F')
                elif msg == '--.':
                    listmsg.append('G')
                elif msg == '....':
                    listmsg.append('H')
                elif msg == '..':
                    listmsg.append('I')
                elif msg == '.---':
                    listmsg.append('J')
                elif msg == '-.-':
                    listmsg.append('K')
                elif msg == '.-..':
                    listmsg.append('L')
                elif msg == '--':
                    listmsg.append('M')
                elif msg == '-.':
                    listmsg.append('N')
                elif msg == '---':
                    listmsg.append('O')
                elif msg == '.--.':
                    listmsg.append('P')
                elif msg == '--.-':
                    listmsg.append('Q')
                elif msg == '.-.':
                    listmsg.append('R')
                elif msg == '...':
                    listmsg.append('S')
                elif msg == '-':
                    listmsg.append('T')
                elif msg == '..-':
                    listmsg.append('U')
                elif msg == '...-':
                    listmsg.append('V')
                elif msg == '.--':
                    listmsg.append('W')
                elif msg == '-..-':
                    listmsg.append('X')
                elif msg == '-.--':
                    listmsg.append('Y')
                elif msg == '--..':
                    listmsg.append('Z')
                elif msg == '.----':
                    listmsg.append('1')
                elif msg == '..---':
                    listmsg.append('2')
                elif msg == '...--':
                    listmsg.append('3')
                elif msg == '....-':
                    listmsg.append('4')
                elif msg == '.....':
                    listmsg.append('5')
                elif msg == '-....':
                    listmsg.append('6')
                elif msg == '--...':
                    listmsg.append('7')
                elif msg == '---..':
                    listmsg.append('8')
                elif msg == '----.':
                    listmsg.append('9')
                elif msg == '-----':
                    listmsg.append('0')
                elif msg == '.-.-.-':
                    listmsg.append('.')
                elif msg == '--..--':
                    listmsg.append(',')
                elif msg == ' ':
                    listmsg.append(' ')
                else:
                    print('║ \033[3;31mLetra não reconhecida! Tente novamente\033[m')
                    sleep(1)
                resp = ' '
                while resp not in 'SN':
                    resp = str(input('║ Add mais uma letra?[S/N]: ')).strip().upper()[0]
                if resp == 'N':
                    break

            print('║ Decodificando as letras...')
            sleep(5)
            pygame.mixer.music.load("Mario-coin-sound.mp3")
            pygame.mixer.music.play()
            print('║ \033[4;32mLetras decodificadas!\033[m')
            sleep(1)
            print('║')
            print('║ Sua mensagem é: ', end='')
            for letra in listmsg:
                print(letra, end='')
            print()
            linha_baixo()    
            listmsg.clear()

            input('\nPressione ENTER para voltar... ')
            
        elif opção == '3':
            os.system('cls')
            alfabeto_morse()
            input('Pressione ENTER para voltar... ')
        
        elif opção == '4':
            print('Voltando...')
            sleep(2)
            break
        
        else:
            pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
            pygame.mixer.music.play()
            print('\033[3;31mERRO, tente novamente com argumentos válidos\033[m')
            sleep(1)

    while escolha == '2':
        os.system('cls')
        linha_cima()
        print('{:<}{:^100}{:>}'.format('║', 'Criptografia AES', '║'))
        print('{:<}{:^20}{:>81}'.format('║', 'Criptografar [ 1 ]', '║'))
        print('{:<}{:>101}'.format('║', '║'))
        print('{:<}{:^24}{:>77}'.format('║', 'Descriptografar [ 2 ]', '║'))
        print('║ {:>100}'.format('║'))
        print('{:<}{:^15}{:>86}'.format('║', 'Voltar [ 3 ]', '║'))
        linha_baixo()
        
        opção = input('Qual é a sua opção? ')
        
        if opção == '1':       
            os.system('cls')
            alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

            chave = 3
            
            linha_cima2()
            print('║ {:^170}'.format('Escreva uma mensagem para codificar'))
            print('║')
            mensagem = str(input('║ Digite sua mensagem: ')).strip().lower()
            if len(mensagem) > 128:
                pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
                pygame.mixer.music.play()
                print('║ \033[3;31mExcedeu limite de caracteres [128]\033[m')
                print('║ Retornando ao começo do programa')
                sleep(1)
                break

            n = len(alfabeto)

            cifrada = ''
            for letra in mensagem:
                indice = alfabeto.index(letra)
                nova_letra = alfabeto[(indice + chave)%n]
                cifrada += nova_letra

            print('║ Criptografando sua mensagem...')
            sleep(5)
            pygame.mixer.music.load("Mario-coin-sound.mp3")
            pygame.mixer.music.play()
            print('║ \033[4;32mMensagem criptografada!\033[m')
            sleep(1)
            print('║')
            print(f'║ Sua mensagem é: {cifrada}')
            linha_baixo2()

            input('Pressione ENTER para voltar... ')

        elif opção == '2':
            os.system('cls')
            alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

            chave = -3
            
            linha_cima2()
            print('║ {:^170}'.format('Escreva uma mensagem para decodifica-lá'))
            print('║')
            mensagem = str(input('║ Digite sua mensagem: ')).strip().lower()
            if len(mensagem) > 128:
                pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
                pygame.mixer.music.play()
                print('║ \033[3;31mExcedeu limite de caracteres [128]\033[m')
                print('║ Retornando ao começo do programa')
                sleep(1)
                break

            n = len(alfabeto)

            cifrada = ''
            for letra in mensagem:
                indice = alfabeto.index(letra)
                nova_letra = alfabeto[(indice + chave)%n]
                cifrada += nova_letra

            print('║ Descriptografando sua mensagem...')
            sleep(5)
            pygame.mixer.music.load("Mario-coin-sound.mp3")
            pygame.mixer.music.play()
            print('║ \033[4;32mMensagem Decodificada!\033[m')
            sleep(1)
            print('║')
            print(f'║ Sua mensagem é: {cifrada}')
            linha_baixo2()

            input('Pressione ENTER para voltar... ')

        elif opção == '3':
            print('Voltando...')
            sleep(2)
            escolha = '1'
            opção = '4'

        else:
            pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
            pygame.mixer.music.play()
            print('\033[3;31mERRO, tente novamente com argumentos válidos\033[m')
            sleep(1)

    while escolha == '3':
        pygame.mixer.music.load("Goodnight.mp3")
        pygame.mixer.music.play()
        sleep(6)
        print('programa encerrado!')
        exit()
            
    while escolha != '1' and '2' and '3':
        pygame.mixer.music.load("som de erro de windows (download) (320 kbps).mp3")
        pygame.mixer.music.play()
        print('\033[3;31mERRO, tente novamente com argumentos válidos\033[m')
        sleep(1)
        break
