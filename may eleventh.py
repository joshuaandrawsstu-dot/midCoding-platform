import pgzrun
WIDTH = 800
HEIGHT = 500

TITLE = "Football Game"

player = Rect((100, 400), (40, 40))

velocity_y = 0
gravity = 1
jump_strength = -15
speed = 5

on_ground = False
score = 0
game_won = False
game_over = False
def draw():
    screen.clear()
    screen.fill("Green")
    screen.draw.filled_rect(player, "blue")
for platform in platforms:
    screen.draw.filled_rect(platform, "red")
def update():
    global velocity_y

    if keyboard.left:
        player.x -= speed

    if keyboard.right:
        player.x += speed
if player.left < 0:
    player.left = 0

if player.right > WIDTH:
    player.right = WIDTH
velocity_y += gravity
player.y += velocity_y
check_platform_collision()
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((150, 390), (120, 20)),
    Rect((350, 320), (120, 20)),
    Rect((550, 250), (120, 20)),
    Rect((250, 180), (120, 20))
]
def check_platform_collision():
    global velocity_y, on_ground

    on_ground = False

    for platform in platforms:
        if player.colliderect(platform) and velocity_y >= 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True