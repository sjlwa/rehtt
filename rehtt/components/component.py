class Component:
    """Base class for creating visual components with state"""

    def __init__(self) -> None:
        pass

    def set_stdscr(self, stdscr):
        self.stdscr = stdscr

    def handle_input(self, ch: int) -> None: ...

    def render(self) -> None: ...

