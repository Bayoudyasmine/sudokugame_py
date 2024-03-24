
from random import sample
from constant import *
from button import Button
from copy import deepcopy



from timer import TEMPS
from score import incremnter_score,getscore

def Generer(empties):
    from destribution import destribution
    from excellent import Excellent
    from game_over import Game_over

    SCREEN.blit(BG3, (0, 0))
    PLAY_MOUSE_POS = pygame.mouse.get_pos()

    GAME_BUTTON = Button(image=pygame.image.load("assets\ButtonGR.png"), pos=(600, 450),
                         text_input="Game over", font=get_font(19), base_color="BLACK", hovering_color="#9AA8BF")

    for button in [GAME_BUTTON]:
        button.changeColor(PLAY_MOUSE_POS)
        button.update(SCREEN)

    def pattern(r, c): return (base*(r % base)+r//base+c) % side

    def shuffle(s): return sample(s, len(s))
    rBase = range(base)
    rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base*base+1))

    grid = [[nums[pattern(r, c)] for r in rows] for c in cols]

    check_grid = deepcopy(grid)

    squares = side*side
    # empties = 12  # squares * 3//4
    for p in sample(range(squares), empties):
        grid[p//side][p % side] = 0

    grid_original = [[grid[x][y] for y in range(
        len(grid[0]))] for x in range(len(grid[0]))]
    print(grid_original)
    print(grid)
    print(check_grid)

    def is_used_in_row(num, r):
        for i in range(9):
            if grid[r][i] == num:
                return True
        return False

    def is_used_in_column(num, c):
        for i in range(9):
            if grid[i][c] == num:
                return True
        return False

    def is_used_in_box(num, r, c):
        box_r = srn * (r // srn)
        box_c = srn * (c // srn)
        for i in range(srn):
            for j in range(srn):
                # self.board[box_r + i][box_c + j] = '*'
                if grid[box_r + i][box_c + j] == num:
                    return True
        return False

    def isvalid(k, i, j):
        # check row
        if not is_used_in_row(k, i):
            # check column
            if not is_used_in_column(k, j):
                # check box
                if not is_used_in_box(k, i, j):
                    return True
        return False

    def is_solved():
        if is_board_filled():
            for a in range(9):
                for b in range(9):
                    if grid[a-1][b-1] == check_grid[a-1][b-1]:
                        SCREEN.blit(BG4, (0, 0))
                        destribution(check_grid, myfont,
                                     original_grid_element_color, 45, 81)
                        Excellent()

    def is_board_filled():
        global n, s
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return False
        return True
    def insert(SCREEN, position):
        i, j = position[1], position[0]
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if(grid_original[i-1][j-1] != 0):
                        return
                    if(event.key == 48):  # checking with 0
                        grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(SCREEN, background_color, (
                            position[0]*40 + 25, position[1]*40 + 53, 40 - 2*buffer, 40 - 2*buffer))
                        pygame.display.update()
                        return
                    if(0 < event.key - 48 < 10):  # We are checking for valid input
                        pygame.draw.rect(SCREEN, background_color, (
                            position[0]*40 + 25, position[1]*40+53, 40 - 2*buffer, 40 - 2*buffer))
                        num = event.key - 48
                        mult=20
                        if isvalid(num, i-1, j-1):
                            value = myfont.render(
                                str(event.key-48), True, (0, 0, 0))
                            SCREEN.blit(
                                value, (position[0]*40+32, position[1]*40+47))
                            grid[i-1][j-1] = num
                            s=mult*5
                            incremnter_score(s)
                            pygame.draw.rect(SCREEN,'#FEAE49', (550, 100, 200, 50))
                        else:
                            s=-mult*4
                            incremnter_score(s)
                            value = myfont.render(
                                str(event.key-48), True, (255, 0, 0))
                            SCREEN.blit(
                                value, (position[0]*40 +32, position[1]*40+47))
                            pygame.draw.rect(SCREEN,'#FEAE49', (550, 100, 200, 50))
                        scor='score: {score:02d}'.format(score=getscore())
                        value1 = myfont.render(scor, True, '#3D424A')
                        SCREEN.blit(value1, (550, 100)) 
                        pygame.display.flip() 
                    is_solved()
                    pygame.display.update()
                    return
                return

    destribution(grid, myfont, original_grid_element_color, 32, 47)

    GAME_BUTTON = Button(image=pygame.image.load("assets\ButtonGR.png"), pos=(600, 450),
                         text_input="Game over", font=get_font(19), base_color="#4E596B", hovering_color="#9AA8BF")
    for button in [GAME_BUTTON]:
        button.changeColor(PLAY_MOUSE_POS)
        button.update(SCREEN)

    game = TEMPS()

    while True:
        if not issalah:
            game.updateTimer()
        game.render(SCREEN)
        if GAME_BUTTON.draw():
            SCREEN.blit(BG5, (0, 0))
            destribution(check_grid, myfont,
                         original_grid_element_color, 45, 81)
            Game_over()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(SCREEN, ((pos[0]-19)//40, (pos[1]-46)//40))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
