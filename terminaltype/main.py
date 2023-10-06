import curses
from curses import wrapper
from terminal_type import TerminalType


def main(win):
    curses.start_color()
    curses.curs_set(0)
    terminal_type = TerminalType(win)
    terminal_type.menu()

if __name__ == '__main__':
    wrapper(main)
