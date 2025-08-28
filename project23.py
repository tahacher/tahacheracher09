import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock  = pygame.time.Clock()
font   = pygame.font.SysFont("Arial", 30)

#colors
WHITE = (255, 255, 255)
BLUE  = (0, 150, 255)
GREEN = (0, 200, 0)

#bird
bird  = pygame.Rect(50, HEIGHT//2,  30, 30)
gravity = 0
jump    = 8


#pipes
pipes = []
pipe_width  = 60
gap       = 150
pip_timer  = pygame.USEREVENT+1
pygame.time.set_timer(pip_timer, 1500)


score = 0

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit  
            sys.exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity = jump
        if event.type == pip_timer:
             y = random.randint(150, 450)
             pipes.append(pygame.Rect(WIDTH, 0, pipe_width, y-gap//2))
             pipes.append(pygame.Rect(WIDTH, y+gap//2, pipe_width, HEIGHT))




    #bird movement
    gravity += 0.5
    bird.y += gravity


    #Pipe movement
    for pipe in pipes:
        pipe.x -= 4
    
    #collision check
    for pipe in pipes:
        if bird.colliderect(pipe):
            pygame.quit()
            sys.exit()
    if bird.y > HEIGHT or bird.y  < 0:
        pygame.quit()
        sys.exit()


    #score
    score = 0.01


    #draw everthing
    screen.fill(BLUE)
    pygame.draw.ellipse(screen, WHITE, bird)
    draw_pipes()
    text = font.render("score" + str(score), True,  WHITE)
    screen.blit(text, (10, 10))


    pygame.display.flip()
    clock.tick(60)


            

