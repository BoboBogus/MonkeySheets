import settings
from tkinter import Button
from Cell import Cell

InitializeClick = 0
class cellLabel:
    all = []
    def __init__(self, num, iscolumn, PosX, PosY,cellHeight, cellWidth):
            self.entry = None
            self.num = num
            self.iscolumn = iscolumn
            self.PosX = PosX
            self.PosY = PosY
            self.cellHeight = cellHeight
            self.cellWidth = cellWidth


            cellLabel.all.append(self)

    def createEntry(self , location):
        ent = Button(
            location,
            bg = settings.fourthColor,
            fg = settings.fontColor,
            font=("Time New Roman", 6),
            text = self.num + 1,
            command = lambda : cellLabel.ResetSize(self)
        )
        self.entry = ent
        ent.bind("<MouseWheel>", lambda event:  cellLabel.rescale(event, self))
    
    def get_celllabel_by_axis(self, num, iscolumn):
        for label in cellLabel.all:
            if label.iscolumn == iscolumn:
                if label.num == num:
                    return label
        
#prob error here!!!!!!!!!!!!!!!!
#tkinter mouse pos is based on the frame which is on
    def rescale(event, self):
        x = 0
        index = self.num
        
        if self.iscolumn:
            if event.num == 5 or event.delta == -120:
                x = self.cellWidth - settings.CellResizeMult
            if event.num == 4 or event.delta == 120:
                x = self.cellWidth + settings.CellResizeMult
            if x > settings.minimumCellThickness:
                cellLabel.rescaleCellColumn(index, x)
        else:
            if event.num == 5 or event.delta == -120:
                x = self.cellHeight - settings.CellResizeMult
            if event.num == 4 or event.delta == 120:
                x = self.cellHeight + settings.CellResizeMult
            if x > settings.minimumCellThickness:
                cellLabel.rescaleCellRow(index, x)

    
    def ResetSize(self):
        index = self.num
        if self.iscolumn:
            x = settings.StartCellWidth
            cellLabel.rescaleCellColumn(index, x)
        else:
            x = settings.StartCellHeight
            cellLabel.rescaleCellRow(index, x)
        


    def rescaleCellRow(Y, height):
        mainCellHeight = 0
        isBigger = None
        for x in range(0,settings.cellX):
            for y in range(0, settings.cellY):
                if y == Y:
                    c = Cell.get_cell_by_axis(Cell, x, y)
                    if c.cellHeight <= height:
                        isBigger = True
                    else:
                        isBigger = False
    
        for x in range(0,settings.cellX):
            for y in range(0, settings.cellY):
                if y == Y:
                    c = Cell.get_cell_by_axis(Cell, x,y)
                    #issue
                    mainCellHeight = c.cellHeight
                    c.entry.place(height = height, y = c.PosY)
                    c.cellHeight = height
                    
                else:
                    if y > Y:
                        a = Cell.get_cell_by_axis(Cell, x,y)
                        if isBigger:
                            a.PosY = a.PosY + (height - mainCellHeight)
                        else:
                            a.PosY = a.PosY - (mainCellHeight - height)
                        a.entry.place(y = a.PosY)
        #for label
        for y in range(0, settings.cellY):
                if y == Y:
                    e = cellLabel.get_celllabel_by_axis(Cell, y, False)
                    mainCellHeight = e.cellHeight
                    e.entry.place(height = height, y = e.PosY)
                    e.cellHeight = height
                else:
                    if y > Y:
                        e = cellLabel.get_celllabel_by_axis(Cell, y, False)
                        if isBigger:
                            e.PosY = e.PosY + (height - mainCellHeight)
                        else:
                            e.PosY = e.PosY - (mainCellHeight - height)
                        e.entry.place(y = e.PosY)


    def rescaleCellColumn(X, width):
        mainCellWidth = 0
        isBigger = None
        for x in range(0,settings.cellX):
            for y in range(0, settings.cellY):
                if x == X:
                    c = Cell.get_cell_by_axis(Cell, x, y)
                    if c.cellWidth >= width:
                        isBigger = True
                    else:
                        isBigger = False
                        
        for x in range(0,settings.cellX):
            for y in range(0, settings.cellY):
                #size change in index
                if x == X:
                    c = Cell.get_cell_by_axis(Cell, x,y)
                    mainCellWidth = c.cellWidth
                    c.entry.place(width = width, x = c.PosX)
                    c.cellWidth = width
                else:
                    if x > X:
                        #position change 
                        a = Cell.get_cell_by_axis(Cell, x,y)
                        if isBigger:
                            a.PosX = a.PosX + (width - mainCellWidth)
                        else:
                            a.PosX = a.PosX - (mainCellWidth - width)
                        a.entry.place(x = a.PosX)
        #for label
        for x in range(0, settings.cellX):
                #size change in index
                if x == X:
                    b = cellLabel.get_celllabel_by_axis(Cell, x, True)
                    mainCellWidth = b.cellWidth
                    b.entry.place(width = width, x = b.PosX)
                    b.cellWidth = width
                #position change
                else:
                    if x > X:
                        b = cellLabel.get_celllabel_by_axis(Cell, x, True)
                        if isBigger:
                            b.PosX = b.PosX + (width - mainCellWidth)
                        else:
                            b.PosX = b.PosX - (mainCellWidth - width)
                        b.entry.place(x = b.PosX)
                        
    def __repr__(self):
        return (f"label {self.num} {self.iscolumn} width is {self.cellWidth} height is {self.cellHeight}")