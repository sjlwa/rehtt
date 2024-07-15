from .components.component import Component
from .events import Event

class Controller:
    """Manages the components on a screen and its events"""

    components: list[Component]

    def __init__(self) -> None:
        self.components = []


    def set_stdscr(self, stdscr):
        self.stdscr = stdscr
        for component in self.components:
            component.set_stdscr(stdscr)


    def add_component(self, component: Component):
        self.components.append(component)


    def render_components(self):
        for component in self.components:
            component.render()


    def handle_components_input(self, ch):
        for component in self.components:
            component.handle_input(ch)


    def handle(self) -> Event:

        self.render_components()

        ch = self.stdscr.getch()
        if ch == ord('q'):
            return Event.QUIT

        self.handle_components_input(ch)

        return Event.NONE


