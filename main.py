from tkinter import*
from tkinter import filedialog
from Cell import Cell
from cellLabel import cellLabel
import settings
import utils


             
def UpdateWindow():
    global root
    global TopFrameHPerc
    global RowFrameThickness
    global ColumnFrameThickness
    global WindowHeight
    global WindowWidth 
    global TopFrame
    global RowFrame
    global ColumnFrame
    global MainFrame
    global menubar
    global filemenu
    global CellsX
    global CellsY
    global CellTX
    global CellTY
    global WindowX
    global WindowY
    global WindowTX
    global WindowTY
    global TitleEntry
    global TitleT

    
    root = Tk()
    try:
        root.title(TitleName)
    except:
        pass
    root.iconphoto(False, PhotoImage(file='images/icon.png'))
    root.configure(background = settings.secondaryColor)
    TopFrameHPerc = settings.TopFrameHeight
    RowFrameThickness = settings.RowFrameThickness
    ColumnFrameThickness = settings.ColumnFrameThickness

    WindowHeight = settings.SCREENHEIGHT
    WindowWidth = settings.SCREENWIDTH

    root.configure(width = WindowWidth, height = WindowHeight + 15)
    TopFrame = Frame(root, bg = settings.secondaryColor, background = settings.secondaryColor, highlightthickness= 1, highlightbackground = settings.thirdColor, highlightcolor= settings.thirdColor)
    TopFrame.place(x=0,y=0, width = utils.widthPercentCalc(100), height = utils.heightPercentCalc(TopFrameHPerc))

    RowFrame = Frame (root, width= WindowWidth, height = utils.heightPercentCalc(RowFrameThickness),  bg = settings.fourthColor)
    RowFrame.place(x=0,y=utils.heightPercentCalc(TopFrameHPerc))
    ColumnFrame = Frame(root, width = utils.widthPercentCalc(ColumnFrameThickness), height = utils.heightPercentCalc(100 - TopFrameHPerc- RowFrameThickness), bg = settings.fourthColor)
    ColumnFrame.place(x=0, y = utils.heightPercentCalc(TopFrameHPerc + RowFrameThickness))

    MainFrame = Frame(root, width = utils.widthPercentCalc(100 - ColumnFrameThickness), height = utils.heightPercentCalc(100 - TopFrameHPerc - RowFrameThickness), bg = settings.mainColor, background = settings.mainColor, highlightthickness= 1, highlightbackground = settings.thirdColor, highlightcolor= settings.thirdColor)
    MainFrame.place(x=utils.widthPercentCalc(ColumnFrameThickness),y=utils.heightPercentCalc(TopFrameHPerc + RowFrameThickness))
    

    def ExportFile():
        FilePath = filedialog.asksaveasfilename(initialfile = (f"{TitleName}.txt"),defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        file = open(FilePath, "a")
        file.truncate(0)
        Row1 = []
        Row2 = []
        for x in range(0,settings.cellX):
            for y in range(0,settings.cellY):
                if x == 0 and y != 0:
                    c = Cell.get_cell_by_axis(Cell, x, y)
                    if c.entry.get() == '':
                        Row1.append("NULL")
                    else:
                        Row1.append(c.entry.get())

                if y == 0 and x != 0:
                    c = Cell.get_cell_by_axis(Cell, x, y)
                    if c.entry.get() == '':
                        Row2.append("NULL")
                    else:
                        Row2.append(c.entry.get())

        for x in range(0,settings.cellX):
            for y in range(0,settings.cellY):
                a = Cell.get_cell_by_axis(Cell, x, y)
                
                if a.entry.get() == "":
                    data = "NULL"
                else:
                    data = a.entry.get()
                packData(Row1, Row2, x, y, data, file)

    def packData(Row1, Row2, x, y, data, file):
        item = (f"{Row2[x-1]}, {Row1[y-1]} = {data}")
        print(item)
        file.write(f"{item} \n")

    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label = "Export As", command = ExportFile)
    filemenu.add_command(label="New", command = lambda: UIUpdate(CellsX, CellsY, WindowX, WindowY, TitleEntry))
    filemenu.add_separator()
    filemenu.add_command(label="Close", command = root.destroy)

    CellsX = Entry(TopFrame, bg = settings.secondaryColor, fg = settings.fontColor, width = 10)
    CellsX.grid(column = 0,row =0)
    CellsY = Entry(TopFrame, bg = settings.secondaryColor, fg = settings.fontColor, width = 10)
    CellsY.grid(column = 1, row = 0)

    CellTX = Label(TopFrame, bg = settings.secondaryColor, text = "Amount of cells for Column", fg = settings.fontColor, font=("Eccentric Std", 6))
    CellTX.grid(column = 0,row = 1)
    CellTY = Label(TopFrame, bg = settings.secondaryColor, text = "Amount of cells for Row", fg = settings.fontColor, font=("Eccentric Std", 6))
    CellTY.grid(column = 1, row = 1)


    WindowX = Entry(TopFrame, bg = settings.secondaryColor, fg = settings.fontColor, width = 10)
    WindowX.grid(column = 2,row =0)
    WindowY = Entry(TopFrame, bg = settings.secondaryColor, fg = settings.fontColor, width = 10)
    WindowY.grid(column = 3, row = 0)

    WindowTX = Label(TopFrame, bg = settings.secondaryColor, text = "Width of the Window in Pixels", fg = settings.fontColor, font=("Eccentric Std", 6))
    WindowTX.grid(column = 2,row = 1)
    WindowTY = Label(TopFrame, bg = settings.secondaryColor, text = "Height of the Window in Pixels", fg = settings.fontColor, font=("Eccentric Std", 6))
    WindowTY.grid(column = 3, row = 1)

    TitleEntry= Entry(TopFrame, bg = settings.secondaryColor, fg = settings.fontColor, width = 10)
    TitleEntry.grid(column = 4, row = 0)

    TitleT = Label(TopFrame, bg = settings.secondaryColor, text = "Enter Name", fg = settings.fontColor, font=("Eccentric Std", 6))
    TitleT.grid(column = 4, row = 1)
    def UIUpdate(CellsX, CellsY, WindowX, WindowY, TitleEntry):
        global TitleName
        numX = CellsX.get()
        numY = CellsY.get()
        WinHX = WindowX.get()
        WinHY = WindowY.get()
        TitleName = TitleEntry.get()

        numX = int(numX)
        numY = int(numY)
        WinHX = int(WinHX)
        WinHY = int(WinHY)
        settings.SCREENWIDTH = WinHX
        settings.SCREENHEIGHT = WinHY
        settings.cellX = numY
        settings.cellY = numY
        root.destroy()
        UpdateWindow()
        MainUI()

def MainUI():
        settings.StartCellWidth = (WindowWidth-utils.widthPercentCalc(ColumnFrameThickness))/settings.cellX
        settings.StartCellHeight =  utils.heightPercentCalc(100-TopFrameHPerc- RowFrameThickness)/settings.cellY
        PositionXmult = (WindowWidth-utils.widthPercentCalc(ColumnFrameThickness))/settings.cellX
        PositionYmult = utils.heightPercentCalc(100-TopFrameHPerc - RowFrameThickness)/settings.cellY
    #only for labels
        for y in range(0,settings.cellY):
            e = cellLabel(y, False, PosY = y * PositionYmult, PosX = 0, cellWidth = utils.widthPercentCalc(ColumnFrameThickness), cellHeight = utils.heightPercentCalc(100-TopFrameHPerc- RowFrameThickness)/settings.cellY)
            e.createEntry(ColumnFrame)
            e.entry.place(x=e.PosX, y=e.PosY, width = utils.widthPercentCalc(ColumnFrameThickness), height = e.cellHeight)

        for x in range(0,settings.cellX):
            #only for labels
            b = cellLabel(x, True, PosX = (utils.widthPercentCalc(ColumnFrameThickness) + (x * PositionXmult)), PosY = 0, cellHeight =utils.heightPercentCalc(RowFrameThickness), cellWidth = (WindowWidth-utils.widthPercentCalc(ColumnFrameThickness))/settings.cellX)
            b.createEntry(RowFrame)
            b.entry.place( x=b.PosX, y=b.PosY, width = b.cellWidth, height = b.cellHeight)

            #for cells in order to create 2d array
            for y in range(0,settings.cellY):
                c = Cell(x,y, PosX = x*PositionXmult, PosY = y*PositionYmult, cellHeight = utils.heightPercentCalc(100-TopFrameHPerc- RowFrameThickness)/settings.cellY, cellWidth = (WindowWidth-utils.widthPercentCalc(ColumnFrameThickness))/settings.cellX)
                c.createEntry(MainFrame)
                c.entry.place(width=c.cellWidth, height=c.cellHeight, x= c.PosX, y= c.PosY )
                #if x == 0:
                #    c = Cell.get_cell_by_axis(Cell, x, y)
                #    c.entry.configure(bg = settings.secondaryColor)
                #if y == 0:
                #    c = Cell.get_cell_by_axis(Cell, x, y)
                #    c.entry.configure(bg = settings.secondaryColor)
    #

UpdateWindow()
root.mainloop()