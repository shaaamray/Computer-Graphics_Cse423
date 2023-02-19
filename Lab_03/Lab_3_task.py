from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(0, 255, 0)
    glVertex2f(x, y)
    glEnd()


def Circlepoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def midPointCircle(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    Circlepoints(x, y, x0, y0)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x, y, x0, y0)

def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_circles(400, 400, 200)
    glutSwapBuffers()

def draw_circles(x, y, radius):
    midPointCircle(x, y, radius)
    midPointCircle(x + (radius / 2), y, radius / 2)
    midPointCircle(x, y + (radius / 2), radius / 2)
    midPointCircle(x, y - (radius / 2), radius / 2)
    midPointCircle(x - (radius / 2), y, radius / 2)
    offset = .11*radius
    x0 = x - (radius / 2) + offset
    y0 = y + (math.sin(45) * (radius / 2)) - offset
    midPointCircle(x0, y0, radius / 2)
    x0 = x + (radius / 2) - offset
    y0 = y + (math.sin(45) * (radius / 2)) - offset
    midPointCircle(x0, y0, radius / 2)
    x0 = x + (radius / 2) - offset
    y0 = y - (math.sin(45) * (radius / 2)) + offset
    midPointCircle(x0, y0, radius / 2)
    x0 = x - (radius / 2) + offset
    y0 = y - (math.sin(45) * (radius / 2)) + offset
    midPointCircle(x0, y0, radius / 2)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(650, 650)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab3_Task")
glutDisplayFunc(screen)

glutMainLoop()