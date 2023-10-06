import curses


class Widget:
    def __init__(self, win, pos, title):
        self.win = win
        self.y, self.x = pos
        self.title = title
        self.is_hovering = False
        
        self.render()

    def get_title_width(self):
        return len(self.title) + 1

    def get_yx(self):
        return self.y, self.x

    def move_cursor_to_start(self):
        self.win.move(self.y, self.x)

    def hovering(self, is_hovering):
        self.is_hovering = is_hovering
    
    def select(self):
        pass

    def render(self):
        style = curses.A_UNDERLINE if self.is_hovering else curses.A_NORMAL
        self.win.addstr(self.y, self.x, self.title, style) 

