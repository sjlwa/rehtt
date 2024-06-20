import curses
from pathlib import Path
from components.items import ItemsList
from components.component import Component
from events import Event

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


    def render_components(self, callback=None):
        for component in self.components:
            if callback is not None:
                callback(component)

            component.render()


    def handle(self) -> Event:

        ch = self.stdscr.getch()
        if ch == ord('q'):
            return Event.QUIT

        def handle_component_input(component):
            component.handle_input(ch)

        self.render_components(handle_component_input)

        return Event.NONE


