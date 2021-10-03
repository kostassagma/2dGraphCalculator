import pygame
# for <RESIZEABLE>
from pygame.locals import *
import keyboard
import math
pygame.init()

# Create a displace surface object
screen = pygame.display.set_mode((800, 600), RESIZABLE)
w, h = pygame.display.get_surface().get_size()
width_center = int(w / 2)
height_center = int(h / 2)
position = [0, 0]
position_of_zero = [position[0] + width_center, position[1] + height_center]
running = True

# Title and icon
pygame.display.set_caption("2d Graph Calculator")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
my_font = pygame.font.SysFont('Arial', 30)

# background
one_unit = 21
# background_horizontal = pygame.image.load('horizontal_line.png')
# background_vertical = pygame.image.load('vertical_line.png')
background_x = width_center + position[0]
background_y = height_center + position[1]
# Vertical_unit_line = pygame.image.load('vertical_unit.jpg')
# Horizontal_unit_line = pygame.image.load('horizontal_unit.jpg')


def background(a, b, c, d):
    pygame.draw.line(screen, (0, 0, 0), (0, background_y), (pygame.display.get_surface().get_size()[0], background_y), 3)
    pygame.draw.line(screen, (0, 0, 0), (background_x, 0), (background_x, pygame.display.get_surface().get_size()[0]), 3)
    pygame.draw.line(screen, (0, 0, 0), (int(a), 0), (int(a), pygame.display.get_surface().get_size()[0]), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, int(b)), (pygame.display.get_surface().get_size()[0], int(b)), 1)
    pygame.draw.line(screen, (0, 0, 0), (int(c), 0), (int(c), pygame.display.get_surface().get_size()[0]), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, int(d)), (pygame.display.get_surface().get_size()[0], int(d)), 1)


# function
done_before = False
previous_x = 111110
previous_y = 11110
x = 0
y = 0

fun = ["math.sqrt(x)"]
typing = False

'''
def function_fun():
    return eval(fun)
'''

# mouse dragging
first_time_pressed = True
mouse_pressed = False
previous_mouse_pos = [0, 0]

previous_number = 0

# menu shit
a = pygame.display.get_surface().get_size()[0]/3
mouse_over_button = False
adding_new_fun = False
fun_to_be_added = []
showing_fun_to_be_added = ""
b = 50
c = [False, 0]
d = False
currently_editing = [False, 0]
fun_being_edited = []
first_time = True
showing_fun_being_edited = ""

while running:

    # RGB red green blue
    screen.fill((255, 255, 255))
    a = pygame.display.get_surface().get_size()[0] / 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_over_button:
                adding_new_fun = True
            elif int(a) >= pygame.mouse.get_pos()[0] >= 0:
                c = [True, pygame.mouse.get_pos()[1]]
            else:
                mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
            first_time_pressed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                one_unit += 1
            if event.button == 5 and one_unit != 1:
                one_unit -= 1
        if event.type == pygame.KEYDOWN:
            if adding_new_fun:
                if keyboard.is_pressed("1"):
                    fun_to_be_added += "1"
                elif keyboard.is_pressed("2"):
                    fun_to_be_added += "2"
                elif keyboard.is_pressed("3"):
                    fun_to_be_added += "3"
                elif keyboard.is_pressed("4"):
                    fun_to_be_added += "4"
                elif keyboard.is_pressed("5"):
                    fun_to_be_added += "5"
                elif keyboard.is_pressed("6"):
                    fun_to_be_added += "6"
                elif keyboard.is_pressed("7"):
                    fun_to_be_added += "7"
                elif keyboard.is_pressed("8"):
                    fun_to_be_added += "8"
                elif keyboard.is_pressed("9"):
                    if keyboard.is_pressed("shift"):
                        fun_to_be_added += "("
                    else:
                        fun_to_be_added += "9"
                elif keyboard.is_pressed("0"):
                    if keyboard.is_pressed("shift"):
                        fun_to_be_added += ")"
                    else:
                        fun_to_be_added += "0"
                elif keyboard.is_pressed("a"):
                    fun_to_be_added += "a"
                elif keyboard.is_pressed("b"):
                    fun_to_be_added += "b"
                elif keyboard.is_pressed("c"):
                    fun_to_be_added += "c"
                elif keyboard.is_pressed("d"):
                    fun_to_be_added += "d"
                elif keyboard.is_pressed("e"):
                    fun_to_be_added += "e"
                elif keyboard.is_pressed("f"):
                    fun_to_be_added += "f"
                elif keyboard.is_pressed("g"):
                    fun_to_be_added += "g"
                elif keyboard.is_pressed("h"):
                    fun_to_be_added += "h"
                elif keyboard.is_pressed("i"):
                    fun_to_be_added += "i"
                elif keyboard.is_pressed("j"):
                    fun_to_be_added += "j"
                elif keyboard.is_pressed("k"):
                    fun_to_be_added += "k"
                elif keyboard.is_pressed("l"):
                    fun_to_be_added += "l"
                elif keyboard.is_pressed("m"):
                    fun_to_be_added += "m"
                elif keyboard.is_pressed("n"):
                    fun_to_be_added += "n"
                elif keyboard.is_pressed("o"):
                    fun_to_be_added += "o"
                elif keyboard.is_pressed("p"):
                    fun_to_be_added += "p"
                elif keyboard.is_pressed("q"):
                    fun_to_be_added += "q"
                elif keyboard.is_pressed("r"):
                    fun_to_be_added += "r"
                elif keyboard.is_pressed("s"):
                    fun_to_be_added += "s"
                elif keyboard.is_pressed("t"):
                    fun_to_be_added += "t"
                elif keyboard.is_pressed("u"):
                    fun_to_be_added += "u"
                elif keyboard.is_pressed("v"):
                    fun_to_be_added += "v"
                elif keyboard.is_pressed("w"):
                    fun_to_be_added += "w"
                elif keyboard.is_pressed("x"):
                    fun_to_be_added += "x"
                elif keyboard.is_pressed("y"):
                    fun_to_be_added += "y"
                elif keyboard.is_pressed("z"):
                    fun_to_be_added += "z"
                elif keyboard.is_pressed("."):
                    fun_to_be_added += "."
                elif keyboard.is_pressed("-"):
                    fun_to_be_added += "-"
                elif keyboard.is_pressed("+"):
                    fun_to_be_added += "+"
                elif keyboard.is_pressed("/"):
                    fun_to_be_added += "/"
                elif keyboard.is_pressed("*"):
                    fun_to_be_added += "*"
                elif keyboard.is_pressed("backspace") and len(fun_to_be_added) != 0:
                    fun_to_be_added.pop(len(fun_to_be_added)-1)
                elif keyboard.is_pressed("enter"):
                    adding_new_fun = False
                    fun.append(showing_fun_to_be_added)
                    fun_to_be_added = []
            # ------------------------------------------------------------------------------------------------------
            elif currently_editing[0]:
                if keyboard.is_pressed("1"):
                    fun_being_edited += "1"
                elif keyboard.is_pressed("2"):
                    fun_being_edited += "2"
                elif keyboard.is_pressed("3"):
                    fun_being_edited += "3"
                elif keyboard.is_pressed("4"):
                    fun_being_edited += "4"
                elif keyboard.is_pressed("5"):
                    fun_being_edited += "5"
                elif keyboard.is_pressed("6"):
                    fun_being_edited += "6"
                elif keyboard.is_pressed("7"):
                    fun_being_edited += "7"
                elif keyboard.is_pressed("8"):
                    fun_being_edited += "8"
                elif keyboard.is_pressed("9"):
                    if keyboard.is_pressed("shift"):
                        fun_being_edited += "("
                    else:
                        fun_to_be_added += "9"
                elif keyboard.is_pressed("0"):
                    if keyboard.is_pressed("shift"):
                        fun_being_edited += ")"
                    else:
                        fun_to_be_added += "0"
                elif keyboard.is_pressed("a"):
                    fun_being_edited += "a"
                elif keyboard.is_pressed("b"):
                    fun_being_edited += "b"
                elif keyboard.is_pressed("c"):
                    fun_being_edited += "c"
                elif keyboard.is_pressed("d"):
                    fun_being_edited += "d"
                elif keyboard.is_pressed("e"):
                    fun_being_edited += "e"
                elif keyboard.is_pressed("f"):
                    fun_being_edited += "f"
                elif keyboard.is_pressed("g"):
                    fun_being_edited += "g"
                elif keyboard.is_pressed("h"):
                    fun_being_edited += "h"
                elif keyboard.is_pressed("i"):
                    fun_being_edited += "i"
                elif keyboard.is_pressed("j"):
                    fun_being_edited += "j"
                elif keyboard.is_pressed("k"):
                    fun_being_edited += "k"
                elif keyboard.is_pressed("l"):
                    fun_being_edited += "l"
                elif keyboard.is_pressed("m"):
                    fun_being_edited += "m"
                elif keyboard.is_pressed("n"):
                    fun_being_edited += "n"
                elif keyboard.is_pressed("o"):
                    fun_being_edited += "o"
                elif keyboard.is_pressed("p"):
                    fun_being_edited += "p"
                elif keyboard.is_pressed("q"):
                    fun_being_edited += "q"
                elif keyboard.is_pressed("r"):
                    fun_being_edited += "r"
                elif keyboard.is_pressed("s"):
                    fun_being_edited += "s"
                elif keyboard.is_pressed("t"):
                    fun_being_edited += "t"
                elif keyboard.is_pressed("u"):
                    fun_being_edited += "u"
                elif keyboard.is_pressed("v"):
                    fun_being_edited += "v"
                elif keyboard.is_pressed("w"):
                    fun_being_edited += "w"
                elif keyboard.is_pressed("x"):
                    fun_being_edited += "x"
                elif keyboard.is_pressed("y"):
                    fun_being_edited += "y"
                elif keyboard.is_pressed("z"):
                    fun_being_edited += "z"
                elif keyboard.is_pressed("-"):
                    fun_being_edited += "-"
                elif keyboard.is_pressed("+"):
                    fun_being_edited += "+"
                elif keyboard.is_pressed("/"):
                    fun_being_edited += "/"
                elif keyboard.is_pressed("*"):
                    fun_being_edited += "*"
                elif keyboard.is_pressed("."):
                    fun_being_edited += "."
                elif keyboard.is_pressed("backspace") and len(fun_being_edited) != 0:
                    fun_being_edited.pop(len(fun_being_edited) - 1)
                elif keyboard.is_pressed("enter"):
                    currently_editing[0] = False
                    fun[currently_editing[1]] = showing_fun_being_edited
                    fun_being_edited = []
                    # fun_to_be_added -= fun_to_be_added[len(fun_to_be_added)-1]
                '''if keyboard.is_pressed(")"):
                    fun_to_be_added += ")"'''

    showing_fun_being_edited = ""
    showing_fun_to_be_added = ""
    for i in fun_to_be_added:
        showing_fun_to_be_added += i

    # dragging
    if mouse_pressed:
        if not first_time_pressed:
            Sum_x = pygame.mouse.get_pos()[0] - previous_mouse_pos[0]
            position[0] += Sum_x
            Sum_y = pygame.mouse.get_pos()[1] - previous_mouse_pos[1]
            position[1] += Sum_y
        previous_mouse_pos = pygame.mouse.get_pos()
        first_time_pressed = False
    background_x = width_center + position[0]
    background_y = height_center + position[1]
    x = 0
    times_run = 0
    # background
    times_done = one_unit

    while times_done <= w:
        background(w / 2 + position[0] + times_done, h / 2 + position[1] + times_done, w / 2 + position[0] - times_done,
                   h / 2 + position[1] - times_done)
        times_done += one_unit

    # Typing the function------------------------------------------------------------------------------------------#
    if mouse_pressed and pygame.display.get_surface().get_size()[0] >= pygame.mouse.get_pos()[0] >= pygame.display.get_surface().get_size()[0] - 70 and 0 <= pygame.mouse.get_pos()[1] <= 30:
        typing = True
        print("yes")

    # presenting function
    for i in fun:
        try:
            times_run = 0
            while times_run != pygame.display.get_surface().get_size()[0]:
                x = (times_run - w/2 - position[0]) / one_unit
                try:
                    y = eval(i) * one_unit
                    d = True
                except:
                    d = False
                presenting_x = times_run
                presenting_y = h/2 + position[1] - y
                if done_before and presenting_x != w:
                    pygame.draw.line(screen, (0, 0, 255), (int(presenting_x), int(presenting_y)), (int(previous_x), int(previous_y)), 2)
                    previous_x = presenting_x
                    previous_y = presenting_y
                elif not done_before:
                    done_before = False
                    previous_x = presenting_x
                    previous_y = presenting_y
                times_run += 1
                done_before = d
                '''if pygame.mouse.get_pos()[0] == presenting_x:
                    values = f"x={int(x*100)/100}, y={int(function_fun()*100)/100}"
                    text_surface = my_font.render(values, False, (0, 0, 255))
                    screen.blit(text_surface, (pygame.display.get_surface().get_size()[0] - 150 - ((len(values)-11)*10), 0))
                    pygame.draw.circle(screen, (0, 0, 255), (int(presenting_x) + 1, int(previous_y) + 1), 4)
                    # circle(surface, color, center, radius)'''
            done_before = False
        except:
            print(fun)

    # text_surface_2 = my_font.render(fun, False, (0, 0, 255))
    # screen.blit(text_surface_2, (0, 0))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, int(a), pygame.display.get_surface().get_size()[1]))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, int(a) - 1, pygame.display.get_surface().get_size()[1]))
    if 44 >= pygame.mouse.get_pos()[0] >= 0 and 44 >= pygame.mouse.get_pos()[1] >= 0:
        pygame.draw.rect(screen, (190, 190, 190), pygame.Rect(0, 0, 44, 44))
        mouse_over_button = True
    else:
        mouse_over_button = False
    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(7, 19, 30, 6))
    pygame.draw.rect(screen, (30, 30, 30), pygame.Rect(19, 7, 6, 30))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 44, int(a), 1))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(44, 0, 1, 44))
    text_surface_2 = my_font.render(showing_fun_to_be_added, False, (0, 0, 0))
    screen.blit(text_surface_2, (50, 5))
    b = 44
    times_done_loop = 0
    for i in fun:
        text_surface_3 = my_font.render(i, False, (0, 0, 0))
        screen.blit(text_surface_3, (7, b))
        b += 40
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, b, int(a), 1))
        if b >= pygame.mouse.get_pos()[1] >= b-40 and pygame.mouse.get_pos()[0] <= pygame.display.get_surface().get_size()[0]/3:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pygame.display.get_surface().get_size()[0]/3 - 124, b - 39, 123, 39))
        if b >= pygame.mouse.get_pos()[1] >= b-40 and pygame.display.get_surface().get_size()[0]/3 - 120 <= pygame.mouse.get_pos()[0] <= pygame.display.get_surface().get_size()[0]/3 - 50:
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(pygame.display.get_surface().get_size()[0]/3 - 123, b - 34, 72, 28))
            if c[0]:
                fun.pop(times_done_loop)
                c[0] = False
        if b >= pygame.mouse.get_pos()[1] >= b-40 and pygame.display.get_surface().get_size()[0]/3 - 50 <= pygame.mouse.get_pos()[0] <= pygame.display.get_surface().get_size()[0]/3:
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(pygame.display.get_surface().get_size()[0]/3 - 47, b - 34, 45, 28))
            if c[0]:
                currently_editing = [True, times_done_loop]
                first_time = True
                c[0] = False
        if b >= pygame.mouse.get_pos()[1] >= b-40 and pygame.mouse.get_pos()[0] <= pygame.display.get_surface().get_size()[0]/3:
            text_surface_2 = my_font.render("delete|edit", False, (0, 0, 0))
            screen.blit(text_surface_2, (int(pygame.display.get_surface().get_size()[0]/3) - 120, b - 40))
        times_done_loop += 1
    not_done = True
    c[0] = False

    # editing a function
    if currently_editing[0]:
        if first_time:
            for i in fun[currently_editing[1]]:
                fun_being_edited.append(i)
            first_time = False
        for i in fun_being_edited:
            showing_fun_being_edited += i
        text_surface_2 = my_font.render(showing_fun_being_edited, False, (0, 0, 0))
        screen.blit(text_surface_2, (50, 5))

    pygame.display.update()
pygame.quit()
