from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(255, 0, 0)
    glVertex2f(x, y)
    glEnd()


def draw_point_black(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(x, y)
    glEnd()


def dda(x1, y1, x2, y2):
    steps = abs(x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else abs(y2 - y1)
    a = (x2 - x1) / steps
    b = (y2 - y1) / steps
    x = x1
    y = y1
    for j in range(0, steps):
        draw_points(x, y)
        x += a
        y += b


def d_dda(x1, y1, x2, y2):
    steps = abs(x2 - x1) if abs(x2 - x1) > abs(y2 - y1) else abs(y2 - y1)
    a = (x2 - x1) / steps
    b = (y2 - y1) / steps
    x = x1
    y = y1
    c = 0
    for i in range(0, steps):
        if c % 2 == 0:
            draw_points(x, y)
        else:
            draw_point_black(x, y)
        x += a
        y += b
        c += 1


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    student_id = 19201109
    if student_id % 2 ==0:
        d_dda(160,440, 440, 440)
        dda(300, 440, 300, 160)
    else:
        d_dda(150, 450, 150, 150)
        dda(400, 450, 400, 150)
        dda(150,300, 400, 300)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_03")
glutDisplayFunc(showScreen)

glutMainLoop()