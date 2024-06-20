import curses
from pathlib import Path
from typing import List
from components.component import Component
from reader import DirectoryScanner, HttpFileReader


class ItemsList(Component):
    """List selectable items as valid directories or files"""

    current: int = 0
    items: List[Path]

    def __init__(self) -> None:
        super().__init__()
        self.items = DirectoryScanner.filter(DirectoryScanner.scan('..'))
        self.items.insert(0, Path('..'))


    def handle_input(self, ch: int):
        """Defines behaviour of the list on an event"""
        if ch == curses.KEY_UP:
            self.current = max(0, self.current - 1)
        elif ch == curses.KEY_DOWN:
            self.current = min(len(self.items) - 1, self.current + 1)


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
