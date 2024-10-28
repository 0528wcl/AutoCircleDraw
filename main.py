from keyboard import is_pressed
from pyautogui import size, moveTo, mouseDown, mouseUp
from numpy import linspace, cos, sin, pi

a = 4
radius = 250

# Creating equally spaced data in range 0 to 2*pi
theta = linspace(0, 2 * pi, a)
x = radius * cos(theta)
y = radius * sin(theta)

resolutionX, resolutionY = size()
moveToX = resolutionX / 2
moveToY = resolutionY / 2 - 20

positions = [(moveToX + x[i], moveToY + y[i]) for i in range(a)]

print("사용법: 브라우저에서 F11 또는 전체화면을 키고 작동시키세요!!\nQ키를 눌러서 작동시키세요!!!!\nInstructions: Go into fullscreen mode on your browser\nPress 'Q' to activate")

try:
    while True:
        if is_pressed("q"):
            moveTo(*positions[0])
            mouseDown(button="left")

            for i in range(1, a):
                moveTo(*positions[i])

            mouseUp(button="left")
            break

except KeyboardInterrupt:
    print("Execution stopped by user.")