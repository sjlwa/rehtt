from typing import Tuple
from urllib.request import Request
import json


class RequestParser:

    @staticmethod
    def parse_entries(entries):
        for i, request_data in enumerate(entries):
            entries[i] = RequestParser.parse(request_data)


    """Parse the contents of an entry as a tuple, containing the request data"""
    @staticmethod
    def parse(request_data: str) -> Tuple :

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



    """Build a request object from the contents of its entry"""
    @staticmethod
    def build(entry: Tuple):
        url, method, headers, data = entry
        return Request(url, method=method, headers=headers, data=data)
