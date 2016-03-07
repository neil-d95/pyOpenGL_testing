#!/usr/bin/python
import sys
import time
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

roll = 0.0
pitch = 0.0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)


def display():
    global roll
    global pitch

    if(roll > 360.0):
        roll = roll - 360.0
    if(pitch > 90.0):
        roll = roll + 180.0
        pitch = 89.5
    elif(pitch < -90.0):
        roll = roll + 180.0
        pitch = -89.5

    text_roll = str(roll)
    text_pitch = str(pitch)
    font = GLUT_BITMAP_HELVETICA_18

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
    # Roll Text top Right
    glRasterPos2f(1.5, 2.0)
    for char in text_roll:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glRasterPos2f(-2.0, 2.0)
    for char in text_pitch:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glColor3f(1.0, 1.0, 0.0)
    glRectf(0.02, 0.02, -0.02, -0.02)
    glRectf(1.0, 0.01, 0.25, -0.01)
    glRectf(-0.25, 0.01, -1.0, -0.01)
    glRotatef(roll, 0.0, 0.0, 1.0)
    pitch_angle = pitch * 0.05
    glTranslatef(0.0, -pitch_angle, 0.0)
    # Draw Pitch marks half for 5 degrees whole for 10 degrees
    glColor3f(1.0, 1.0, 1.0)
    num = 0.0
    while num <= 4.5:
        if num % 0.5 == 0:
            line_width = 1.0
        else:
            line_width = 0.5
        glBegin(GL_LINES)
        glVertex2f(line_width, num)
        glVertex2f(-line_width, num)
        glEnd()
        # Add 10 degree Text
        degree = num / 0.05
        if degree % 10 == 0 and degree != 0:
            glRasterPos2f(-1.0, num)
            for char in str(int(degree)):
                glutBitmapCharacter(font, ord(char))
            glRasterPos2f(-1.0, -num)
            for char in str(int(-degree)):
                glutBitmapCharacter(font, ord(char))
        glBegin(GL_LINES)
        glVertex2f(line_width, -num)
        glVertex2f(-line_width, -num)
        glEnd()
        num += 0.25

    # Draw Fixed triangle for 0 degrees Roll
    glTranslatef(0.0, pitch_angle, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.055, 1.055)
    glVertex2f(-0.055, 1.055)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glRectf(2.0, 2.0, -2.0, -pitch_angle)
    glColor3f(0.5, 0.35, 0.05)
    glRectf(2.0, -2.0, -2.0, -pitch_angle)

    glPopMatrix()
    glutSwapBuffers()
    glutPostRedisplay()


def reshape(w, h):
    glViewport(0, 0, w, h)
    if h == 0:
        h = 1
    aspect = w / h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    gluPerspective(45, aspect, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global roll
    global pitch

    if key == GLUT_KEY_LEFT or key == b"4":
        print("Left")
        roll -= 0.5
    elif key == GLUT_KEY_RIGHT or key == b"6":
        print("Right")
        roll += 0.5
    elif key == GLUT_KEY_UP or key == b"8":
        print("Up")
        if roll > 90 and roll < 270:
            pitch += 0.5
        else:
            pitch -= 0.5
    elif key == GLUT_KEY_DOWN or key == b"2":
        print("Down")
        if roll > 90 and roll < 270:
            pitch -= 0.5
        else:
            pitch += 0.5
    elif key == 110 or key == b"5":
        print("Center")
        roll = 0.0
        pitch = 0.0
glutInit(sys.argv)

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow('HSI')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutSpecialFunc(keyboard)
glutMainLoop()
