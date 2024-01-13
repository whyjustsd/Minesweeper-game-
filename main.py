from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
root.configure(bg= "black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("MineSwepper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = "black",
    width = settings.WIDTH,
    height = utils.height_prct(25)
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text= 'Minesweeper game',
    font=('',48)

)
game_title.place(
    x= utils.width_prct(25),y=0
)

left_frame = Frame(
    root,
    bg = "black",
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25) )

center_frame = Frame(
    root,
    bg = "black",
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)
center_frame.place(
    x= utils.width_prct(25),
    y = utils.height_prct(25),
)
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row =y
        )


Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,y=0
)

Cell.randomize_mines()
print(Cell,all)
root.mainloop()
