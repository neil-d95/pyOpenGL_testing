#!/usr/bin/python
import sys
import time
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

spin = 0.0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)


def display():
    global spin
    print(spin)
    time.sleep(0.06)
    spin += 0.5
    if(spin > 360.0):
        spin = spin - 360.0
    texts = str(spin)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLoadIdentity()             # clear the matrix
    # viewing transformation
    gluLookAt(0.0, 0.0, 5.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)
    glPushMatrix()
    # Fixed triangle for roll indication.
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.05, 0.95)
    glVertex2f(-0.05, 0.95)
    glEnd()
    glRasterPos2f(2.5, 2.5)
    for char in texts:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glRectf(1.0, 0.01, -1.0, -0.01)
    glRotatef(spin, 0.0, 0.0, 1.0)
    # Draw Pitch marks half for 5 degrees whole for 10 degrees
    num = 0.25
    while num < 2.0:
        if num % 0.5 == 0:
            line_width = 1.0
        else:
            line_width = 0.5
        glBegin(GL_LINES)
        glVertex2f(line_width, num)
        glVertex2f(-line_width, num)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(line_width, -num)
        glVertex2f(-line_width, -num)
        glEnd()
        num += 0.25
    glColor3f(0.0, 0.0, 1.0)
    glRectf(2.0, 2.0, -2.0, 0.0)
    glColor3f(0.5, 0.35, 0.05)
    glRectf(2.0, -2.0, -2.0, 0.0)

    glPopMatrix()
    glutSwapBuffers()
    glutPostRedisplay()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == chr(27):
        import sys
        sys.exit(0)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow('HSI')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()
