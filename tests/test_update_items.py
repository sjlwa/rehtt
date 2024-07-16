import unittest

from rehtt.components.items import ItemsList

class TestUpdateItems(unittest.TestCase):

    def test_update_items_on_context_change(self):

        items = ItemsList()
        items.print_items()
        items.select_item(4)
        items.print_items()
        items.select_item(1)
        items.print_items()
        items.back_from_item()
        items.print_items()
        items.select_item(1)
        items.print_items()

