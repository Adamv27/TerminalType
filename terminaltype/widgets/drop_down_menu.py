import curses
from widgets.widget import Widget 
from widgets import SYMBOLS

class DropDownMenu(Widget):
    def __init__(self, 
                 win,
                 pos,
                 title,
                 options, 
                 can_select_multiple=False):

        super().__init__(win, pos, title)
        self.options = options
        self.can_select_multiple = can_select_multiple
        self.currently_selected_index = 0
        self.expanded = False

    def get_currently_selected(self) -> str:
        return self.options[self.currently_selected_index]

    def expand(self):
        for index, option in enumerate(self.options, start=1):
            symbol = SYMBOLS['toggle-off']
            if option.is_selected:
                symbol = SYMBOLS['toggle-on']

            option_title = f'{symbol}  {option.name}'
            self.win.addstr(self.y + index, self.x, option_title)
        self.move_cursor_to_start()

    def close(self):
        for index in range(1, len(self.options) + 1):
            self.win.move(self.y + index, self.x)
            self.win.clrtoeol() 
        self.move_cursor_to_start()
    
    def select(self):
        if self.expanded:
            self.close()
        else:
            self.expand()
        self.expanded = not self.expanded


