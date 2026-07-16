import random
import math
bolsa = ['Faca velha']
esquerda = 0
direita = 0
meio = 0
def inicio():
    print("As aventuras de você mesmo \n"
    "1. Começar \n"
    "2. Sair")
    game = input('> ')
    if game == '1':
         direcao = floresta() 
    elif game == '2':
        print('Tchau :D')

def floresta():
        if 'Maçã' in bolsa:
            print('\n1.Olhar o mapa \n'
            "2. Ir para o sul \n"
            "3. Ir para o norte \n"
            "4. Ir para o leste \n"
            "5. Ir para o oeste \n"
            "6. Olhar a bolsa")
            direcao = input('> ')
            if direcao == '1':
                mapa()
            elif direcao == "2":
                sul()
            elif direcao == '3':
                norte()
            elif direcao == '4':
                leste()
            elif direcao == '5':
                oeste()
            elif direcao == '6':
                ItemBolsa()
        else:
            print("\nVocê é um jovem aldeão que mora em uma cidade remota nas montanhas e decide ir colher cogumelos na floresta próxima para fazer uma sopa \n"
            'Por descuido você escorrega em um barranco e acaba se perdendo: \n'
            '1. Olhar em volta \n'
            "2. Ir para o sul \n"
            "3. Ir para o norte \n"
            '4. Ir para o leste \n'
            "5. Ir para o oeste")
            direcao = input('> ')
            if direcao == '1':
                area()
            elif direcao == "2":
                sul()
            elif direcao == '3':
                norte()
            elif direcao == '4':
                leste()
            elif direcao == '5':
                oeste()
            elif direcao == '6':
                ItemBolsa()
            

def ItemBolsa():
    print('\nDentro da bolsa você têm:')
    for item in bolsa:
        print('- ', item)
    direcao = floresta()

def mapa():
    print('\n /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
' /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
'  |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   \n'
' \n'
' /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\             /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\ \n'
' /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\             /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\  \n'
'  |  |   |   |  |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |         / \   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |   \n'
'                                                                          ____| |__   \n'
' /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  /         \  /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
' /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /___________\ /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
'  |  |    |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |  |    _   _  |  |  |    |  |   |  |   |  |   |  |   |  |   |  |   |  |   \n'
'                                                                        |   | | |_| | \n'
' /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ |___|_|_____| /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  /|\/|\ \n'
' /|\/|\  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\               /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  /|\/|\ \n'
'  |  |    |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |                 |  |   |  |   |  |   |  |   |  |   |  |   |  |    |  | \n'
'         \n'
' /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
' /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'  |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |          |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  | \n'
'  \n'
'     /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'     /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'      |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |          |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  | \n'
'   \n'
'                                            /|\/|\        /|\/|\                              /|\/|\        /|\/|\ \n'
' /|\/|\ /|\/|\ /|\/|\    _________   /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\       O        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\   ___    __           /|\/|\ \n'
' /|\/|\ /|\/|\ /|\/|\   /  ~~  ~~ \  /|\/|\  |  |  /|\/|\  |  |  /|\/|\      /|\       /|\/|\  |  |  /|\/|\  |  |  /|\/|\   | |   |  |_____     /|\/|\ \n'
'  |  |   |  |   |  |   / ~~ ~~ ~~  \  |  |          |  |          |  |       / \        |  |          |  |          |  |    | |   |     _  |     |  |  \n' 
'                       \~~ ~~ ~~ ~~/                                                                                        |_|   |    | | | \n'
'                        \_________/ \n'
' /|\/|\ /|\/|\ /|\/|\                         /|\/|\        /|\/|\        /|\/|\               /|\/|\        /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
' /|\/|\ /|\/|\ /|\/|\                  /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'  |  |   |  |   |  |                   /|\/|\  |  |  /|\/|\  |  |  /|\/|\  |  |         /|\/|\  |  |  /|\/|\  |  |  /|\/|\  |  |   |  |   |  |   |  |  \n'
'                                        |  |          |  |          |  |                 |  |          |  |          |  | \n'
' \n'
'     /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'     /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\        /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'      |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |          |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |  \n'
'                                                                                                                                                        \n'
'   /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\         /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
'   /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\         /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\  \n'
'    |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |           |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   \n'
'                                                                                                                                                        \n'
'   /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\     __________         /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'   /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\    /          \__      /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ /|\/|\ \n'
'    |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |   |  |    /     _        \      |  |   |  |   |  |   |  |   |  |   |  |   |  |  \n'
'                                                                                 /_____( )________\ \n'
)
    print('Ao norte você vê sua casa, ao sul uma caverna, a oeste um lago e a leste algumas ruínas')
    direcao = floresta()

def area():
    global bolsa

    bolsa = ['Mapa', 'Bússola', 'Maçã']
    
    

    print('\nAo olhar em volta, você avista a bolsa que trouxe junto e a pega \n'
    'Dentro da bolsa você têm:')
    for item in bolsa:
        print('- ', item)
    direcao = floresta()

def sul():
        print('\nVocê decide ir para o sul e encontra uma toca de urso \n'
        '1. Voltar \n'
        '2. Olhar mais de perto \n'
        '3. Jogar uma pedra')
        acao = input('> ')
        if acao == '1':
            direcao = floresta()
        elif acao == '2':
            olhar()
        elif acao == '3':
            pedra()

def sul2():
        print('\nVocê sai da caverna \n'
        '1. Voltar \n'
        '2. Olhar mais de perto \n'
        '3. Jogar uma pedra \n')
        acao = input('> ')
        if acao == '1':
            direcao = floresta()
        elif acao == '2':
            olhar2()
        elif acao == '3':
            pedra()

def olhar():
    print('\nVocê decide olhar mais de perto a caverna e vê o urso dormindo \n'
        'Ao lado do urso você vê um esqueleto com algumas roupas e uma bolsa \n'
        '1. Voltar \n'
        '2. Se esgueirar até o esqueleto \n'
        '3. Atacar o urso de surpresa')
    acao = input('> ')
    if acao == '1':
        direcao = floresta()
    elif acao == '2':
        try:
            bolsa
            print('\nVocê consegue se esgueirar até o esqueleto sem acordar o urso e, ao vasculha-lo, você escontra alguns trapos e uma espada')
            bolsa.extend(['Trapos', 'Espada'])
            print('Você guarda os trapos e a espada na bolsa')
            acao = sul2()
        except:
            print('Você chega até o esqueleto mas ainda não achou sua bolsa e não tem onde guardar os itens')
            sul()
    elif acao == '3':
        luta1()

def olhar2():
    print('\nVocê decide olhar mais de perto a caverna e vê o urso dormindo \n'
        'Ao lado do urso você vê um esqueleto ja pilhado \n'
        '1. Voltar \n'
        '2. Se esgueirar até o esqueleto \n'
        '3. Atacar o urso de surpresa')
    acao = input('> ')
    if acao == '1':
        direcao = floresta()
    elif acao == '2':
        print('\nVocê consegue se esgueirar até o esqueleto sem acordar o urso e não encontra nada')
        acao = sul2()
    elif acao == '3':
        print('\nVocê ataca o urso de surpresa com sua nova espada e consegue mata-lo \n'
              '1. Voltar \n'
              '2. Desmantelar o urso')
        acao = input('>')
        if acao == '1':
             direcao = floresta()
        elif acao == '2':
            print('\nVocê desmantela o urso e guarda sua carne e pele \n'
                  '1. Voltar')
            bolsa.extend(['Pele de urso', 'Carne de urso'])
            voltar = input('> ')
            if voltar == '1':
                direcao = floresta()

def pedra():
    try:
        bolsa
        if 'Pele de urso' in bolsa:
            jogada = random.randrange(4)
            if jogada <= 2:
                print('\nO urso acordou')
                acao = luta2()
            elif jogada == 3:
                print('O urso ainda está dormindo')
                sul2()
    except NameError:
        print('A pedra bate no chão da caverna')
        sul2()        
        
def luta1():
    urso = 50
    print('\nVocê ataca o urso de surpresa com sua faca e consegue feri-lo.\n'
          'O urso, ferido e furioso, se vira para você.')
    hp = 100
    armaduraU = 20
    while urso > 0 and hp >0:
        print('                                     \n' 
'                  \n' 
'						                 \n'
'						                      \n'
'			                                 \n'
'	   ( )      _-                            \n'
'	 _(|  )- - _ )                             \n' 
'     __- ( |          \                              \n' 
'	/             \                              \n'
'	/       o.  |o }                             \n'
'	|            \ ;                             \n'
'	   \_         __\                             \n'
'              \'-_    \.//                           \n'
'	         / ----                              \n'
'	        /                                      \n'
'          _                                    \n'
'	  _-                                   \n'
'								  \n'
'        \n')
        print(f'\nUrso\nHP: {urso}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')
        acao = input('> ')
        if acao == '1':
            danoU = random.randrange(10, 51)
            dano = 10
            danoF = dano-((dano*armaduraU)/100)
            urso -= danoF
            hp -= danoU
            print(f'\nVocê atacou o urso e causou {danoF} de dano!')
            print(f'O urso te atacou e causou {danoU}')
            print(f'Seu HP agora é {hp}|100')
            if urso <= 0:
                print('\nVocê matou o urso!')
                print('1. Voltar\n'
                    '2. Desmantelar o urso')
                acao1 = input('> ')
                if acao1 == '1':
                    direcao = floresta()
                elif acao1 == '2':
                    print('Você desmantela o urso e guarda sua pele e carne\n'
                        'Você volta pelo caminho que veio')
                    bolsa.extend(['Pele de urso', 'Carne de urso'])
                    direcao = floresta()
            if hp <= 0:
                print('Você foi morto e devorado pelo urso, se perguntando se esse foi o mesmo destino do esqueleto\n' \
                'Final (4/8)')
                inicio()
        elif acao == '2':
            print('\nVocê fugiu do combate!')
            direcao = floresta()
            return

    print('\nVocê matou o urso!')
    print('1. Voltar\n'
          '2. Desmantelar o urso')
    acao1 = input('> ')
    if acao1 == '1':
        direcao = floresta()
    elif acao1 == '2':
        print('Você desmantela o urso e guarda sua pele e carne\n'
              'Você volta pelo caminho que veio')
        bolsa.extend(['Pele de urso', 'Carne de urso'])
        direcao = floresta()

def luta2():
    urso = 100
    hp = 100
    print('O animal furioso parte para cima de você')
    print('                                     \n' 
'                  \n' 
'						                 \n'
'						                      \n'
'			                                 \n'
'	   ( )      _-                            \n'
'	 _(|  )- - _ )                             \n' 
'     __- ( |          \                              \n' 
'	/             \                              \n'
'	/       o.  |o }                             \n'
'	|            \ ;                             \n'
'	   \_         __\                             \n'
'              \'-_    \.//                           \n'
'	         / ----                              \n'
'	        /                                      \n'
'          _                                    \n'
'	  _-                                   \n'
'								  \n'
'        \n')

    while urso > 0 and hp > 0:
        print(f'\nUrso\nHP: {urso}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if acao == '1':
            danoU = random.randrange(10, 51)
            dano = 20
            urso -= dano
            hp -= danoU
            print(f'\nVocê atacou o urso e causou {dano} de dano!')
            print(f'O urso te atacou e causou {danoU}')
            print(f'Seu HP agora é {hp}|100')
            if urso <= 0:
                    print('\nVocê matou o urso!')
                    print('1. Voltar\n'
                    '2. Desmantelar o urso')
                    acao1 = input('> ')
                    if acao1 == '1':
                        direcao = floresta()
                    elif acao1 == '2':
                        print('Você desmantela o urso e guarda sua pele e carne\n'
                        'Você volta pelo caminho que veio')
                        bolsa.extend(['Pele de urso', 'Carne de urso'])
                        direcao = floresta()
            if hp <= 0:
                print('Você foi morto e devorado pelo urso, se perguntando se esse foi o mesmo destino do esqueleto\n' \
                'Final (4/8)')
                inicio()
        elif acao == '2':
            print('\nVocê fugiu do combate!')
            direcao = floresta()
            return

    print('\nVocê matou o urso!')
    print('1. Voltar\n'
          '2. Desmantelar o urso')
    acao1 = input('> ')
    if acao1 == '1':
        direcao = floresta()
    elif acao1 == '2':
        print('Você desmantela o urso e guarda sua pele e carne\n'
              'Você volta pelo caminho que veio')
        bolsa.extend(['Pele de urso', 'Carne de urso'])
        direcao = floresta()

def mumia():
    hpM = 100
    hp = 100
    while hpM > 0 and hp > 0:
        print(f'\nMorto-Vivo\nHP: {hpM}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoM = random.randrange(10,26)
                dano = 20
                hp -= danoM
                try:    
                    luzE         
                    if luzE == 30:
                        danoT = (dano+luzE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Morto-Vivo e causou {danoT} de dano!')
                        print(f'O Morto-Vivo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Morto-Vivo e causou {dano} de dano!')
                        print(f'O Morto-Vivo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpM -= dano
                    print(f'\nVocê atacou o Morto-Vivo e causou {dano} de dano!')
                    print(f'O Morto-Vivo te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                leste2()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    luzE         
                    if luzE == 30:
                        dano = 20
                        danoT = (dano+luzE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Morto-Vivo e causou {danoT} de dano!')
                        print(f'O Morto-Vivo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Morto-Vivo e causou {dano} de dano!')
                        print(f'O Morto-Vivo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 10
                    hpM -= dano
                    print(f'\nVocê atacou o Morto-Vivo e causou {dano} de dano!')
                    print(f'O Morto-Vivo te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                leste2()
    print('Você matou o Morto-vivo')
    ruinas()
    global morto_vivo
    morto_vivo = 1

def fada():
    print('Uma fada aparece (ela não toma ataques físicos, apenas de atributo)')
    hpF = 100
    hp = 100
    while hpF > 0 and hp > 0:
        print(f'\nFada\nHP: {hpF}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoF = random.randrange(5,31)
                dano = 0
                hp -= danoF
                try:    
                    escuridaoE         
                    if escuridaoE == 30:
                        danoT = (dano+escuridaoE)*2
                        hpF -= danoT
                        print(f'\nVocê atacou a Fada e causou {danoT} de dano!')
                        print(f'A Fada te atacou e causou {danoF}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpF -= dano
                        print(f'\nVocê atacou a Fada e causou {dano} de dano!')
                        print(f'A Fada te atacou e causou {danoF}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpF <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpF -= dano
                    print(f'\nVocê atacou a Fada e causou {dano} de dano!')
                    print(f'A Fada te atacou e causou {danoF}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpF <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    escuridaoE       
                    if escuridaoE == 30:
                        dano = 0
                        danoT = (dano+escuridaoE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou a Fada e causou {danoT} de dano!')
                        print(f'A Fada te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou a Fada e causou {dano} de dano!')
                        print(f'A Fada te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 0
                    hpM -= dano
                    print(f'\nVocê atacou a Fada e causou {dano} de dano!')
                    print(f'A Fada te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou a Fada')
    Labirinto()

def fantasma():
    print('Um fantama aparece (ele não toma ataques físicos, apenas de atributo)')
    hpF = 100
    hp = 100
    while hpF > 0 and hp > 0:
        print(f'\nFantasma\nHP: {hpF}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoF = random.randrange(5,31)
                dano = 0
                hp -= danoF
                try:    
                    luzE         
                    if luzE == 30:
                        danoT = (dano+luzE)*2
                        hpF -= danoT
                        print(f'\nVocê atacou o Fantasma e causou {danoT} de dano!')
                        print(f'O Fantasma te atacou e causou {danoF}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpF -= dano
                        print(f'\nVocê atacou o Fantasma e causou {dano} de dano!')
                        print(f'O Fantasma te atacou e causou {danoF}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpF <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpF -= dano
                    print(f'\nVocê atacou o Fantasma e causou {dano} de dano!')
                    print(f'O Fantasma te atacou e causou {danoF}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpF <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    luzE       
                    if luzE == 30:
                        dano = 0
                        danoT = (dano+luzE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Fantasma e causou {danoT} de dano!')
                        print(f'O Fantasma te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Fantasma e causou {dano} de dano!')
                        print(f'O Fantasma te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 0
                    hpM -= dano
                    print(f'\nVocê atacou o Fantasma e causou {dano} de dano!')
                    print(f'O Fantasma te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou o Fantasma')
    Labirinto()

def slimeF():
    hpM = 100
    hp = 100
    while hpM > 0 and hp > 0:
        print(f'\nSlime de Fogo\nHP: {hpM}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoM = random.randrange(10,26)
                dano = 20
                hp -= danoM
                try:    
                    aguaE         
                    if aguaE == 30:
                        danoT = (dano+aguaE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de fogo e causou {danoT} de dano!')
                        print(f'O Slime de fogo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de fogo e causou {dano} de dano!')
                        print(f'O Slime de fogo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            Labirinto()
                except NameError:
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de fogo e causou {dano} de dano!')
                    print(f'O Slime de fogo te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    aguaE        
                    if aguaE == 30:
                        dano = 20
                        danoT = (dano+aguaE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de fogo e causou {danoT} de dano!')
                        print(f'O Slime de fogo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de fogo e causou {dano} de dano!')
                        print(f'O Slime de fogo te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 10
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de fogo e causou {dano} de dano!')
                    print(f'O Slime de fogo te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou o Slime de fogo')
    Labirinto()

def slimeA():
    hpM = 100
    hp = 100
    while hpM > 0 and hp > 0:
        print(f'\nSlime de Água\nHP: {hpM}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoM = random.randrange(10,26)
                dano = 20
                hp -= danoM
                try:    
                    terraE         
                    if terraE== 30:
                        danoT = (dano+terraE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Água e causou {danoT} de dano!')
                        print(f'O Slime de Água te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Água e causou {dano} de dano!')
                        print(f'O Slime de Águao te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Água e causou {dano} de dano!')
                    print(f'O Slime de Água te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    terraE        
                    if terraE == 30:
                        dano = 20
                        danoT = (dano+terraE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Água e causou {danoT} de dano!')
                        print(f'O Slime de Água te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Água e causou {dano} de dano!')
                        print(f'O Slime de Água te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 10
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Água e causou {dano} de dano!')
                    print(f'O Slime de Água te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou o Slime de Água')
    Labirinto()

def slimeT():
    hpM = 100
    hp = 100
    while hpM > 0 and hp > 0:
        print(f'\nSlime de Terra\nHP: {hpM}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoM = random.randrange(10,26)
                dano = 20
                hp -= danoM
                try:    
                    arE        
                    if arE == 30:
                        danoT = (dano+arE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Terra e causou {danoT} de dano!')
                        print(f'O Slime de Terra te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Terra e causou {dano} de dano!')
                        print(f'O Slime de Terra te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Terra e causou {dano} de dano!')
                    print(f'O Slime de Terra te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    arE        
                    if arE == 30:
                        dano = 20
                        danoT = (dano+arE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Terra e causou {danoT} de dano!')
                        print(f'O Slime de Terra te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Terra e causou {dano} de dano!')
                        print(f'O Slime de Terra te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 10
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Terra e causou {dano} de dano!')
                    print(f'O Slime de Terra te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou o Slime de Terra')
    Labirinto()

def slimeAr():
    print('Um slime de Ar aparece')
    hpM = 100
    hp = 100
    while hpM > 0 and hp > 0:
        print(f'\nSlime de Ar\nHP: {hpM}|100 MP: 0|0')
        print('1. Atacar')
        print('2. Fugir')

        acao = input('> ')
        if 'Espada' in bolsa:
            if acao == '1':
                danoM = random.randrange(10,26)
                dano = 20
                hp -= danoM
                try:    
                    fogoE         
                    if fogoE == 30:
                        danoT = (dano+fogoE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Ar e causou {danoT} de dano!')
                        print(f'O Slime de Ar te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Ar e causou {dano} de dano!')
                        print(f'O Slime de Ar te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Ar e causou {dano} de dano!')
                    print(f'O Slime de Ar te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
        else:
            if acao == '1':
                danoM = random.randrange(10,26)
                hp -= danoM
                try:    
                    fogoE       
                    if fogoE == 30:
                        dano = 20
                        danoT = (dano+fogoE)*2
                        hpM -= danoT
                        print(f'\nVocê atacou o Slime de Ar e causou {danoT} de dano!')
                        print(f'O Slime de Ar te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                    else:
                        hpM -= dano
                        print(f'\nVocê atacou o Slime de Ar e causou {dano} de dano!')
                        print(f'O Slime de Ar te atacou e causou {danoM}')
                        print(f'Seu HP agora é {hp}|100')
                        if hpM <= 0:
                            break
                        elif hp <=0:
                            print('Você morreu')
                            inicio()
                except NameError:
                    dano = 10
                    hpM -= dano
                    print(f'\nVocê atacou o Slime de Ar e causou {dano} de dano!')
                    print(f'O Slime de Ar te atacou e causou {danoM}')
                    print(f'Seu HP agora é {hp}|100')
                    if hpM <= 0:
                        
                        break
                    
                    elif hp <=0:
                        print('Você morreu')
                        inicio()
            elif acao == '2':
                print('Você fugiu')
                Labirinto()
    print('Você matou o Slime de Ar')
    Labirinto()

def norte():
    if 'Faca de ouro' in bolsa or 'Espada Mágica' or 'Armadura Mágica':
        print('Você volta para casa e vende os itens que conseguiu, ficando muito rico e vivendo uma vida feliz\n' \
        'Final (2/8)')
    elif 'Cogumelos Perfeitos' in bolsa:
        print('Você volta pra casa e usa os Cogumelos Perfeitos para fazer a melhor sopa de cogumelos do mundo\n' \
        'Final (3/8)')
    else:
        print('\nVocê vai para o norte e consegue achar o caminho de casa, mas se pergunta que tipo de aventuras poderia ter tido. \n'
          'Final (1/8)')
        game = inicio()

def oeste():
    print('\nVocê decide ir para oeste e encontra um grande lago\n' \
    '                                  \n'
'         ~~~~~~~~~~~~~~~~~~~~~~~~~\n'
'       (                  o         )\n'
'      (                             )\n'
'     (        ~~         ~~          )\n'
'     (                               )\n'
'     (        o                       )\n'
'     (                  ~~            )  \n'    
'     (           ~~                   )\n'
'      (                       c      )\n'
'        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
'                                     \n'
'      \n'
    '1. Voltar\n' 
    '2. Olhar o lago')
    lago = input('> ')
    if lago == '1':
        floresta()
    elif lago == '2':
        print('\nVocê decide olhar ao redor do lago\n' \
        'Andando pelas margens você acaba tropessando e derrubando sua faca no lago\n' \
        'Uma bela mulher segurando uma faca de ouro na mão direita e uma de prata na mão esquerda sai da água e diz\n' \
        '"Eu vi que você perdeu sua faca, então me diga, você derrubou a faca de ouro ou a de prata?"')
        faca = input('> ')
        if faca == 'ouro' or 'prata':
            print('\nVendo uma oportunidade de fazer dinheiro, você resolve mentir, porém a fada do lago sabe da verdade e se enche de fúria\n' \
            '"Pela sua ganância, você merece ser punido!"')
            print('A água do lago te envolve e te puxa para o fundo\n' \
            'Você morreu\n' \
            'Final (5/8)')
            game = inicio()
        elif faca == 'faca velha':
            print('\nVocê decide falar a verdade para a fada do lago e ela fica contente\n' \
            '"Muito bem, por sua honestidade lhe recompensarei com ambas as facas de ouro e prata"')
            bolsa += ['Faca de ouro, Faca de prata']
            print('Você agradece a fada e se despede')
            floresta()

def leste():
    print('\nVocê decide ir para o Leste, onde encontra algumas ruínas de um antigo templo de pedra\n' \
    '1. Voltar\n' \
    '2. Olhar o lado de fora\n' \
    '3. Olhar o lado de dentro')
    acao = input('> ')
    if acao == '1':
        direcao = floresta()
    elif acao == '2':
        acao2 = lesteF()
    elif acao == '3':
        acao3 = ruinas()

def leste2():
    print('Você está de frente para as ruínas de um antigo templo de pedra\n' \
    '1. Voltar\n' \
    '2. Olhar o lado de fora\n' \
    '3. Olhar o lado de dentro')
    acao = input('> ')
    if acao == '1':
        direcao = floresta()
    elif acao == '2':
        acao2 = lesteF()
    elif acao == '3':
        print('\nVocê decide entrar nas ruínas de pedra\n') 
        acao3 = ruinas()

def lesteF():
    print('\nVocê decide olhar o lado de fora das ruínas\n' \
        'Você encontra alguns pilares caídos circundando uma pedra com algumas inscrições\n' \
        'Ao se aproximar, você consegue ler: "O segredo está no começo"\n' \
        '1. Voltar\n' \
        '2. Continuar a olhar em volta')
    acao2 = input('> ')
    if acao2 == '1':
        acao = leste2()
    elif acao2 == 'As aventuras de você mesmo':
        if 'Espada Mágica' in bolsa or 'Cogumelos Perfeitos' in bolsa or 'Armadura Mágica' in bolsa:
            print('Boa tentativa, engraçadinho, mas não dessa vez.\n')
            lesteF()
        else:
            EE()
    elif acao2 == '2':
        print('Você não acha mais nada')
        leste2()
    else:
        print('Nada acontece')
        lesteF()

def ruinas():
    print('O lado de dentro das ruínas revela uma sala larga com um sarcófago no meio e três passagens, uma em cada paredes\n' 
    '1. Voltar\n' 
    '2. Olhar o sarcófago\n' 
    '3. Olhar a passagem da direita\n' 
    '4. Olhar a passagem do meio\n' 
    '5. Olhar a passagem da esquerda')
    acao3 = input('> ')
    if acao3 == '1':
        leste2()
    elif acao3 == '2':
        if morto_vivo >= 1:
            print('\nVocê se aproxima do sarcófago ja aberto, não há mais nada para fazer aqui\n' \
            '1. Voltar\n')
            tumba = input('> ')
            if tumba == '1':
                ruinas()
        else:
            print('\nVocê se aproxima do sarcófago no meio da sala, uma fina fumaça parece sair por sua tampa e você pode jurar que escutou um leve suspiro vindo de dentro\n' \
            '1. Voltar\n' \
            '2. Sair e nunca mais voltar\n' \
            '3. Abrir o sarcófago')
            tumba = input('> ')
            if tumba == '1':
                ruinas()
            elif tumba == '2':
                Final2()
            elif tumba == '3':
                print('\nVocê decide abrir o sarcófago, empurrando a pesada tampa de pedra revelando um cadever ressecado\n' \
    'O cadaver então avança em sua direção, se revelando um morto-vivo!')
                mumia()
    elif acao3 == '3':
        PassagemD()
    elif acao3 == '4':
        PassagemM()
    elif acao3 == '5':
        Labirinto()

def Labirinto():
    global esquerda, direita, meio
    if esquerda == 3 and direita == 3 and meio == 2:
        FinalS2()
    else:
        print('Você devide ir pela passagem da Esquerda e encontra um labirinto com três passagens\n' \
        '1. Voltar\n' \
        '2. Esquerda\n' \
        '3. Direita\n' \
        '4. Meio')
        caminho = input('> ')
        if caminho == '1':
            ruinas()
        elif caminho == '2':
            esquerda += 1
            Monstros()
        elif caminho == '3':
            direita += 1
            Monstros()
        elif caminho == '4':
            meio += 1
            Monstros()

def Final2():
    print('\nApós se assustar com as ruínas e a ideia do que poderia ter naquele sarcófago, você decide sair de lá correndo\n' \
    'Você adentra ainda mais na floresta e nunca mais é achado\n' \
    'Final (6/8)')

def PassagemD():
    print('Você decide ir pela passagem da direita e se depara com um baú\n' \
    '1. Voltar\n' \
    '2. Abrir o baú')
    acao = input('> ')
    if acao == '1':
        ruinas()
    elif acao == '2':
        print('Você decide abrir o baú, então se aproxima e toca na tampa\n' \
        'O baú então se revela um mímico e te devora por completo\n' \
        'Final (7/8)')
        inicio()

def PassagemM():
    print('Você decide seguir pelo caminho do meio e se depara com uma enorme porta, trancada por uma fechadura mágica, com apenas um pedestal no meio\n' \
    '1. Voltar\n' \
    '2. Colocar um item no pedestal')
    acao = input('> ')
    if acao == '1':
        ruinas()
    elif acao == '2':
        print('Qual item você escolhe?')
        print(bolsa)
        acao2 = input('> ')
        if acao == 'Trapos':
            print('Você decide colocar os Trapos no pedestal, surpreendentemente a porta se abre e revela inúmeros tesouros, lhe fazendo o homem mais rico de sua cidade e lhe garantindo uma vida boa\n' \
            'Final (8/8)')
        else:
            print('Nada acontece\n')
            PassagemM()

def Monstros():
    monstro = random.randrange (19, 141)
    if monstro > 20 and monstro <= 40:
        fada()
    elif monstro >40 and monstro <= 60:
        slimeF()
    elif monstro > 60 and monstro <= 80:
        slimeA()
    elif monstro > 80 and monstro <= 100:
        slimeT()
    elif monstro > 100 and monstro <= 120:
        slimeAr()
    elif monstro > 120 and monstro <= 141:
        fantasma()

def EE():
    print('\nVocê vê um clarão repentino vindo da pedra e, após sua visão se ajustar, você vê uma capivara em pose de meditação vestindo uma túnica\n'
          'A capivara então diz: "Ó mortal, por ter me invocado lhe darei o direito de escolher uma recompensa, mas para isso, você deve me dar uma oferenda!"')
    print('Surpreso por estar vendo uma capivara mágica, você começa a pensar em uma oferenda\n'
          '1. Voltar\n' 
          '2. Olhar a bolsa')
    acaoS = input('> ')
    if acaoS == '1':
        FinalS1()
    elif acaoS == '2':
        if 'Maçã' in bolsa:
            ItemBolsa2()
        else:
            print('Você não achou sua bolsa')

def atributoEspada():
    print('Escolha um atributo para sua espada mágica\n' \
    '1. Luz\n' \
    '2. Escuridão\n'
    '3. Fogo\n'
    '4. Água\n'
    '5. Ar\n'
    '6. Terra\n')
    escolher = input('> ')
    if escolher == '1':
        global luzE
        luzE = 30
    elif escolher == '2':
        global escuridaoE
        escuridaoE = 30
    elif escolher == '3':
        global fogoE
        fogoE = 30
    elif escolher == '4':
        global aguaE
        aguaE = 30
    elif escolher == '5':
        global arE
        arE = 30
    elif escolher == '6':
        global terraE
        terraE = 30
    lesteF()

def ItemBolsa2():
    print('Dentro da bolsa você têm:')
    for item in bolsa:
        print('- ', item)
    print('Você decide escolher a oferenda')
    acao = input('> ')
    if acao == 'Maçã':
        print('Você entrega a maçã que trouxe como lanche\n' \
        'A capivara mágica fica muito contente e diz:\n' \
        ' "Que bela oferenda, depois de tantos anos estou morrendo de fome, pode escolher o que deseja."\n' \
        '1. Espada Mágica\n' \
        '2. Cogumelos Perfeitos\n' \
        '4. Nada')
        acaoS1 = input('> ')
        if acaoS1 == '1':
            print('Você escolheu a Espada Mágica e, como um bônus, a capivara te deixou escolher um encantamento\n')
            bolsa.extend(['Espada Mágica'])
            atributoEspada()
        elif acaoS1 == '2':
            print('Você escolheu a Cogumelos Perfeitos, se despediu da capivara e voltou\n')
            bolsa.extend(['Cogumelos Perfeitos'])
    else:
        print('A capivara recusa sua oferenda, ache outra coisa')
        ItemBolsa2()

def FinalS1():
    print('\nDepois de pensar muito, você decide ignorar a capivara mágica, achando ser apenas uma alucinação\n' \
    'A capivara fica furiosa com sua atitude e usa seu feitiço mais poderoso em você, te transformando em um cogumelo\n' \
    'Você fica lá, sem poder se mexer e falar, mas estranhamente podendo enxergar, passam-se dias, semanas, meses e anos, porém você continua lá\n' \
    'Completamente sozinho.\n' \
    'Final secreto (1/2)')

def FinalS2():
    print('\nApós muito tempo tentando, você finalmente chega ao final do labirinto\n' \
    'Lá, você encontra uma bela casa no meio de um campo com um pomar a sua direita e um jardim logo à frente\n' \
    'Se encantando pelo ambiente, você decide morar lá, até porque você não sabe como sair.\n' \
    'Final secreto (2/2)\n')
    inicio()

inicio()