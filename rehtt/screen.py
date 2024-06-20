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
        self.stdscr.keypad(True)

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


    def loop(self, screen):
        """Handles render loop"""
        screen.clear()

        self.controller.render_components()

        while True:
            rows, cols = screen.getmaxyx()
            screen.addstr(0, cols - len(str(cols)), str(cols))
            screen.addstr(rows - 1, 0, "Press 'q' to exit")

            event = self.controller.handle()

            if event == Event.QUIT:
                break

            screen.refresh()
