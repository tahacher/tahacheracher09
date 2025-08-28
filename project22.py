import pygame, sys

pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Paddle
paddle = pygame.Rect(WIDTH//2-50, HEIGHT-30, 100, 10)

# Ball
ball = pygame.Rect(WIDTH//2, HEIGHT-45, 15, 15)
ball_speed = [4, -4]
ball_active = False   # ✅ Ball waits until space is pressed

# Bricks
bricks = [pygame.Rect(x*50+5, y*20+5, 40, 10) for x in range(10) for y in range(5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_active = True   # ✅ Start the ball when SPACE pressed

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(6, 0)

    # Ball movement
    if ball_active:
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]
    else:
        # Stick ball to paddle before launch
        ball.centerx = paddle.centerx
        ball.bottom = paddle.top - 1

    # Collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)

    if ball.bottom >= HEIGHT:
        ball_active = False   # Ball lost → reset to paddle

    # Draw everything
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)
