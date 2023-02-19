from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(0, 179, 0)
    glVertex2f(x, y)
    glEnd()


def convertZone0(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 3:
        x1,y1 = -x1,y1
    elif zone == 4:
        x1,y1 = -x1,-y1
    elif zone == 7:
        x1,y1 = x1,-y1
    elif zone == 1:
        x1,y1 = y1,x1
    elif zone == 2:
        x1,y1 = y1,-x1
    elif zone == 5:
        x1,y1 = -y1,-x1
    elif zone == 6:
        x1,y1 = -y1,x1

    return x1, y1


def org_zone(x1, y1, zone):
    if zone == 0:
        pass
    elif zone == 3:
        x1,y1 = -x1,y1
    elif zone == 4:
        x1,y1 = -x1,-y1
    elif zone == 7:
        x1,y1 = x1,-y1
    elif zone == 1:
        x1,y1 = y1,x1
    elif zone == 2:
        x1,y1 = -y1,x1
    elif zone == 5:
        x1,y1 = -y1,-x1
    elif zone == 6:
        x1,y1 = y1,-x1

    return x1, y1


def midPoint(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)

    draw_points(x1, y1)

    x1, y1 = convertZone0(x1, y1, zone)
    x2, y2 = convertZone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx / 2)
    x = x1
    y = y1

    while (x < x2):
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + (dy - dx)
            y = y + 1
        x_new, y_new = org_zone(x, y, zone)
        draw_points(x_new, y_new)


def FindZone(x1, y1, x2, y2):
    dx = (x2-x1)
    dy =(y2-y1)
    zone = None
    if (abs(dx) >= abs(dy)):
        if (dx >= 0 and dy >= 0):
            zone = 0
        if (dx < 0 and dy >= 0):
            zone = 3
        if (dx < 0 and dy < 0):
            zone = 4
        if (dx >= 0 and dy < 0):
            zone = 7

    elif (abs(dy) > abs(dx)):
        if (dx >= 0 and dy >= 0):
            zone = 1
        if (dx < 0 and dy >= 0):
            zone = 2
        if (dx < 0 and dy < 0):
            zone = 5
        if (dx >= 0 and dy < 0):
            zone = 6
    return zone

def digit_nine(length, width, x_val, y_val):

    midPoint(x_val, y_val, x_val, y_val + length)
    midPoint(x_val, y_val + length, x_val + width, y_val + length)
    midPoint(x_val + width, y_val + length, x_val + width, y_val)
    midPoint(x_val + width, y_val, x_val, y_val)
    midPoint(x_val, y_val - length, x_val + width, y_val - length)
    midPoint(x_val + width, y_val - length, x_val + width, y_val)

def digit_zero(length, width, x_val, y_val):

    midPoint(x_val,y_val, x_val, y_val + length)
    midPoint(x_val, y_val + length, x_val + width, y_val + length)
    midPoint(x_val + width, y_val + length, x_val + width, y_val)
    midPoint(x_val, y_val, x_val, y_val - length)
    midPoint(x_val, y_val - length, x_val + width, y_val - length)
    midPoint(x_val + width, y_val - length, x_val + width, y_val)


def id_digit():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 750, 750)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ID = 19201109
    digit_zero(150, 150, 300, 500)
    digit_nine(150, 150, 500, 500)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(750, 750)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Lab 2_Task")
glutDisplayFunc(id_digit)

glutMainLoop()