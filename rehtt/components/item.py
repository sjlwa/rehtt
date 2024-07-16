import curses
from pathlib import Path
from urllib.request import Request


class Item:
    
    value: Path|Request
    
    def __init__(self, value: Path|Request) -> None:
        self.value = value


    def method_colors(self, method: str):
        if method == 'GET': return curses.color_pair(1)
        elif method == 'POST': return curses.color_pair(2)
        elif method == 'PUT': return curses.color_pair(3)
        elif method == 'DELETE': return curses.color_pair(4)


    def render(self, screen, y, current=False):
        if isinstance(self.value, Path):
            if current:
                screen.addstr(y, 0, self.value.name, curses.A_REVERSE)
            else:
                screen.addstr(y, 0, self.value.name, curses.A_NORMAL)
        else:
            self.value: Request
            method = self.value.get_method()
            if current:
                screen.addstr(y, 0, method, curses.A_REVERSE)
                screen.addstr(y, 8, self.value.get_full_url(), curses.A_REVERSE)
            else:
                screen.addstr(y, 0, method, self.method_colors(method))
                screen.addstr(y, 8, self.value.get_full_url(), curses.A_NORMAL)
            
        

