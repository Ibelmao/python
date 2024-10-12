import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

def desenha_grade(screen, screen_size):
    pos_y = screen_size[1] / 3
    pygame.draw.line(screen, (0, 255, 0), (0, pos_y), (screen_size[0], pos_y), 5)
    pygame.draw.line(screen, (0, 255, 0), (0, 2 * pos_y), (screen_size[0], 2 * pos_y), 5)
    
    pos_x = screen_size[0] / 3
    pygame.draw.line(screen, (255, 0, 0), (pos_x, 0), (pos_x, screen_size[1]), 5)
    pygame.draw.line(screen, (255, 0, 0), (2 * pos_x, 0), (2 * pos_x, screen_size[1]), 5)

class Bola(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        fonte = pygame.font.Font(None, 100)
        texto = fonte.render('O', True, (0, 0, 0))
        retangulo_texto = texto.get_rect(center=(x, y))
        self.surf = texto
        self.rect = retangulo_texto

class Xis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        fonte = pygame.font.Font(None, 100)
        texto = fonte.render('X', True, (0, 0, 0))
        retangulo_texto = texto.get_rect(center=(x, y))
        self.surf = texto
        self.rect = retangulo_texto

def checa_vitoria(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]
    return None

def checa_empate(tabuleiro):
    for row in tabuleiro:
        if "" in row:
            return False  # Ainda há espaços vazios, não é empate
    return True  # Nenhum espaço vazio e ninguém ganhou, é empate

def mostra_mensagem(screen, mensagem):
    fonte = pygame.font.Font(None, 80)
    texto = fonte.render(mensagem, True, (0, 0, 0))
    rect = texto.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
    screen.blit(texto, rect)
    pygame.display.update()
    pygame.time.wait(2000)

def jogar_novamente():
    fonte = pygame.font.Font(None, 50)
    mensagem = "Jogar novamente? (S/N)"
    screen.fill((255, 255, 255))
    texto = fonte.render(mensagem, True, (0, 0, 0))
    rect = texto.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
    screen.blit(texto, rect)
    pygame.display.update()

    esperando_resposta = True
    while esperando_resposta:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return True  # Reiniciar o jogo
                elif event.key == pygame.K_n:
                    return False  # Fechar o jogo

######## MAIN ############

SCREEN_SIZE = (640, 480)
WIDTH_SIZE = SCREEN_SIZE[0] / 3
HEIGHT_SIZE = SCREEN_SIZE[1] / 3
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Jogo da Velha")
loop = True

while loop:
    # Inicializa o tabuleiro e o estado do jogo
    figuras = []
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    vez = "X"
    game_over = False

    while not game_over:
        screen.fill((255, 255, 255))
        desenha_grade(screen, SCREEN_SIZE)

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                loop = False
            elif event.type == MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                x, y = pos
                pos_quadrante_x = int(x // WIDTH_SIZE)
                pos_quadrante_y = int(y // HEIGHT_SIZE)

                if tabuleiro[pos_quadrante_y][pos_quadrante_x] == "":
                    largura_retangulo = WIDTH_SIZE
                    altura_retangulo = HEIGHT_SIZE

                    if vez == "X":
                        figura = Xis(
                            int(pos_quadrante_x * largura_retangulo + largura_retangulo // 2),
                            int(pos_quadrante_y * altura_retangulo + altura_retangulo // 2)
                        )
                        tabuleiro[pos_quadrante_y][pos_quadrante_x] = "X"
                        vez = "O"
                    else:
                        figura = Bola(
                            int(pos_quadrante_x * largura_retangulo + largura_retangulo // 2),
                            int(pos_quadrante_y * altura_retangulo + altura_retangulo // 2)
                        )
                        tabuleiro[pos_quadrante_y][pos_quadrante_x] = "O"
                        vez = "X"

                    figuras.append(figura)

                    # Verificar se há um vencedor
                    vencedor = checa_vitoria(tabuleiro)
                    if vencedor:
                        mostra_mensagem(screen, f"Jogador {vencedor} venceu!")
                        game_over = True

                    # Verificar se houve empate
                    if not vencedor and checa_empate(tabuleiro):
                        mostra_mensagem(screen, "Empate!")
                        game_over = True

        # Desenhar as figuras no tabuleiro
        for figura in figuras:
            screen.blit(figura.surf, figura.rect)

        pygame.display.update()

    # Perguntar se deseja jogar novamente
    if game_over:
        loop = jogar_novamente()

pygame.quit()
