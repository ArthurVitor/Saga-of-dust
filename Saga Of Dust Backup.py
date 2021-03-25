#Saga of dust v1
import random, time

nm = str(input('Qual seu nome? '))
time.sleep(0.5)
print('Existem 3 aventureiros para você escolher.\n'
      'Aqui estam listados os 3 e suas estatisticas')
print('<>'*30)
print('''Arthur:
Fogo

Vida:247
Atk:12-56
Def:22  
Vel: 26''')
print('<>'*30)
print('''Diego:
Terra

Vida:227
Atk:10-58
Def:15
Vel:15''')
print('<>'*30)

print('''Bia:
Água

Vida:271
Atk:10-53
Def:21
Vel:13''')
print('<>'*30)
print(' ')
print('Vou lhe explicar como funciona o jogo')
print('O jogo funciona com um sistema de turnos que mudam de acordo com uma ação, seja ela atacar/correr/defende e etc')
print('Para você executar uma ação tera que escolher uma dessas opções')
print(' ')
print('Atacar [A]\n', end=''
      'A opção atacar ira causar dano ao inimigo\n'
      'Defender [D]\n'
      'Com a opção defender você ira tentar se defender do ataque de seu inimigo\n'
      'Correr [C]\n'
      'Se você escolher a opção correr você ira sair da partida\n')
print(' ')
print('Vou lhe mostrar um breve tutorial do jogo')
print(' ')
tt = ' '
while tt not in 'ADC':
    print('Atacar [A]\n'
    'Defender [D]\n'
    'Correr [C]\n')
    msv = 200
    vida = 245
    while vida >= 1:
        tt = str(input('Oque você deseja fazer? ')).strip().upper()[0]
        if tt == 'C':
            break
        if tt == 'A' and msv >= 1 and vida >= 1:
            jgt = random.randint(12, 56)
            msv -= jgt
            if msv <= 0:
                print('O monstro está morto!')
                print('Você ganhou!')
                break
            print(f'Você causou {jgt} de dano ao monstro')
            print(f'O monstro está com {msv} de vida!\n')
            print('Agora é a vez do monstro\n')
            mst = random.randint(10, 35)
            vida -= mst
            if vida <= 0:
                print('Você está morto!')
                print('Você ganhou!')
                break
            print(f'O monstro causou {mst} de dano a você!')
            print(f'Você está com {vida} de vida!\n')
print(' ')
esl = ' '
while esl not in 'ABD':
    esl = str(input('Escolha qual aventureiro você deseja usar: ')).strip().upper()[0]
    if esl == 'A':
        Vida = 247
        Atk1 = 12
        Atk2 = 56
        print('Você escolheu o aventureiro Arthur; Boa Sorte na sua aventura!')
    elif esl == 'B':
        Vida = 271
        Atk1 = 10
        Atk2 = 58
        print('Você escolheu o aventureiro Bia; Boa Sorte na sua aventura!')
    elif esl == 'D':
        Vida = 227
        Atk1 = 10
        Atk2 = 53
        print('Você escolheu o aventureiro Diego; Boa Sorte na sua aventura!')

while True:
    avt = str(input('Oque você deseja fazer? Suicidio ou Andar? ')).strip().upper()[0]
    if avt == 'S':
        print('Você se matou. Fim de jogo')
        break
    elif avt == 'A':
            an = random.randint(1, 5)
            if an == 2 or 4:
                mnl = random.randint(1, 3)
                print(f'Você achou um monstro level {mnl}')
                if mnl == 1:
                    msv = 200
                    vida = Vida
                    while msv >= 1:
                        tt = str(input('Oque você deseja fazer? ')).strip().upper()[0]
                        if tt == 'C':
                            break
                        if tt == 'A' and msv >= 1 and vida >= 1:
                            jgt = random.randint(12, 56)
                            msv -= jgt
                            if msv <= 0:
                                print('O monstro está morto!')
                                print('Você ganhou!')
                                break

                            print(f'Você causou {jgt} de dano ao monstro')
                            print(f'O monstro está com {msv} de vida!\n')
                            print('Agora é a vez do monstro\n')
                            mst = random.randint(15, 40)
                            vida -= mst
                            if vida <= 0:
                                print('Você está morto!')
                                print('Você ganhou!')
                                break
                            print(f'O monstro causou {mst} de dano a você!')
                            print(f'Você está com {vida} de vida!\n')
                if mnl == 2:
                        msv = 250
                        vida = Vida
                        while msv >= 1:
                            tt = str(input('Oque você deseja fazer? ')).strip().upper()[0]
                            if tt == 'C':
                                break
                            if tt == 'A' and msv >= 1 and vida >= 1:
                                jgt = random.randint(12, 56)
                                msv -= jgt
                                if msv <= 0:
                                    print('O monstro está morto!')
                                    print('Você ganhou!')
                                    break

                                print(f'Você causou {jgt} de dano ao monstro')
                                print(f'O monstro está com {msv} de vida!\n')
                                print('Agora é a vez do monstro\n')
                                mst = random.randint(25, 50)
                                vida -= mst
                                if vida <= 0:
                                    print('Você está morto!')
                                    print('Você ganhou!')
                                    break
                                print(f'O monstro causou {mst} de dano a você!')
                                print(f'Você está com {vida} de vida!\n')
                if mnl == 3:
                        msv = 300
                        vida = Vida
                        while msv >= 1:
                            tt = str(input('Oque você deseja fazer? ')).strip().upper()[0]
                            if tt == 'C':
                                break
                            if tt == 'A' and msv >= 1 and vida >= 1:
                                jgt = random.randint(12, 56)
                                msv -= jgt
                                if msv <= 0:
                                    print('O monstro está morto!')
                                    print('Você ganhou!')
                                    break

                                print(f'Você causou {jgt} de dano ao monstro')
                                print(f'O monstro está com {msv} de vida!\n')
                                print('Agora é a vez do monstro\n')
                                mst = random.randint(40, 80)
                                vida -= mst
                                if vida <= 0:
                                    print('Você está morto!')
                                    print('Você ganhou!')
                                    break
                                print(f'O monstro causou {mst} de dano a você!')
                                print(f'Você está com {vida} de vida!\n')
