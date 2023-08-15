import pygame
import sys

# Инициализация pygame
pygame.init()

# Размеры окна
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 480

# Цвета
WHITE = (230, 230, 230)
BLACK = (0, 0, 0)

# Размеры и скорость платформы
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 150
PADDLE_SPEED = 20

# Размеры и скорость мячика
BALL_WIDTH, BALL_HEIGHT = 20, 20
BALL_SPEED_X, BALL_SPEED_Y = 3, 6

# Функция для обновления экрана
def update_screen():
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, opponent_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    pygame.draw.aaline(window, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
    pygame.display.update()

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('my Ping-Pong')

# Создание платформ
player_paddle = pygame.Rect(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Создание мячика
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_WIDTH // 2, WINDOW_HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
ball_speed_x, ball_speed_y = BALL_SPEED_X, BALL_SPEED_Y

# Главный цикл игры
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        player_paddle.y += PADDLE_SPEED

    # Обновление положения мячика
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Проверка столкновения мячика с краями окна
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Проверка столкновения мячика с платформами
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    # Обновление экрана
    update_screen()

    # Ограничение частоты обновления экрана
    clock.tick(60)
