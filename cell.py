from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, i, j, is_mine=False):
        self.is_mine = is_mine
        self.i = i
        self.j = j
        self.cell_btn_obj = None

        # Añadir la celda a la lista de celdas
        Cell.all.append(self)

    def create_btn_obj(self,location, w, h):
        btn = Button(
            location,
            width=w,
            height=h,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_mines == 0:
                for cell_o in self.surrounded_cells:
                    cell_o.show_cell()
            self.show_cell()

    def get_cell(self, i , j):
        for cell in Cell.all:
            if cell.i== i and cell.j == j:
                return cell

    @property
    def surrounded_cells(self):
        surr_cells = []
        for i in [self.i-1, self.i, self.i+1]:
            for j in [self.j-1, self.j, self.j+1]:
                surr_cells.append(self.get_cell(i, j))
        surr_cells.remove(self.get_cell(self.i, self.j))
        surr_cells = [cell for cell in surr_cells if cell is not None]
        return surr_cells

    @property
    def surrounded_mines(self,):
        surr_mines = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                surr_mines += 1
        return surr_mines

    def show_cell(self):
        surr_mines = self.surrounded_mines
        if surr_mines != 0:
            self.cell_btn_obj.configure(text=f"{surr_mines}")
        self.cell_btn_obj.configure(bg='gray')

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')

    def right_click_actions(self, event):
        # print(event)
        print('Right')

    @staticmethod
    def randomize_mines():
        mined_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in mined_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.i}. {self.j})"