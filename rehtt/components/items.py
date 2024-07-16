import curses
from os import sep, write
from pathlib import Path
from typing import List

from .item import Item
from rehtt.parser.request import RequestParser
from rehtt.parser.parser import HttpFileParser
from .component import Component
from rehtt.reader import DirectoryScanner, HttpFileReader


class ItemsList(Component):
    """List selectable items as valid directories or files"""

    current: int = 0
    dir: Path
    items: List[Item]


    def print_items(self):
        print('====== items list ======')
        print("current: ", self.current, " dir: ", self.dir)
        for item in self.items:
            print(item.value)
        print()


    def __init__(self) -> None:
        super().__init__()
        self.dir = Path('.').absolute()
        self.update_items()


    def update_items(self):
        """Refresh the items by scanning the current directory or file"""

        if self.dir.is_file():
            file_reader = HttpFileReader(str(self.dir))
            file_parser = HttpFileParser(file_reader)
            file_parser.parse_variables()
            file_parser.replace_variables()
            file_parser.parse_entries()
            RequestParser.build_all(file_parser.entries)
            self.items = file_parser.entries
        else:
            self.items = DirectoryScanner.filter(DirectoryScanner.scan(self.dir))
            self.items.insert(0, Item(Path('..')))


    def back_from_item(self):
        self.dir = self.dir.parent
        self.current = 0
        self.update_items()


    def select_item(self, current=None):
        if current:
            self.current = current

        selected = self.items[self.current]

        if isinstance(selected.value, Path):
            if str(selected.value) == '..':
                self.dir = self.dir.parent
            else:
                self.dir = Path.joinpath(self.dir, selected.value)

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
            item: Item

            if i >= max_y - 2:
                break

            item.render(self.stdscr, i, i == self.current)
