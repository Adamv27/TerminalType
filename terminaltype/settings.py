import sys
import curses
from widgets import MenuOption
from widgets.drop_down_menu import DropDownMenu 


class Settings:
    def __init__(self, win):
        self.win = win 
        
        self.menus = []
        self.selected_index = 0
        self.setup_menus()

    def setup_menus(self):
        self.win.move(1, 1)
        
        position = [1, 1]
        test_options = [MenuOption('15s', False),
                        MenuOption('30s', True),
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
        self.__move_to_menu(0)
       
    def toggle_selected(self):
        menu = self.menus[self.selected_index]
        menu.select()        
    
    def shift_cursor_horizontally(self, offset):
        if self.menus[self.selected_index].is_expanded():
            return

        new_index = self.selected_index + offset
        if new_index >= 0 and new_index < len(self.menus):
            self.__move_to_menu(new_index)

    def __move_to_menu(self, index):
        prev_menu = self.menus[self.selected_index]
        prev_menu.set_hovering(False)
        prev_menu.update()
        self.selected_index = index
        new_menu = self.menus[self.selected_index]
        new_menu.set_hovering(True)
        new_menu.update()
        new_menu.move_cursor_to_start() 
    
    def handle_key(self, key):
        match key:
            case 'q':
                sys.exit()
            case 'KEY_LEFT':
                self.shift_cursor_horizontally(-1)
            case 'KEY_RIGHT':
                self.shift_cursor_horizontally(1)
            case 'KEY_UP':
                self.menus[self.selected_index].shift_cursor_vertically(-1) 
            case 'KEY_DOWN':
                self.menus[self.selected_index].shift_cursor_vertically(1)
            case '\n':
                self.toggle_selected()
        
