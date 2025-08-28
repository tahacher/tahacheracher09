import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("🏓 Pong")

WHITE = (255, 255, 255)

# Paddles and ball
paddle1 = pygame.Rect(30, HEIGHT//2-60, 10, 120)
paddle2 = pygame.Rect(WIDTH-40, HEIGHT//2-60, 10, 120)
ball = pygame.Rect(WIDTH//2-10, HEIGHT//2-10, 20, 20)
ball_speed = [5, 5]
ball_active = False   # ✅ ball won’t move until SPACE pressed

score1, score2 = 0, 0
font = pygame.font.SysFont("Arial", 40)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                ball_active = True   # ✅ start ball when SPACE pressed

    keys = pygame.key.get_pressed()
    # Player 1 (W/S)
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 6
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 6
    # Player 2 (Up/Down)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 6
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 6

    # Ball movement
    if ball_active:
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]
    else:
        # Reset ball to center until game starts
        ball.center = (WIDTH//2, HEIGHT//2)

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball_active = False
        ball_speed = [5, 5]
    if ball.right >= WIDTH:
        score1 += 1
        ball_active = False
        ball_speed = [-5, 5]

    # Draw
    screen.fill((0,0,0))
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2,0), (WIDTH//2,HEIGHT))

    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    screen.blit(score_text, (WIDTH//2-40, 20))

    if not ball_active:
        msg = font.render("Press SPACE to start", True, WHITE)
        screen.blit(msg, (WIDTH//2-150, HEIGHT//2+50))

    pygame.display.flip()
    clock.tick(60)
