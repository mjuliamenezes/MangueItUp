import pygame, sys
from config import * 

pygame.init()

bg = pygame.image.load('imagens/score.png')

def ganhou_function(tela1, resultado, jogador): 
    try:
        porcentagem_acertos = (resultado[1]['acertos']/resultado[1]['notas'])*100

        valor = '{0:.1f}'.format(porcentagem_acertos)
        valor = str(valor)
        texto_acertos = fontGrande.render(valor + '%',True,esquerda)

        arquivo = open('ranking.csv', 'a', encoding='utf8')
        arquivo.write(jogador + '-' + valor + '\n')
        arquivo.close()

        state = GANHOU
        clock = pygame.time.Clock()
        while state == GANHOU:
            clock.tick(fps)  
            tela1.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = QUIT
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        state = RANKING

            tela1.blit(bg, (0,0))

            tela1.blit(texto_acertos,(840,615))

            pygame.display.flip()
            pygame.display.update()

        return state

    except FileNotFoundError:
        print("Pontuação: Arquivo Não Encontrado")
    except Exception as e:
            print("Erro na Pontuação:", str(e))