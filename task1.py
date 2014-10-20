__author__ = 'esenin'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 500
height = width
cube_width = width / 2
left = - cube_width / 2
right = -left
top = cube_width / 2
bottom = -top
near = cube_width / 2
far = near + cube_width / 2

ORTHO_VIEW = 0
FOCUS60_VIEW = 1
FOCUS75_VIEW = 2
FOCUS100_VIEW = 3

output_type = ORTHO_VIEW


def draw_cube_wo_front():
    glColor3f(0, 0, 1)
    glBegin(GL_QUADS)  # right side
    glVertex3f(right, bottom, near)
    glVertex3f(right, bottom, far)
    glVertex3f(right, top, far)
    glVertex3f(right, top, near)
    glEnd()

    glColor3f(0, 0, 0.7)
    glBegin(GL_QUADS)  # left side
    glVertex3f(left, bottom, near)
    glVertex3f(left, bottom, far)
    glVertex3f(left, top, far)
    glVertex3f(left, top, near)
    glEnd()

    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)  # bottom side
    glVertex3f(right, bottom, near)
    glVertex3f(right, bottom, far)
    glVertex3f(left, bottom, far)
    glVertex3f(left, bottom, near)
    glEnd()

    glColor3f(0, 0.7, 0)
    glBegin(GL_QUADS)  # top side
    glVertex3f(right, top, near)
    glVertex3f(right, top, far)
    glVertex3f(left, top, far)
    glVertex3f(left, top, near)
    glEnd()

    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)  # far side
    glVertex3f(right, bottom, far)
    glVertex3f(right, top, far)
    glVertex3f(left, top, far)
    glVertex3f(left, bottom, far)
    glEnd()


def refresh_perspective(p_angle=100):
    glMatrixMode(GL_PROJECTION)
    aspect = width / height
    gluPerspective(p_angle, aspect, near, far)

    eye = (0, 0, 0)
    center = (0, 0, (near + far) / 2)
    cam_up = (0, 1, 0)
    gluLookAt(eye[0], eye[1], eye[2],
              center[0], center[1], center[2],
              cam_up[0], cam_up[1], cam_up[2])


def refresh_ortho():
    glMatrixMode(GL_PROJECTION)
    near_val = 0
    far_val = -2 * width
    glOrtho(- width / 2, width / 2, - width / 2, width / 2, near_val, far_val)


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, width, width)

    if output_type == ORTHO_VIEW:
        refresh_ortho()
    elif output_type == FOCUS60_VIEW:
        refresh_perspective(60)
    elif output_type == FOCUS75_VIEW:
        refresh_perspective(75)
    elif output_type == FOCUS100_VIEW:
        refresh_perspective(100)

    draw_cube_wo_front()

    glutSwapBuffers()


def on_input(key, x, y):
    global output_type
    output_type = (output_type + 1) % (FOCUS100_VIEW + 1)


def make_lighting():
    glLightfv(GL_LIGHT0, GL_POSITION, [width / 3, width / 3, 0, 0])
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def init_open_gl():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, width)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Task 1: draw cube")


def main():
    init_open_gl()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(on_input)
    glutMainLoop()

main()