import curses


class Settings:
    pass


class CollapsingMenu:
    def __init__(self, title, options: list[str], can_select_multiple=False):
        self.title = title
        self.options = options
        self.can_select_multiple = can_select_multiple
        self.currently_selected_index = 0

    def get_currently_selected(self) -> str:
        return self.options[self.currently_selected_index]


