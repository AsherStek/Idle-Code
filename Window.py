import tkinter as tk

class GameWindow:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        self.root.resizable(0,0)
        self.root.focus_set()

        self.cans = {}

    def createCan(self, width, height, row, col, rspan, cspan, scale, bg, id, stick=None):
        self.cans[id] = [
            tk.Canvas(self.root, width=width, height=height, bg=bg), 
            row, 
            col, 
            rspan, 
            cspan, 
            scale, 
            stick,
            id
            ]
    
    def positionCans(self):
        ids = self.cans.keys()
        for id in ids:
            if self.cans[id][6] != None:
                print("Stickied")
                self.cans[id][0].grid(row=self.cans[id][1],
                column=self.cans[id][2], 
                rowspan=self.cans[id][3],
                columnspan=self.cans[id][4],
                sticky=(self.cans[id][6]))
            else:
                print("Not Stickied")
                self.cans[id][0].grid(row=self.cans[id][1], 
                column=self.cans[id][2],
                rowspan=self.cans[id][3],
                columnspan=self.cans[id][4])

    def disableCan(self, id):
        self.cans[id][0].config(state="disabled")

    def enabledCan(self, id):
        self.cans[id][0].config(state="enabled")

    def getCan(self, id):
        return self.cans[id]

    def Update(self):
        self.root.update()

    def bindKey(self, key, command, id):
        self.cans[id][0].bind(key, command)

    def getMousePos(self):
        return (self.root.winfo_pointerx(), self.root.winfo_pointery())
