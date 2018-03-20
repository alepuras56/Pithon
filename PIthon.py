import pygame, random, sys


def collide(x1, x2, y1, y2, d):
    if x1 + d > x2 and x1 < x2 + d and y1 + d > y2 and y1 < y2 + d:
        return True
    else:
        return False

def die(screen, score):
    typewriter.play()
    done = False
    x = 10
    y = 10
    count = 0
    totalWidth = 0
    font = pygame.font.SysFont('Arial', 60)
    while not done:
        text = font.render(pi[count], True, (255, 255, 255))
        count += 1
        if count >= score:
            done = True
            typewriter.stop()
        screen.blit(text, (x,y))
        pygame.display.update()
        pygame.time.wait(50)
        x += text.get_width()
        totalWidth += text.get_width()
        if totalWidth > 750:
            totalWidth = 0
            x = 10
            y += text.get_height() + 10
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)

def type2(num, pos):
    font = pygame.font.SysFont('Arial', 20)
    text = font.render(num, 1, (0, 0, 0))
    screen.blit(text, pos)

def type(num, pos):
    char = pi[int(num)]
    if char == "." : screen.blit(dot, pos)
    elif char == "0" : screen.blit(zero, pos)
    elif char == "1" : screen.blit(one, pos)
    elif char == "2" :  screen.blit(two, pos)
    elif char == "3" : screen.blit(three, pos)
    elif char == "4" : screen.blit(four, pos)
    elif char == "5" : screen.blit(five, pos)
    elif char == "6" : screen.blit(six, pos)
    elif char == "7" : screen.blit(seven, pos)
    elif char == "8" : screen.blit(eight, pos)
    elif char == "9" : screen.blit(nine, pos)

pro = False
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116"

dot = pygame.image.load(".\Resources\..png")
zero = pygame.image.load(r".\Resources\0.png")
one = pygame.image.load(r".\Resources\1.png")
two = pygame.image.load(r".\Resources\2.png")
three = pygame.image.load(r".\Resources\3.png")
four = pygame.image.load(r".\Resources\4.png")
five = pygame.image.load(r".\Resources\5.png")
six = pygame.image.load(r".\Resources\6.png")
seven = pygame.image.load(r".\Resources\7.png")
eight = pygame.image.load(r".\Resources\8.png")
nine = pygame.image.load(r".\Resources\9.png")

pygame.mixer.init()
munch = pygame.mixer.Sound(".\Resources\munch.wav")
bad = pygame.mixer.Sound(r".\Resources\bad2.wav")
typewriter = pygame.mixer.Sound(r".\Resources\type.wav")

pygame.init()
locked = False
screenWidth, screenHeight = 800, 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('PI-thon')
clock = pygame.time.Clock()

#Get GameLevel
choice = False
font = pygame.font.SysFont('Arial', 60)
text = font.render("Welcome to PIthon!", True, (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery - 100
screen.fill((0, 0, 0))
screen.blit(text, textrect)

font = pygame.font.SysFont('Arial', 40)

text = font.render("Select your mode", True, (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery - 30
screen.blit(text, textrect)

text = font.render("I love pi", True, (255, 255, 255))
prorect = text.get_rect()
prorect.centerx = screen.get_rect().centerx - 200
prorect.centery = screen.get_rect().centery + 30
screen.blit(text, prorect)

text = font.render("I love pie", True, (255, 255, 255))
funrect = text.get_rect()
funrect.centerx = screen.get_rect().centerx + 200
funrect.centery = screen.get_rect().centery + 30
screen.blit(text, funrect)

font = pygame.font.SysFont('Arial', 25)
text = font.render("(Choose the correct next digit)", True, (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx - 200
textrect.centery = screen.get_rect().centery + 65
screen.blit(text, textrect)

text = font.render("(Free mode)", True, (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx + 200
textrect.centery = screen.get_rect().centery + 65
screen.blit(text, textrect)

pygame.display.update()
while not choice:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if prorect.collidepoint(pos[0], pos[1]):
                choice = True
                pro = True
            if funrect.collidepoint(pos[0], pos[1]):
                choice = True
                pro = False
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()


#Start with the game
partWidth = 25
xs = [320, 320, 320, 320]
ys = [180, 160, 140, 120]
direction = "D"
randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
applepos = randx, randy
randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
randOtherAppleValue = int(random.randint(0, 9))
while randOtherAppleValue == int(pi[len(xs)]):
    randOtherAppleValue = int(random.randint(0, 9))
otherApplePos = randx, randy

while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and not locked:
            if event.key == pygame.K_UP and direction != "D":
                direction = "U"
                locked = True
            elif event.key == pygame.K_DOWN and direction != "U":
                direction = "D"
                locked = True
            elif event.key == pygame.K_LEFT and direction != "R":
                direction = "L"
                locked = True
            elif event.key == pygame.K_RIGHT and direction != "L":
                direction = "R"
                locked = True
    i = len(xs)-1
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], partWidth):
            die(screen, len(xs))
        i -= 1
    if collide(xs[0], applepos[0] - partWidth/2, ys[0], applepos[1] - partWidth/2, partWidth):
        munch.play()
        xs.append(0)
        ys.append(0)
        randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
        randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
        applepos = randx, randy
        randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
        randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
        randOtherAppleValue = int(random.randint(0, 9))
        while randOtherAppleValue == int(pi[len(xs)]):
            randOtherAppleValue = int(random.randint(0, 9))
        otherApplePos = randx, randy
    if collide(xs[0], otherApplePos[0] - partWidth/2, ys[0], otherApplePos[1] - partWidth/2, partWidth) and pro:
        rand = int(random.randint(0, 2))
        bad.play()
        xs.pop()
        ys.pop()
        if xs.__len__() == 0:
            die(screen, 0)
        randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
        randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
        applepos = randx, randy
        randx = (int(random.randint(partWidth, screenWidth - partWidth)/partWidth) * partWidth) + partWidth / 2
        randy = (int(random.randint(partWidth, screenHeight - partWidth)/partWidth) * partWidth) - partWidth / 2
        randOtherAppleValue = int(random.randint(0, 9))
        if pi[len(xs)] != '.':
            while randOtherAppleValue == int(pi[len(xs)]):
                randOtherAppleValue = int(random.randint(0, 9))
        otherApplePos = randx, randy

    if xs[0] < 0 or xs[0] > screenWidth or ys[0] < 0 or ys[0] > screenHeight:
        die(screen, len(xs))
    i = len(xs)-1
    while i >= 1:
        xs[i] = xs[i-1]
        ys[i] = ys[i-1]
        i -= 1
    if direction == "D" :
        ys[0] += partWidth
    elif direction == "R" :
        xs[0] += partWidth
    elif direction == "U" :
        ys[0] -= partWidth
    elif direction == "L" :
        xs[0] -= partWidth
    locked = False
    screen.fill((86, 3, 173))
    for i in range(0, len(xs)):
        type(i, (xs[i], ys[i]))
    pygame.draw.circle(screen, (255, 177, 0), applepos, partWidth/2, 0)
    type2(pi[i+1], (applepos[0]-4, applepos[1]-12))
    if pro:
        pygame.draw.circle(screen, (255, 177, 0), otherApplePos, partWidth/2, 0)
        type2(str(randOtherAppleValue), (otherApplePos[0]-4, otherApplePos[1]-12))
    pygame.display.update()