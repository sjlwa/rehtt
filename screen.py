import curses

class Screen:

    """Initialize the screen"""
    def __init__(self) -> None:
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)


    """Starts the rendering"""
    def start(self):
        curses.wrapper(self.loop)


    """Revert configutation changes"""
    def close(self) -> None:
        if self.stdscr:
            curses.echo()
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.endwin()


    """Renders the screen indefinitly"""
    def loop(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Press 'q' to exit")
        self.stdscr.refresh()

        while True:
            ch = self.stdscr.getch()
            if ch == ord('q'):
                break
