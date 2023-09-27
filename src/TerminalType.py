import time
import curses
from curses import wrapper
from Settings import Settings


class TerminalType:
    def __init__(self, win: curses.window):
        self.win = win
        self.win_x, self.win_y = self.win.getmaxyx()
        self.test_length = 15
    
    def menu(self):
        self.win.clear()        
        self.settings = Settings(self.win) 
        self.win.move(0, 0) 
        while True:
            key = self.win.getkey()
            
            if key == 'KEY_RIGHT':
                self.settings.move_right()
            elif key == 'KEY_LEFT':
                self.settings.move_left()

        self.win.getch()


    def typing_test(self):
        self.win.clear()
        
        self.win.addstr(0, 0, 'Characters')
        
        self.win.addstr(0, len('characters') + 1, 'Test type')
        self.win.refresh()

        selected = False
        while True:
            key = self.win.getkey()
            
            if key == '\n':
                selected = not selected                
                highlight = curses.A_DIM if selected else curses.A_NORMAL
                self.win.addstr(0, 0, 'Characters', highlight)

            elif key == 'q':
                break
            self.win.refresh() 

        self.win.getch()


def main(win):
    curses.start_color()
    terminalType = TerminalType(win)
    terminalType.menu()


if __name__ == '__main__':
    wrapper(main)
