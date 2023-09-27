import curses


class Settings:
    def __init__(self, win):
        self.win = win 
        
        self.menus = []
        self.currently_selected = 0
        self.setup_menus()
        


    def setup_menus(self):
        self.win.move(0, 0)
        position = [0, 0]
        testTypes = CollapsingMenu(self.win, position, "Test Types", [])
        
        position[0] += testTypes.get_title_width() 
        characters = CollapsingMenu(self.win, position, "Characters", [], can_select_multiple=True)
        self.menus = [testTypes, characters]

    def move_right(self):
        if self.currently_selected + 1 < len(self.menus):
            self.currently_selected += 1
            
            menu = self.menus[self.currently_selected]
            y,x = menu.get_yx()
            self.win.move(y, x)

    def move_left(self):
        if self.currently_selected - 1 >= 0:
            self.currently_selected -= 1
            
            menu = self.menus[self.currently_selected]
            y,x = menu.get_yx()
            self.win.move(y, x)

    def expand_selected(self):
        menu = self.menus[self.currently_selected]
        menu.expand()


class CollapsingMenu:
    def __init__(self, 
                 win,
                 pos,
                 title, 
                 options: list[str], 
                 can_select_multiple=False):
        self.win = win
        self.title_x, self.title_y = pos
        self.title = title
        self.options = options
        self.can_select_multiple = can_select_multiple
        self.currently_selected_index = 0
        
        self.render()
   
    def get_yx(self):
        return (self.title_y, self.title_x)

    def get_title_width(self):
        return len(self.title) + 1

    def get_currently_selected(self) -> str:
        return self.options[self.currently_selected_index]

    def render(self):
        self.win.addstr(self.title_y, self.title_x, self.title) 
    
    def expand(self):
        pass

