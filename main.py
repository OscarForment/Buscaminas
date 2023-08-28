from tkinter import *
from cell import Cell
import settings
import utils



root = Tk()
# Ajustes de la ventana
root.configure(bg="Black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Buscaminas')
root.resizable(False, False)
# Crea la barra de arriba
top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utils.height_prct(20)
)
top_frame.place(x=0, y=0)
# Crea la zona central donde ira el juego
center_frame = Frame(
    root,
    bg='green',
    width=settings.WIDTH,
    height=utils.height_prct(80)
)
center_frame.place(x=0,y=utils.height_prct(20))
# Asumimos que la cuadricula será un cuadrado de un tamaño preestablecido
w = int((center_frame.winfo_reqwidth()/settings.GRID_SIZE)/7.5)
h = int((center_frame.winfo_reqheight()/settings.GRID_SIZE)/17)

for i in range(settings.GRID_SIZE):
    for j in range(settings.GRID_SIZE):
        c = Cell(i, j)
        c.create_btn_obj(center_frame, w, h)
        c.cell_btn_obj.grid(column=i, row=j)
Cell.randomize_mines()
# Abre la ventana
root.mainloop()