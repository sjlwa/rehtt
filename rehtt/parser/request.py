from typing import Tuple
from urllib.request import Request
import json

from rehtt.components.item import Item
from ..log import logtty

class RequestParser:

    @staticmethod
    def parse_entries(entries):
        for i, request_data in enumerate(entries):
            if isinstance(request_data, Item):
                entries[i] = RequestParser.parse(str(request_data.value))
            else:
                entries[i] = RequestParser.parse(request_data)


    @staticmethod
    def parse(request_data: str) -> Tuple :
        """Parse the contents of an entry as a tuple, containing the request data"""

        parts = request_data.split('\n', 1)
        first_line = parts[0].split(' ')

        method = first_line[0]
        url = first_line[1]
        data = None
        headers = {}

        if len(parts) > 1:

            content = parts[1].split('\n\n')
            potential_headers = content[0].split('\n')
            headers = {
                line.split(': ')[0]: line.split(': ')[1]
                for line in potential_headers  if ': ' in line
            }

            if len(content) > 1:
                if 'application/json' in headers.get('Content-Type', '') and content[1] != "":
                    data = json.dumps(json.loads(content[1])).encode('utf-8')
                else:
                    data = content[1].encode('utf-8')

        return (url, method, headers, data)



    @staticmethod
    def build(entry: Tuple):
        """Build a request object from the contents of its entry"""
        url, method, headers, data = entry
        return Request(url, method=method, headers=headers, data=data)


    @staticmethod
    def build_all(entries):
        for i, entry in enumerate(entries):
            entries[i] = Item(RequestParser.build(entry))
