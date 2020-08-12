import random
import sys
import threading
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import games
import solver

slp_time = 0.25
# initgame = random.choice(games.all)
initgame = games.vhard1


def set_pallete(App):
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    App.setPalette(palette)


def set_xvals(num):
    if num <= 2:
        xvals = [0, 1, 2]
    elif num <= 5:
        xvals = [3, 4, 5]
    else:
        xvals = [6, 7, 8]
    return xvals


def set_yvals(num):
    if num % 3 == 0:
        xvals = [0, 1, 2]
    elif num % 3 == 1:
        xvals = [3, 4, 5]
    else:
        xvals = [6, 7, 8]
    return xvals


def get_box_cell(xvals, yvals, num):
    x = num // 3
    y = num % 3
    return xvals[x], yvals[y]


class ApplicationWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Sudoku Solver'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.main_widget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.main_widget)

        self.grid_plot = PlotCanvas(self.main_widget)
        self.grid_plot.initPlot()

        self.overlay_plot = PlotCanvas(self.grid_plot)
        self.overlay_plot.initOverlay()
        self.overlay_plot.setStyleSheet("background-color:transparent;")
        self.overlay_plot.draw()

        self.btn_layout = QtWidgets.QHBoxLayout()
        self.veasy_btn = QtWidgets.QPushButton('Very Easy')
        self.veasy_btn.clicked.connect(lambda: self.grid_plot.update_grid(games.breezy))

        self.easy_btn = QtWidgets.QPushButton('Easy')
        self.easy_btn.clicked.connect(lambda: self.grid_plot.update_grid(games.easy))

        self.medium_btn = QtWidgets.QPushButton('Medium')
        self.medium_btn.clicked.connect(lambda: self.grid_plot.update_grid(games.medium))

        self.hard_btn = QtWidgets.QPushButton('Hard')
        self.hard_btn.clicked.connect(lambda: self.grid_plot.update_grid(games.hard))

        self.vhard_btn = QtWidgets.QPushButton('Very Hard')
        self.vhard_btn.clicked.connect(lambda: self.grid_plot.update_grid(games.vhard))

        self.btn_layout.addWidget(self.veasy_btn)
        self.btn_layout.addWidget(self.easy_btn)
        self.btn_layout.addWidget(self.medium_btn)
        self.btn_layout.addWidget(self.hard_btn)
        self.btn_layout.addWidget(self.vhard_btn)

        self.layout.addLayout(self.btn_layout)
        self.layout.addWidget(self.grid_plot)
        self.solve_btn = QtWidgets.QPushButton('Solve')
        self.solve_btn.clicked.connect(self.beginSolve)
        self.layout.addWidget(self.solve_btn)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

    def visualSolve(self):
        self.grid_plot.grid.initialise_solve()
        for i in range(100):
            list_type, list_num, indx, num = self.grid_plot.grid.return_solve()
            if list_type is False:
                break
            print(f'Set {list_type}{list_num} cell{indx} to {num}')
            self.grid_plot.visualListSet(list_type, list_num, indx, num)
            time.sleep(slp_time)
            self.grid_plot.visualCellSet(list_type, list_num, indx, num)
            time.sleep(slp_time)
            self.grid_plot.clearColours()
        print('PUZZLE SOLVED!')

    def beginSolve(self):
        t = threading.Thread(target=self.visualSolve)
        t.start()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), facecolor='none', dpi=dpi, tight_layout=True)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def initPlot(self):

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        update_time = int(slp_time * 1000 / 3)
        timer.start(update_time)

        self.grid = solver.Grid(initgame)
        self.ax = self.figure.add_subplot()
        self.ax.axis('tight')
        self.ax.axis('off')

        self.cell_text = self.grid.get_all()

        self.visual = self.ax.table(cellText=self.cell_text, cellLoc='center', loc='center')
        self.visual.scale(1.0, 2.0)
        self.set_edges()
        self.draw()

    def initOverlay(self):
        self.ax = self.figure.add_subplot()
        self.ax.axis('tight')
        self.ax.axis('off')
        cell_text = games.blank
        self.visual = self.ax.table(cellText=cell_text, cellLoc='center', loc='center')
        self.visual.scale(1.0, 2.0)

        for x, y in self.visual.get_celld():
            c = self.visual[x, y]
            right_edges = [2, 5, 8]
            top_edges = [0, 3, 6]
            c.set_edgecolor('k')
            c.set_facecolor('none')
            if x in top_edges:
                if y == 0:
                    c.visible_edges = 'TL'
                elif y in right_edges:
                    c.visible_edges = 'TR'
                else:
                    c.visible_edges = 'T'

            elif x == 8:
                if y == 0:
                    c.visible_edges = 'BL'
                elif y in right_edges:
                    c.visible_edges = 'BR'
                else:
                    c.visible_edges = 'B'
            else:
                if y == 0:
                    c.visible_edges = 'L'
                elif y in right_edges:
                    c.visible_edges = 'R'
                else:
                    c.visible_edges = ''
        # self.draw()

    def update_grid(self, difficulty):
        # game_list = exec(f'games.{difficulty}')
        game = random.choice(difficulty)
        # print(game)
        self.grid = solver.Grid(game)
        self.cell_text = self.grid.get_all()
        for x, row in enumerate(game):
            for y, num in enumerate(row):
                self.visualTextSet(x, y, num)

        self.draw()

    def set_edges(self):
        for x, y in self.visual.get_celld():
            c = self.visual[x, y]
            c.set_edgecolor('lightgrey')

    def clearColours(self):
        for x, y in self.visual.get_celld():
            c = self.visual[x, y]
            c.set_facecolor('white')

    def visualListSet(self, list_type, list_num, indx, cell):
        if list_type == 'box':
            xvals = set_xvals(list_num)
            yvals = set_yvals(list_num)
            for x, y in self.visual.get_celld():
                c = self.visual[x, y]
                if x in xvals and y in yvals:
                    c.set_facecolor('lightskyblue')

        elif list_type == 'pencil':
            pass

        else:
            for x, y in self.visual.get_celld():
                c = self.visual[x, y]
                if list_type == 'col':
                    a, b = y, x
                else:
                    a, b = x, y
                if a == list_num:
                    c.set_facecolor('lightskyblue')

    def visualCellSet(self, list_type, list_num, indx, cell):
        if list_type == 'box':
            xvals = set_xvals(list_num)
            yvals = set_yvals(list_num)
            cellvals = get_box_cell(xvals, yvals, indx)
            for x, y in self.visual.get_celld():
                c = self.visual[x, y]
                if x == cellvals[0] and y == cellvals[1]:
                    c.set_facecolor('mediumspringgreen')
                    self.visualTextSet(x, y, cell, delay=slp_time)

        else:
            for x, y in self.visual.get_celld():
                c = self.visual[x, y]
                if list_type == 'col':
                    # or list_type =='pencil':
                    a, b = y, x
                else:
                    a, b = x, y
                if a == list_num and b == indx:
                    c.set_facecolor('mediumspringgreen')
                    self.visualTextSet(x, y, cell, delay=slp_time)

    def visualTextSet(self, x, y, num, delay=0.0):
        time.sleep(delay)
        self.grid.df.iloc[x][y].set_num(num)
        self.visual[x, y].get_text().set_text(num)

    def update_figure(self):

        self.draw()


if __name__ == '__main__':
    App = QtWidgets.QApplication(sys.argv)
    App.setStyle('Fusion')
    set_pallete(App)
    aw = ApplicationWindow()
    aw.show()
    # aw.visualSolve()
    sys.exit(App.exec_())
