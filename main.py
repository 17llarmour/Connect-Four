from pygame import *


# mouse.get_pos()
# Arrow following cursor, when click, place counter


def add_counters(screen, grid, colour, column):
    row = len(grid) - 1
    # print(row)
    while grid[row][column] != "b":
        row -= 1
        # print(row)
    grid[row][column] = colour
    draw_grid(screen, grid)
    win = win_check(grid, row, column, colour)
    return (grid, win)


def draw_grid(screen, grid):
    screen.fill((0, 0, 0))

    draw.rect(screen, (31, 90, 255), (50, 50, 700, 600))
    y_offset = 0
    row = 0

    while y_offset < 600:
        x_offset = 0
        col = 0
        while x_offset < 700:
            if grid[row][col] == "b":
                draw.circle(screen, (255, 255, 255), (100 + x_offset, 100 + y_offset), 40)
            elif grid[row][col] == "r":
                draw.circle(screen, (255, 0, 0), (100 + x_offset, 100 + y_offset), 40)
            else:
                draw.circle(screen, (255, 255, 0), (100 + x_offset, 100 + y_offset), 40)
            x_offset += 100
            col += 1
        y_offset += 100
        row += 1

    display.flip()
    time.delay(5)


def win_check(grid, lastRow, lastCol, colour):
    return win_horizontal_check(grid, lastRow, lastCol, colour) or \
           win_verticle_check(grid, lastRow, lastCol, colour) or \
           win_right_diagonal_check(grid, lastRow, lastCol, colour) or \
           win_left_diagonal_check(grid, lastRow, lastCol, colour)


def win_horizontal_check(grid, lastRow, lastCol, colour):
    found = 1
    x = 1
    while lastCol + x < 7 and grid[lastRow][lastCol + x] == colour:
        found += 1
        x += 1
    x = 1
    while lastCol - x >= 0 and grid[lastRow][lastCol - x] == colour:
        found += 1
        x += 1
    if found >= 4:
        return True
    return False


def win_verticle_check(grid, lastRow, lastCol, colour):
    found = 1
    x = 1
    while lastRow + x <= 4 and grid[lastRow + x][lastCol] == colour:
        found += 1
        x += 1
    if found >= 4:
        return True
    return False


def win_right_diagonal_check(grid, lastRow, lastCol, colour):
    found = 1
    x = 1
    y = 1
    while lastCol + x < 7 and lastRow - y >= 0 and grid[lastRow - y][lastCol + x] == colour:
        found += 1
        x += 1
        y += 1
    x = 1
    y = 1
    while lastCol - x >= 0 and lastRow + y <= 4 and grid[lastRow + y][lastCol - x] == colour:
        found += 1
        x += 1
        y += 1
    if found >= 4:
        return True
    return False


def win_left_diagonal_check(grid, lastRow, lastCol, colour):
    found = 1
    x = 1
    y = 1
    while lastCol - x >= 0 and lastRow - y >= 0 and grid[lastRow - y][lastCol - x] == colour:
        found += 1
        x += 1
        y += 1
    x = 1
    y = 1
    while lastCol + x < 7 and lastRow + y <= 4 and grid[lastRow + y][lastCol + x] == colour:
        found += 1
        x += 1
        y += 1
    print(found)
    if found >= 4:
        return True
    return False


def arrow_draw(screen, mouse_pos, last_mouse):
    draw.rect(screen, (0, 0, 0), (last_mouse, 25, 10, 10))
    draw.rect(screen, (0, 255, 0), (mouse_pos, 25, 10, 10))

    display.flip()
    time.delay(5)


if __name__ == '__main__':

    init()
    width = 800
    height = 700

    screen = display.set_mode((width, height))
    end_program = False

    column = -1

    grid = [["b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b", "b", "b"]]

    draw_grid(screen, grid)

    player = ["r", "y"]
    pos = 0
    win = False

    last_mouse_x = 0

    while not end_program:
        for e in event.get():
            if e.type == QUIT:
                end_program = True
            if e.type == KEYDOWN:

                if e.key == K_1:
                    column = 0
                if e.key == K_2:
                    column = 1
                if e.key == K_3:
                    column = 2
                if e.key == K_4:
                    column = 3
                if e.key == K_5:
                    column = 4
                if e.key == K_6:
                    column = 5
                if e.key == K_7:
                    column = 6
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    (column, row) = mouse.get_pos()
                    if column < 50 or column > 750:
                        column = -1
                    else:
                        column /= 100
                        column -= 1
                        column = round(column)

        (mouse_x, mouse_y) = mouse.get_pos()
        arrow_draw(screen, mouse_x, last_mouse_x)
        last_mouse_x = mouse_x

        while column != -1:
            if grid[0][column] != "b":
                print("Column full")
                column = -1
                break
            if pos > 1:
                pos = 0
            turn = player[pos]

            (grid, win) = add_counters(screen, grid, turn, column)

            pos += 1
            column = -1

        if win == True:
            end_program = True

    print("Player", turn, "has won!")
