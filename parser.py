from typing import List
from reader import HttpFileReader
import re


"""Parse a file containing the directives for http requests"""
class HttpFileParser:

    file_reader: HttpFileReader
    prog = re.compile('(GET|POST|DELETE|PUT)')
    entries_pos: List
    entries: List = []


    def __init__(self, file_reader: HttpFileReader) -> None:
        self.file_reader = file_reader


    """Convert the contents into a manageable object format"""
    def parse_entries(self):
        content = self.file_reader.read()
        self.entries_pos = [entry.span() for entry in self.prog.finditer(content)]
        self.split()


    """Split the contents as its individual requests"""
    def split(self):
        length = len(self.entries_pos)
        for i in range(0, length):
            pos = self.entries_pos[i]

            if i < length - 1:
                next_pos = self.entries_pos[i + 1]
                self.entries.append(self.file_reader.content[pos[0]:next_pos[0]])

            else:
                self.entries.append(self.file_reader.content[pos[0]:-1])
