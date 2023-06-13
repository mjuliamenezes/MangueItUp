import pygame, sys, csv
from config import *
from ganhou import *

clock = pygame.time.Clock()

def exibir_ranking(tela1):
    try:
        state = RANKING
        ranking = []
        with open('ranking.csv', 'r', encoding='utf8') as arquivo:
            linhas = arquivo.readlines()
            pontuacoes=[]
            for linha in linhas:
                linha = linha.strip().split('-')
                valor = float(linha[1])
                ranking.append(valor)  
            ranking.sort(reverse=True)
        
            for i, v in enumerate(ranking):
                if i < 5: 
                    if i == 0:
                        ranking_texto1 = fontMedia.render(f"1. Pontuação: {v}", True, esquerda)
                    if i == 1:
                        ranking_texto2 = fontMedia.render(f"2. Pontuação: {v}", True, esquerda)
                    if i == 2:
                        ranking_texto3 = fontMedia.render(f"3. Pontuação: {v}", True, esquerda)
                    if i == 3:
                        ranking_texto4 = fontMedia.render(f"4. Pontuação: {v}", True, esquerda)
                    if i == 4:
                        ranking_texto5 = fontMedia.render(f"5. Pontuação: {v}", True, esquerda)


        while state == RANKING:
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
                            state = INIT

            bgranking = pygame.image.load('imagens/Ranking.png')
            tela1.blit(bgranking, (0,0))
            tela1.blit(ranking_texto1,(640, 300))
            tela1.blit(ranking_texto2,(640,420))
            tela1.blit(ranking_texto3,(640,540))
            tela1.blit(ranking_texto4,(640,660))
            tela1.blit(ranking_texto5,(640,780))

            pygame.display.flip()
            pygame.display.update()

        return state

    except FileNotFoundError:
        print("Ranking: Arquivo Não Encontrado")
    except Exception as e:
            print("Erro no Ranking:", str(e))