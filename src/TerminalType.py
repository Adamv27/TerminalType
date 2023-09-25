import time
import curses
from curses import wrapper


class TerminalType:
    def __init__(self, win: curses.window):
        self.win = win
        self.win_x, self.win_y = self.win.getmaxyx()
        self.test_length = 15
    

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
    terminalType.typing_test()


if __name__ == '__main__':
    wrapper(main)
