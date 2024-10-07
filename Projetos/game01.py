import pygame
pygame.init()

def desenha_grade(screen, screen_size):
    # LINHAS HORIZONTAIS
    pos_y = screen_size[1] / 3
    pygame.draw.line(
        surface=screen, 
        color=(0, 255, 0), 
        start_pos=(0, pos_y),
        end_pos=(screen_size[0], pos_y),
        width=5,
    )
    pygame.draw.line(
        surface=screen, 
        color=(0, 255, 0), 
        start_pos=(0, pos_y * 2),
        end_pos=(screen_size[0], pos_y * 2),
        width=5,
    )
    # LINHAS VERTICAIS
    pos_x = screen_size[0] / 3
    pygame.draw.line(
        surface=screen,
        color=(255, 0, 0),
        start_pos=(pos_x, 0),
        end_pos=(pos_x, screen_size[1]),
        width=5,
    )
    pygame.draw.line(
        surface=screen,
        color=(255, 0, 0),
        start_pos=(2 * pos_x, 0),
        end_pos=(2 * pos_x, screen_size[1]),
        width=5,
    )

class Bola(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        fonte = pygame.font.Font(None, 100)
        texto = fonte.render('O', True, (0, 0, 0))
        retangulo_texto = texto.get_rect(
            center=(x, y)
        )
        self.surf = texto
        self.rect = retangulo_texto

class Xis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        fonte = pygame.font.Font(None, 100)
        texto = fonte.render('X', True, (0, 0, 0))
        retangulo_texto = texto.get_rect(
            center=(x, y)
        )
        self.surf = texto
        self.rect = retangulo_texto

def checa_vitoria(tabuleiro):
    # Verifica linhas, colunas e diagonais
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

######## MAIN ############

SCREEN_SIZE = (640, 480)
WIDTH_SIZE = SCREEN_SIZE[0] / 3
HEIGHT_SIZE = SCREEN_SIZE[1] / 3
screen = pygame.display.set_mode(SCREEN_SIZE)
loop = True
figuras = []

# Cria a matriz do tabuleiro (3x3)
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
vez = "X"  # Controla de quem é a vez

while loop:
    # Adiciona a cor de fundo
    screen.fill((255, 255, 255))
    desenha_grade(screen, SCREEN_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos
            pos_quadrante_x = int(x // WIDTH_SIZE)
            pos_quadrante_y = int(y // HEIGHT_SIZE)

            # Verifica se a célula já foi ocupada
            if tabuleiro[pos_quadrante_y][pos_quadrante_x] == "":
                largura_retangulo = WIDTH_SIZE
                altura_retangulo = HEIGHT_SIZE

                if vez == "X":
                    figura = Xis(
                        int(pos_quadrante_x * largura_retangulo + largura_retangulo // 2),
                        int(pos_quadrante_y * altura_retangulo + altura_retangulo // 2)
                    )
                    tabuleiro[pos_quadrante_y][pos_quadrante_x] = "X"
                    vez = "O"  # Alterna a vez
                else:
                    figura = Bola(
                        int(pos_quadrante_x * largura_retangulo + largura_retangulo // 2),
                        int(pos_quadrante_y * altura_retangulo + altura_retangulo // 2)
                    )
                    tabuleiro[pos_quadrante_y][pos_quadrante_x] = "O"
                    vez = "X"  # Alterna a vez

                figuras.append(figura)

                # Checa se há um vencedor
                vencedor = checa_vitoria(tabuleiro)
                if vencedor:
                    print(f"Jogador {vencedor} venceu!")
                    loop = False

    # Desenha as figuras no tabuleiro
    for figura in figuras:
        screen.blit(figura.surf, figura.rect)

    # Atualiza a tela
    pygame.display.update()

pygame.quit()
