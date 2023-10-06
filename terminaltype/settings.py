import curses
from widgets.drop_down_menu import DropDownMenu 
from collections import namedtuple

class Settings:
    def __init__(self, win):
        self.win = win 
        
        self.menus = []
        self.currently_selected = 0
        self.menu_expanded = False

        self.setup_menus()

    def setup_menus(self):
        self.win.move(1, 1)
        
        MenuOption = namedtuple('MenuOption', 'name is_selected')
        position = [1, 1]
        test_options = [MenuOption('15s', False),
                        MenuOption('30s', False),
                        MenuOption('60s', False),
                        MenuOption('30 Words', False),
                        MenuOption('100 Words', False)]
        test_type = DropDownMenu(self.win, position, "Test Type", test_options) 
        position[1] += test_type.get_title_width()

        character_options = [MenuOption('Capitals', True), 
                             MenuOption('Special', False), 
                             MenuOption('Punctuation', True)]
        characters = DropDownMenu(self.win, position, 'Characters', character_options, can_select_multiple=True)
        self.menus = [test_type, characters]

    def move_right(self):
        if not self.menu_expanded and self.currently_selected + 1 < len(self.menus):
            self.__move_to_menu(self.currently_selected + 1)

    def move_left(self):
        if not self.menu_expanded and  self.currently_selected - 1 >= 0:
            self.__move_to_menu(self.currently_selected - 1)

    def toggle_selected(self):
        menu = self.menus[self.currently_selected]
        menu.select()        
        self.menu_expanded = not self.menu_expanded
   
    def __move_to_menu(self, index):
        prev_menu = self.menus[self.currently_selected]
        prev_menu.hovering(False)
        prev_menu.render()
        self.currently_selected = index
        new_menu = self.menus[self.currently_selected]
        new_menu.hovering(True)
        new_menu.render()
        new_menu.move_cursor_to_start() 


