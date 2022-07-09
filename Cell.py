from tkinter import Entry
import settings
class Cell:
    all = []
    def __init__(self, x,y, PosX, PosY, cellHeight, cellWidth):
            self.entry = None
            self.x = x
            self.y = y
            self.PosX = PosX
            self.PosY = PosY
            self.cellHeight = cellHeight
            self.cellWidth = cellWidth
            Cell.all.append(self)
    
    def createEntry(self , location):
        ent = Entry(
            location,
            bg = settings.mainColor,
            fg = settings.fontColor,
            font=("Eccentric Std", 6)
        )
        self.entry = ent

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    def __repr__(self):
        return (f"Cell at {self.x}, {self.y}")