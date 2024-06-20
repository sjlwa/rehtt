import curses

class Screen:

    def __init__(self, controller) -> None:
        """Initialize the screen"""
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)


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


    def loop(self, stdscr):
        """Handles render loop"""

        self.stdscr = stdscr
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Press 'q' to exit")
        self.stdscr.refresh()

        while True:
            ch = self.stdscr.getch()
            if ch == ord('q'):
                break
