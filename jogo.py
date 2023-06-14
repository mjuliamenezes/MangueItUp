# Importando bibliotecas 
import pygame
import random
from sprites import *
from config import *  
from selecao_musica import cardapio

def game(window):
    lista = cardapio(window)

    # Condições 
    game = True
    inicio = True

    # Variáveis 
    player_data = {
        'combo' : 0,
        'acertos' : 0,
        'erros' : 0, 
        'notas' : 0
    }
    combo = 0
    clock = pygame.time.Clock()

    # Janela
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mangue It Up')
    window.fill((0,0,0))


    dados_teclas = {
        'esquerda' : [esquerda, (735, 225), pygame.K_LEFT],
        'cima' :[cima,(885, 225), pygame.K_UP],
        'baixo' : [baixo,(1035, 225), pygame.K_DOWN],
        'direita' : [direita,(1185, 225), pygame.K_RIGHT],
    }
  
    # Dicionários 
            # Dados das Teclas 

    assets = {
        'notas' : {
            'esquerda' : pygame.image.load('assets/setas/seta_esquerda.png').convert_alpha(),
            'cima' : pygame.image.load('assets/setas/seta_cima.png').convert_alpha(),
            'baixo' : pygame.image.load('assets/setas/seta_baixo.png').convert_alpha(),
            'direita' : pygame.image.load('assets/setas/seta_direita.png').convert_alpha(),
        },
    }

    todas_as_notas = pygame.sprite.Group()
    
    # Inicializando as sprites

    atual = 'esquerda'
    mensagem = True
    nota = Notes(atual, assets, dados_teclas)
    tecla = Teclas(atual, window, dados_teclas)
    tempo = 0
    segundo = 0
    ta = 0
    state = GAME
    
    pygame.mixer.init()

    # Estrutura para tocar música 
    pygame.mixer.music.load(lista[1])                    #Carrega a música
    pygame.mixer.music.set_volume(1)                     #o volume vai de 0 a 1

    # Fonte para textos
    while state == GAME:
        
        cenario = pygame.image.load('imagens/musica_inicio.png')

        if inicio == False: 
            clock.tick(fps)
            segundo = segundo % fps
            if segundo == 0:
                tempo += 1 
            segundo += 1
            
            if tempo != ta:
                ta+=1
                nota = Notes(random.choice(['esquerda', 'cima','baixo','direita']),assets, dados_teclas)
                nota.speed_y = nota.speed_y + (lista[2])
                todas_as_notas.add(nota)
                player_data['notas'] +=1 

        else:
            tecla_start = fontMedia.render("Aperte uma tecla para começar!", True,  (255,255,255)) 

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dados_teclas['esquerda'][0] = branco
                    esqpress = nota.nome == 'esquerda'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and esqpress:
                        player_data['acertos']+=1
                        nota.remove()
                        player_data['combo']+=1
                        mensagem = True
                    else:
                        player_data['erros'] +=1
                        mensagem = False
                        if combo>player_data['combo']:
                            player_data['combo'] = combo
                
                if event.key == pygame.K_UP:
                    dados_teclas['cima'][0] = branco
                    cimapress = nota.nome == 'cima'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and cimapress:
                        player_data['acertos']+=1
                        nota.remove()
                        player_data['combo']+=1
                        mensagem = True
                    else:
                        player_data['erros'] +=1
                        mensagem = False
                        if combo>player_data['combo']:
                            player_data['combo'] = combo
                
                if event.key == pygame.K_DOWN:
                    dados_teclas['baixo'][0] = branco
                    baixopress = nota.nome == 'baixo'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and baixopress:
                        player_data['acertos'] += 1
                        nota.remove()
                        player_data['combo']+=1
                        mensagem = True
                    else:
                        player_data['erros'] +=1
                        mensagem = False
                        if combo>player_data['combo']:
                            player_data['combo'] = combo

                if event.key == pygame.K_RIGHT:
                    dados_teclas['direita'][0] = branco
                    dirpress = nota.nome == 'direita'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and dirpress:
                        player_data['acertos'] +=1
                        nota.remove()
                        player_data['combo']+=1
                        mensagem = True                    
                    else:
                        player_data['erros'] +=1
                        mensagem = False
                        if combo>player_data['combo']:
                            player_data['combo'] = combo

            if event.type == pygame.KEYUP:
                if inicio:
                    inicio = False
                    pygame.mixer.music.play()

                if event.key == pygame.K_ESCAPE:
                    exit()

                if tempo >= dicio[lista[1]]:
                    pygame.mixer.music.stop()
                    state = GANHOU

                if event.key == pygame.K_LEFT:
                    dados_teclas['esquerda'][0] = esquerda
                    esqpress = False

                if event.key == pygame.K_UP:
                    dados_teclas['cima'][0] = cima
                    cimapress = False

                if event.key == pygame.K_DOWN:
                    dados_teclas['baixo'][0] = baixo
                    baixopress = False   

                if event.key == pygame.K_RIGHT:
                    dados_teclas['direita'][0] = direita
                    dirpress = False
        
        if nota.rect.y - 60 == y_teclas-2*tecla.radius+2:
            player_data['erros']+=1
        
        mensagem_acerto = fontMedia.render("ARRETADO!", True, branco)
        mensagem_erro = fontMedia.render("VIXE!", True, branco) 
        if player_data['acertos'] < 10:
            ponto_combo = fontPequena.render(f"0{str(player_data['acertos'])}", True, branco)
        else: 
            ponto_combo = fontPequena.render(f"{str(player_data['acertos'])}", True, branco)

        window.blit(cenario,(0,0))
        window.blit(nota.image, nota.rect)
        window.blit(ponto_combo, (945,870))

        if mensagem == True and player_data['acertos']!=0:
            window.blit(mensagem_acerto, (820,170))
        elif mensagem == False:
            window.blit(mensagem_erro, (860,170))
            

        todas_as_notas.update()
        if inicio:
            window.blit(tecla_start,(width/3.25,height/2))  
        
        lista_para_return = [state, player_data]

        pygame.display.update()

        
    return lista_para_return