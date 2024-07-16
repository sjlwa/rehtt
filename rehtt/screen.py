import curses
from .controller import Controller
from .components.items import ItemsList
from .events import Event


class Screen:

    controller: Controller

    def __init__(self, controller) -> None:
        """Initialize the screen"""
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(True)

        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

        self.controller = controller
        self.init_components()
        self.controller.set_stdscr(self.stdscr)


    def init_components(self):
        self.controller.add_component(ItemsList())


    def start(self):
        """Starts the rendering"""
        curses.wrapper(self.loop)


    def close(self) -> None:
        """Revert configutation changes"""
        if self.stdscr:
            curses.echo()
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.endwin()
            curses.curs_set(1)


    def loop(self, screen):
        """Handles render loop"""
        screen.clear()
        while True:
            rows, cols = screen.getmaxyx()
            screen.addstr(0, cols - len(str(cols)), str(cols))
            screen.addstr(rows - 1, 0, "Press 'q' to exit")

            event = self.controller.handle()

            if event == Event.QUIT:
                break

            screen.clear()
