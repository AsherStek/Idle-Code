import Window
import math as m

w = 1280
h = 640
t = "IDLE CODE"
scale = 32

def click():
    print(f"Clicked Canvas: {ids[0]} at X: {win.getMousePos()[0]} Y: {win.getMousePos()[1]}")

ids = [
    "Click Area",
    "Upgrade Area"
]

keys = [
    '<Button-1>'
]

commands = [
    click
]

win = Window.GameWindow(w, h, t)
win.createCan(m.floor(w/1.25), h, 0, 1, scale, 'grey80', ids[0])
win.createCan(m.floor(w/2.75), h, 0, 0, scale, 'white', ids[1])
win.positionCans()
win.bindKey(keys[0], lambda e=win.getCan(ids[0])[0]: commands[0](), ids[0])

while True:
    win.Update()

