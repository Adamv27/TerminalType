import curses
from terminaltype.widgets.widget import Widget
from terminaltype.widgets import SYMBOLS, MenuOption


class DropDownMenu(Widget):
    def __init__(self,
                 win,
                 pos: list[int],
                 title: str,
                 options: list[MenuOption],
                 can_select_multiple=False):

        super().__init__(win, pos, title)
        self.options = options
        self.can_select_multiple = can_select_multiple
        self.selected_index = -1
        self.expanded = False

    def get_selected_options(self):
        return [option.name for option in self.options if option.is_selected]

    def select(self):
        if self.expanded and self.is_hovering:
            self.close()
        elif self.expanded and not self.is_hovering:
            self.toggle_option()
        else:
            self.expand()

    def expand(self):
        for index, option in enumerate(self.options, start=1):
            symbol = SYMBOLS['toggle-on'] if option.is_selected else SYMBOLS['toggle-off']
            option_title = f'{symbol}  {option.name}'

            style = curses.A_DIM if index - 1 == self.selected_index else curses.A_NORMAL 
            self.win.addstr(self.y + index, self.x, option_title, style)
        self.move_cursor_to_start()
        self.expanded = True

    def close(self):
        for index in range(1, len(self.options) + 1):
            self.win.move(self.y + index, self.x)
            self.win.clrtoeol()
        self.move_cursor_to_start()
        self.expanded = False

    def is_expanded(self):
        return self.expanded

    def shift_cursor_vertically(self, offset):
        if not self.is_expanded():
            return

        new_index = self.selected_index + offset
        if new_index >= -1 and new_index < len(self.options):
            self.set_hovering(False)
            if new_index == -1:
                self.set_hovering(True)
            self.selected_index = new_index
            self.update()

    def toggle_option(self):
        if not self.can_select_multiple:
            for option in self.options:
                option.is_selected = False

        option = self.options[self.selected_index]
        option.is_selected = not option.is_selected
        self.update()

    def update(self):
        self.render()
        if self.is_expanded():
            self.expand()

