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
    pos_x = screen_size[0] / 3 # 640/3
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

######## MAIN ############

SCREEN_SIZE = (640, 480)
WIDTH_SIZE = SCREEN_SIZE[0] / 3
HEIGHT_SIZE = SCREEN_SIZE[1] / 3
screen = pygame.display.set_mode(SCREEN_SIZE)
loop = True
figuras = []

while loop:
    # ADICIONO A COR NO FORMATO RGB (RED, GREEN, BLUE)
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

            largura_retangulo = WIDTH_SIZE
            altura_retangulo = HEIGHT_SIZE

            xis = Xis(
                int(pos_quadrante_x * largura_retangulo + largura_retangulo // 2),
                int(pos_quadrante_y * altura_retangulo + altura_retangulo // 2)
            )
            figuras.append(xis)

    for figura in figuras:
        screen.blit(
            figura.surf,
            figura.rect,
        )
    # largura_retangulo = WIDTH_SIZE
    # altura_retangulo = HEIGHT_SIZE
    # xis = Xis(largura_retangulo // 2, altura_retangulo // 2)
    # screen.blit(
    #     xis.surf,
    #     xis.rect,
    # )
    # bola = Bola(largura_retangulo + largura_retangulo // 2, altura_retangulo // 2)
    # screen.blit(
    #     bola.surf,
    #     bola.rect,
    # )
    # xis = Xis(2 * largura_retangulo + largura_retangulo // 2, altura_retangulo // 2)
    # screen.blit(
    #     xis.surf,
    #     xis.rect,
    # )

    # ATUALIZA TELA
    pygame.display.update()