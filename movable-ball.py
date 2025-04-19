import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")
clock = pygame.time.Clock()#این رو چون کد کار نمی کردن از هوش مصنوعی پرسید

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Ball:
    def __init__(self):
        self.radius = 30
        self.x = 400
        self.y = 300
        self.color = WHITE
        self.speed = 10

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= WIDTH - self.radius:
            self.x = new_x
        if self.radius <= new_y <= HEIGHT - self.radius:
            self.y = new_y

    def toggle_speed(self):
        self.speed = 20 if self.speed == 10 else 10

    def set_color(self, color):
        self.color = color

ball = Ball()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ball.set_color(RED)
            elif event.key == pygame.K_g:
                ball.set_color(GREEN)
            elif event.key == pygame.K_s:
                ball.toggle_speed()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball.move(-ball.speed, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(ball.speed, 0)
    if keys[pygame.K_UP]:
        ball.move(0, -ball.speed)
    if keys[pygame.K_DOWN]:
        ball.move(0, ball.speed)

    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
