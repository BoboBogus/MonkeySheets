from tkinter import*
from Cell import Cell

root = Tk()
for x in range(0, 5):
    for y in range(0, 5):
        c = Cell(x,y,1,1,1,1)
        c.createEntry(root)
        c.entry.grid(column = x, row = y)
        print(c.entry.get())

btn = Button(root, command = lambda:entryCheck())
btn.grid(column = 0, row =6)
def entryCheck():
    print(Cell.all)
    for x in range(0, 5):
        for y in range(0, 5):
            c = Cell.get_cell_by_axis(Cell, x,y)
            print(c)
            print(c.entry.get())
root.mainloop()