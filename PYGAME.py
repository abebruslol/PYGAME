import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

BLACK = (0,0,0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)


FPS = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мишень")

xcor = WIDTH/2
ycor = HEIGHT/2

run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run_game = False
            elif event.key == pygame.K_w:
                ycor -= 10
            elif event.key == pygame.K_s:
                ycor += 10
            elif event.key == pygame.K_a:
                xcor -= 10
            elif event.key == pygame.K_d:
                xcor += 10
            
        
    clock.tick(FPS)
    screen.fill(WHITE)
    #pygame.draw.rect(screen, RED ,(WIDTH/2-75,HEIGHT/2-75,150,150))
    pygame.draw.circle(screen, BLACK ,(WIDTH/2,HEIGHT/2),160)
    pygame.draw.circle(screen, WHITE ,(WIDTH/2,HEIGHT/2),140)
    pygame.draw.circle(screen, BLACK ,(WIDTH/2,HEIGHT/2),120)
    pygame.draw.circle(screen, WHITE ,(WIDTH/2,HEIGHT/2),100)
    pygame.draw.circle(screen, BLACK ,(WIDTH/2,HEIGHT/2),80)
    pygame.draw.circle(screen, WHITE ,(WIDTH/2,HEIGHT/2),60)
    pygame.draw.circle(screen, RED ,(WIDTH/2,HEIGHT/2),40)
    pygame.draw.circle(screen, GREEN ,(xcor,ycor),40)
    pygame.display.flip()

pygame.quit()