import curses
from os import sep
from pathlib import Path
from typing import List
from .component import Component
from ..reader import DirectoryScanner, HttpFileReader


class ItemsList(Component):
    """List selectable items as valid directories or files"""

    current: int = 0
    dir: Path
    items: List[Path]

    def __init__(self) -> None:
        super().__init__()
        self.dir = Path('.').absolute()
        self.update_items()


    def update_items(self):
        """Refresh the items by scanning the current directory"""
        self.items = DirectoryScanner.filter(DirectoryScanner.scan(self.dir))
        self.items.insert(0, Path('..'))


    def back_from_item(self):
        self.dir = self.dir.parent
        self.current = 0
        self.update_items()


    def select_item(self):
        selected = self.items[self.current]

        if selected == '..':
            self.dir = self.dir.parent
        else:
            self.dir = Path.joinpath(self.dir, selected)

        self.current = 0
        self.update_items()


    def handle_input(self, ch: int):
        """Defines behaviour of the list on an event"""

        if ch == -1:
            return

        elif ch == curses.KEY_UP:
            self.current = max(0, self.current - 1)

        elif ch == curses.KEY_DOWN:
            self.current = min(len(self.items) - 1, self.current + 1)

        #ctrl+left
        elif ch == 554:
            self.back_from_item()

        #ctrl+right
        elif ch == 569:
            self.select_item()


    def render(self):
        "Renders the item list"
        max_y, max_x = self.stdscr.getmaxyx()

        for i, item in enumerate(self.items):
            item: Path

            if i >= max_y - 2:
                break

            if i == self.current:
                self.stdscr.addstr(i, 0, str(item.name), curses.A_REVERSE)
            else:
                self.stdscr.addstr(i, 0, str(item.name))
