#!/usr/bin/python
import sys
from math import radians, tan, sin, cos
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Changed for working on inverted
roll = 0.0
pitch = 0.0


def box_cal(roll, pitch_angle):
    x_max = 2.0
    y_max = 2.0
    pitch_roll = radians(roll + 90)
    sector = int(roll / 90)
    roll = roll % 90.0
    roll_rad = radians(roll)

    diff_y = pitch_angle / sin(pitch_roll)
    diff_x = pitch_angle / cos(pitch_roll)

    x_hoz_right = x_max
    x_hoz_left = -x_max
    y_hoz_right = x_max
    y_hoz_left = -x_max
    if sector == 0:
        if roll >= 0 and roll <= 45:
            blue_top_right = 2, 2
            blue_top_left = -2, 2
            blue_top_extra = -2, 2
            brown_bottom_extra = 2, -2
            brown_bottom_right = 2, -2
            brown_bottom_left = -2, -2

            y_hoz_left = (tan(roll_rad) * -x_max) - diff_y
            y_hoz_right = (tan(roll_rad) * x_max) - diff_y

            over_y_right = y_hoz_right - 2.0
            under_y_left = y_hoz_left + 2.0
            if y_hoz_left <= -2.0:
                y_hoz_left = -2.0
                if roll != 0:
                    x_hoz_left = -x_max - (under_y_left / tan(roll_rad))
                if x_hoz_left >= 2.0:
                    x_hoz_left = 2.0
                brown_bottom_left = x_hoz_left, -2
                blue_top_extra = -2, -2
            if y_hoz_left >= 2.0:
                y_hoz_left = 2.0
            if y_hoz_right <= -2.0:
                y_hoz_right = -2.0
            if y_hoz_right >= 2.0:
                y_hoz_right = 2.0
                if roll != 0:
                    x_hoz_right = x_max - (over_y_right / tan(roll_rad))
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
                blue_top_right = x_hoz_right, 2
                brown_bottom_extra = 2, 2

        elif roll > 45 and roll < 90:
            blue_top_right = -2, 2
            blue_top_left = -2, 2
            blue_top_extra = -2, -2
            brown_bottom_extra = 2, 2
            brown_bottom_right = 2, -2
            brown_bottom_left = 2, -2

            x_hoz_right = (y_max / tan(roll_rad)) - diff_x
            x_hoz_left = (-y_max / tan(roll_rad)) - diff_x

            over_x_right = x_hoz_right - 2.0
            under_x_left = x_hoz_left + 2.0

            if x_hoz_right >= 2.0:
                x_hoz_right = 2.0
                y_hoz_right = x_max - (over_x_right * tan(roll_rad))
                if y_hoz_right <= -2.0:
                    y_hoz_right = -2.0
                blue_top_right = 2, 2
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
            if x_hoz_left >= 2.0:
                x_hoz_left = 2.0
            if x_hoz_right <= -2.0:
                x_hoz_right = -2.0
            if x_hoz_left <= -2.0:
                x_hoz_left = -2.0
                y_hoz_left = -y_max - (under_x_left * tan(roll_rad))
                if y_hoz_left >= 2.0:
                    y_hoz_left = 2.0
                brown_bottom_left = -2, -2

    elif sector == 1:
        if roll >= 0 and roll <= 45:
            blue_top_right = -2, 2
            blue_top_left = -2, -2
            blue_top_extra = -2, -2
            brown_bottom_extra = 2, 2
            brown_bottom_right = 2, 2
            brown_bottom_left = 2, -2

            x_hoz_left = (y_max * tan(roll_rad)) - diff_x
            x_hoz_right = (-y_max * tan(roll_rad)) - diff_x

            over_x_right = x_hoz_right + 2.0
            under_x_left = x_hoz_left - 2.0

            if x_hoz_left >= 2.0:
                x_hoz_left = 2.0
                if roll != 0:
                    y_hoz_left = -(y_max - (under_x_left / tan(roll_rad)))
                if y_hoz_left <= -2.0:
                    y_hoz_left = -2.0
                brown_bottom_left = 2, 2
                blue_top_extra = 2, -2

            if x_hoz_right >= 2.0:
                x_hoz_right = 2.0

            if x_hoz_right <= -2.0:
                x_hoz_right = -2.0
                if roll != 0:
                    y_hoz_right = -(-y_max - (over_x_right /
                                    tan(roll_rad)))
                if y_hoz_right <= -2.0:
                    y_hoz_right = -2.0

                blue_top_right = -2, -2
                brown_bottom_extra = -2, 2

            if y_hoz_left >= 2.0:
                y_hoz_left = 2.0

        elif roll > 45 and roll < 90:
            blue_top_right = 2, -2
            blue_top_left = -2, -2
            blue_top_extra = -2, -2
            brown_bottom_extra = 2, 2
            brown_bottom_right = 2, 2
            brown_bottom_left = -2, 2

            y_hoz_left = (x_max / tan(roll_rad)) - diff_y
            y_hoz_right = (-x_max / tan(roll_rad)) - diff_y
            over_y_left = y_hoz_left - 2.0
            under_y_right = y_hoz_right + 2.0

            if y_hoz_left >= 2.0:
                y_hoz_left = 2.0
                x_hoz_left = -x_max + (over_y_left * tan(roll_rad))
                if x_hoz_left >= 2.0:
                    x_hoz_left = 2.0
                brown_bottom_left = x_hoz_left, 2
                blue_top_extra = -2, 2

            if y_hoz_right >= 2.0:
                y_hoz_right = 2.0
            if y_hoz_right <= -2.0:
                y_hoz_right = -2.0
                x_hoz_right = x_max + (under_y_right * tan(roll_rad))
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
                brown_bottom_extra = 2, -2
                blue_top_right = x_hoz_right, -2
            if y_hoz_left <= -2.0:
                y_hoz_left = -2.0

    elif sector == 2:
        if roll >= 0 and roll <= 45:
            blue_top_right = 2, -2
            blue_top_left = 2, -2
            blue_top_extra = -2, -2
            brown_bottom_right = 2, 2
            brown_bottom_left = -2, 2
            brown_bottom_extra = 2, 2

            y_hoz_left = (-x_max * tan(roll_rad)) - diff_y
            y_hoz_right = (x_max * tan(roll_rad)) - diff_y
            over_y_right = y_hoz_right - 2.0
            under_y_left = y_hoz_left + 2.0

            if y_hoz_left <= -2.0:
                y_hoz_left = -2.0
                if roll != 0:
                    x_hoz_left = -(y_max + (under_y_left /
                                   tan(roll_rad)))
                if x_hoz_left >= 2.0:
                    x_hoz_left = 2.0
                brown_bottom_left = -2, -2
                brown_bottom_right = -2, 2

            if y_hoz_right <= -2.0:
                y_hoz_right = -2.0

            if y_hoz_right >= 2.0:
                y_hoz_right = 2.0
                if roll != 0:
                    x_hoz_right = -(-y_max + (over_y_right /
                                    tan(roll_rad)))
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
                blue_top_right = 2, 2

            if y_hoz_left >= 2.0:
                y_hoz_left = 2.0

        elif roll > 45 and roll < 90:
            blue_top_right = 2, 2
            blue_top_left = 2, -2
            blue_top_extra = 2, -2
            brown_bottom_extra = -2, 2
            brown_bottom_right = -2, 2
            brown_bottom_left = -2, -2

            x_hoz_left = (-y_max / tan(roll_rad)) - diff_x
            x_hoz_right = (y_max / tan(roll_rad)) - diff_x

            over_x_right = x_hoz_right - 2.0
            under_x_left = x_hoz_left + 2.0

            if x_hoz_left <= -2.0:
                x_hoz_left = -2.0
                y_hoz_left = -y_max - (under_x_left * tan(roll_rad))
                if y_hoz_left >= 2.0:
                    y_hoz_left = 2.0
                brown_bottom_left = -2, y_hoz_left
                blue_top_extra = -2, -2

            if x_hoz_right <= -2.0:
                x_hoz_right = -2.0

            if x_hoz_right >= 2.0:
                x_hoz_right = 2.0
                y_hoz_right = x_max - (over_x_right * tan(roll_rad))
                if y_hoz_right <= -2.0:
                    y_hoz_right = -2.0
                blue_top_right = 2, -2
                brown_bottom_extra = 2, 2

            if x_hoz_left >= 2.0:
                x_hoz_left = 2.0

    elif sector == 3:
        if roll >= 0 and roll <= 45:
            blue_top_right = 2, -2
            blue_top_left = 2, 2
            blue_top_extra = 2, 2
            brown_bottom_extra = -2, -2
            brown_bottom_right = -2, -2
            brown_bottom_left = -2, 2
            y_hoz_right = -y_hoz_right
            y_hoz_left = -y_hoz_left

            x_hoz_left = (-y_max * tan(roll_rad)) - diff_x
            x_hoz_right = (y_max * tan(roll_rad)) - diff_x

            over_x_right = x_hoz_right - 2.0
            under_x_left = x_hoz_left + 2.0

            if x_hoz_left <= -2.0:
                x_hoz_left = -2.0
                if roll != 0:
                    y_hoz_left = -(-y_max - (under_x_left /
                                   tan(roll_rad)))
                if y_hoz_left <= -2.0:
                    y_hoz_left = -2.0
                brown_bottom_left = -2, -y_hoz_left
                blue_top_extra = -2, 2

            if x_hoz_right <= -2.0:
                x_hoz_right = -2.0

            if x_hoz_right >= 2.0:
                x_hoz_right = 2.0
                if roll != 0:
                    y_hoz_right = -(x_max - (over_x_right /
                                    tan(roll_rad)))
                if y_hoz_right >= 2.0:
                    y_hoz_right = 2.0
                blue_top_right = 2, 2
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
                brown_bottom_extra = 2, -2

            if x_hoz_left >= 2.0:
                x_hoz_left = 2.0

        elif roll > 45 and roll < 90:
            blue_top_right = 2, 2
            blue_top_left = -2, 2
            blue_top_extra = -2, 2
            brown_bottom_extra = 2, -2
            brown_bottom_right = 2, -2
            brown_bottom_left = -2, -2

            y_hoz_left = (x_max / tan(roll_rad)) - diff_y
            y_hoz_right = (-x_max / tan(roll_rad)) - diff_y
            over_y_left = y_hoz_left - 2.0
            under_y_right = y_hoz_right + 2.0

            if y_hoz_left >= 2.0:
                y_hoz_left = 2.0
                x_hoz_left = -x_max + (over_y_left * tan(roll_rad))
                if x_hoz_left >= 2.0:
                    x_hoz_left = 2.0
                brown_bottom_left = -2, 2
                brown_bottom_right = -2, -2
            if y_hoz_right >= 2.0:
                y_hoz_right = 2.0
            if y_hoz_right <= -2.0:
                y_hoz_right = -2.0
                x_hoz_right = x_max + (under_y_right * tan(roll_rad))
                if x_hoz_right <= -2.0:
                    x_hoz_right = -2.0
                blue_top_right = 2, -2
                blue_top_left = 2, 2
            if y_hoz_left <= -2.0:
                y_hoz_left = -2.0

    hoz_right = x_hoz_right, y_hoz_right
    hoz_left = x_hoz_left, y_hoz_left

    return(blue_top_left, blue_top_extra, blue_top_right,
           hoz_left, hoz_right,
           brown_bottom_left, brown_bottom_extra, brown_bottom_right)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)


def display():
    global roll
    global pitch

    if(roll >= 360.0):
        roll = roll - 360.0
    elif(roll < 0):
        roll = 359.5

    if(pitch > 90.0):
        if roll < 180:
            roll = roll + 180.0
        else:
            roll = roll - 180.0
        pitch = 89.5
    elif(pitch < -90.0):
        if roll < 180:
            roll = roll + 180.0
        else:
            roll = roll - 180.0
        pitch = -89.5

    print(pitch, roll)

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
    # Airplane Reference Line
    glRectf(0.02, 0.02, -0.02, -0.02)
    glRectf(1.0, 0.01, 0.25, -0.01)
    glRectf(-0.25, 0.01, -1.0, -0.01)

    # Start of background scene
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

    glRotatef(-roll, 0.0, 0.0, 1.0)

    points = box_cal(roll, pitch_angle)
    # 0-blue_top_left, 1-blue_top_extra, 2-blue_top_right,
    # 3-hoz_left, 4-hoz_right,
    # 5-brown_bottom_left, 6-brown_bottom_extra 7-brown_bottom_right

    print(points)

    # Sky Box
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(points[3][0], points[3][1])
    glVertex2f(points[1][0], points[1][1])
    glVertex2f(points[0][0], points[0][1])
    glVertex2f(points[2][0], points[2][1])
    glVertex2f(points[4][0], points[4][1])
    glEnd()

    # Ground Box
    glColor3f(0.5, 0.35, 0.05)
    glBegin(GL_POLYGON)
    glVertex2f(points[5][0], points[5][1])
    glVertex2f(points[3][0], points[3][1])
    glVertex2f(points[4][0], points[4][1])
    glVertex2f(points[6][0], points[6][1])
    glVertex2f(points[7][0], points[7][1])
    glEnd()

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
