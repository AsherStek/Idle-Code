import Window
import math as m

w = 1280
h = 640
t = "IDLE CODE"
scale = 32

def click(e):
    print(f"Clicked Canvas: {win.getCan(ids[0])[7]} at X: {win.getMousePos()[0]} Y: {win.getMousePos()[1]}")

ids = [
    "Click Area", # 0
    "Upgrade Area", # 1
    "Console Area" # 2
]

keys = [
    '<Button-1>' # Mouse Click
]

commands = [
    click
]

win = Window.GameWindow(w, h, t)
win.createCan(m.floor(w/1.341), h-160, 0, 5, 6, 5, scale, 'blue', ids[0], 'N' + 'W')
win.createCan(m.floor(w/4), h, 0, 0, 10, 4, scale, 'white', ids[1], 'W')
win.createCan(m.floor(w/1.341), 160, 7, 5, 3, 5, scale, 'black', ids[2], 'S' + 'W')
win.positionCans()
win.bindKey(keys[0], lambda e : commands[0](e), ids[0])

while True:
    win.Update()

