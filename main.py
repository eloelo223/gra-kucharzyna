import pygame
import random

# rozpocznij program
pygame.init()

score = 0


# ekran gry
screen = pygame.display.set_mode((800, 600))


# giereczka
pygame.display.set_caption("kucharzyna")

icon = pygame.image.load("assets/woman.png")
pygame.display.set_icon(icon)
# gracz
playerIMG = pygame.image.load("assets/cooker.png")
playerX = 368
playerY = 480
speed = 0
speed1 = 0
# przeciwnik

enemyIMG = pygame.image.load("assets/ninja.png.")
enemyX = random.randint(1, 735)
enemyY = random.randint(20, 300)
enemyspeed = 0.3

#przeciwnik 2

enemyIMG2 = pygame.image.load("assets/woman.png.")
enemy2X = random.randint(1, 735)
enemy2Y = random.randint(20, 300)
enemyspeed2 = 0.3

# broń
weaponIMG = pygame.image.load("assets/spatula.png.")
weaponX = 0
weaponY = 0
weaponspeedY = 1
weaponState = "ready"


def player(x, y):
    screen.blit(playerIMG, (x, y))



def enemy(x, y):
    screen.blit(enemyIMG, (x, y))


def enemy2(x, y):
    screen.blit(enemyIMG2, (x, y))


def throw_weapon(x, y):
    global weaponState
    weaponState = "throw"
    screen.blit(weaponIMG, (x + 16, y + 10))

def kolizja(enemyX, enemyY, weaponX, weaponY):
    if (enemyX <= weaponX + 25 and enemyX >= weaponX - 25) and (enemyY <= weaponY +25 and enemyY >= weaponY - 25):
        return  True
    else:
        return  False


def kolizja2(enemy2X, enemy2Y, weaponX, weaponY):
    if (enemy2X <= weaponX + 25 and enemy2X >= weaponX - 25) and (enemy2Y <= weaponY +25 and enemy2Y >= weaponY - 25):
        return  True
    else:
        return  False


def kolizja_enemy(playerX, playerY, enemyX, enemyY):
    if (playerX <= enemyX + 25 and playerX >= enemyX - 25) and (playerY <= enemyY +25 and playerY >= enemyY - 25):
        return  True
    else:
        return  False

def kolizja_enemy2(playerX, playerY, enemy2X, enemy2Y):
    if (playerX <= enemy2X + 25 and playerX >= enemy2X - 25) and (playerY <= enemy2Y +25 and playerY >= enemy2Y - 25):
        return  True
    else:
        return  False


def genEnemy():
    global enemyX, enemyY, enemyspeed
    enemyX = random.randint(1, 735)
    enemyY = random.randint(20, 300)
    enemyspeed = 0.5

def genEnemy2():
    global enemy2X, enemy2Y, enemyspeed2
    enemy2X = random.randint(1, 735)
    enemy2Y = random.randint(20, 300)
    enemyspeed2 = 0.5

#running
running = True
while running:
    screen.fill((255, 115, 115))  # Red Green Blu

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weaponY = playerY
                throw_weapon(playerX, weaponY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -0.5
            if event.key == pygame.K_RIGHT:
                speed = 0.5
            if event.key == pygame.K_UP:
                speed1 = -0.5
            if event.key == pygame.K_DOWN:
                speed1 = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed1 = 0
    playerX += speed
    playerY += speed1
    # blokowanie granic
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    # ogranicznie ruchu enemi
    if enemyX <= 0:
        enemyspeed *= -1
        enemyY += 32
    elif enemyX >= 736:
        enemyspeed *= -1
        enemyY += 32
    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= 536:
        enemyY = 0

    if enemy2X <= 0:
        enemyspeed2 *= -1
        enemy2Y += 32
    elif enemy2X >= 736:
        enemyspeed2 *= -1
        enemy2Y += 32
    if enemy2Y <= 0:
        enemy2Y = 0
    elif enemy2Y >= 536:
        enemy2Y = 0


    enemy2X += enemyspeed2
    enemyX += enemyspeed

    if weaponY <= -32:
        weaponY = -50
        weaponState = "ready"

    player(playerX, playerY)

    # strzał
    if weaponState == "throw":
        throw_weapon(playerX, weaponY)
        weaponY -= weaponspeedY
    kolizja(enemyX, enemyY, playerX, weaponY)
    if kolizja(enemyX,enemyY,playerX,weaponY):
        weaponState = "ready"
        weaponY = -50
        score += 1
        genEnemy()
        print(score)



    if kolizja(enemy2X,enemy2Y,playerX,weaponY):
        weaponState = "ready"
        weaponY = -50
        score += 1
        genEnemy2()
        print(score)


    if kolizja_enemy(playerX,playerY,enemyX,enemyY):
        playerX = 368
        playerY = 480
        speed = 0
        speed1 = 0
        score = 0
        print(score)


    if kolizja_enemy2(playerX,playerY,enemy2X,enemy2Y):
        playerX = 368
        playerY = 480
        speed = 0
        speed1 = 0
        score = 0
        print(score)


    enemy(enemyX, enemyY)
    enemy2(enemy2X, enemy2Y)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score: ' + str(score), False, (0, 0, 0))
    screen.blit(textsurface, dest=(0, 0))


    pygame.display.update()