from recordtype import recordtype


SYMBOLS = {'toggle-off': '\uf204',
           'toggle-on': '\uf205'}

MenuOption = recordtype('MenuOption', 'name is_selected')

