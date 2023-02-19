from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time



def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)

    glBegin(GL_TRIANGLES)
    glColor3f(255, 215, 0)
    glVertex3f(250, 460, 0)
    glVertex3f(50, 300, 0)
    glVertex3f(450, 300, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 0, 255)
    glVertex2i(60, 300)
    glVertex2i(440, 300)
    glVertex2i(440, 90)
    glVertex2i(60, 90)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(100, 260)
    glVertex2i(140, 260)
    glVertex2i(140, 220)
    glVertex2i(100, 220)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(360, 260)
    glVertex2i(400, 260)
    glVertex2i(400, 220)
    glVertex2i(360, 220)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(195, 240)
    glVertex2i(315, 240)
    glVertex2i(315, 90)
    glVertex2i(195, 90)
    glEnd()

    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2i(295, 160)
    glEnd()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_02")
glutDisplayFunc(showScreen)

glutMainLoop()