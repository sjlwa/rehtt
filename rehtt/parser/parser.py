from pathlib import Path
from re import split
from re import sub as replace_substring
from typing import Dict, List, Tuple
from rehtt.reader import HttpFileReader
from rehtt.parser.progs import Progs
from rehtt.parser.request import RequestParser


class HttpFileParser:
    """Parse a file containing the directives for http requests"""

    file_reader: HttpFileReader
    entries_pos: List
    entries: List = []
    variables: Dict = dict()

    def __init__(self, file_reader: HttpFileReader) -> None:
        self.file_reader = file_reader


    @staticmethod
    def extract_variable(variable_occurrence) -> Tuple:
        parts = split('(@|=)', variable_occurrence.group(0))
        name = parts[2]
        value = parts[4]
        return (name, value)


    def parse_variables(self):
        """Find the defined variables and save them as a dictionary"""

        content = self.file_reader.read()
        for var in Progs.VARS_DEFINITION.finditer(content):
            name, value = self.extract_variable(var)
            self.variables[name] = value


    def replace_variables(self):
        """Replace occurrences of variables in the contents with the real value"""

        while True:
            content = self.file_reader.read()

            def replace_var(match):
                var_name = match.group(0)[2:-2]
                return self.variables.get(var_name, match.group(0))

            updated_content = replace_substring(Progs.VARS_REPLACEMENT, replace_var, content)
            if updated_content == content:
                break

            self.file_reader.content = updated_content


    def parse_entries(self):
        """Convert the contents into a manageable object format"""

        content = self.file_reader.read()
        self.entries_pos = [entry.span() for entry in Progs.METHODS.finditer(content)]
        self.split_entries()
        RequestParser.parse_entries(self.entries)


    def split_entries(self):
        """Split the contents as its individual requests"""

        self.entries = []

        length = len(self.entries_pos)
        for i in range(0, length):
            pos = self.entries_pos[i]

            if i < length - 1:
                next_pos = self.entries_pos[i + 1]
                self.entries.append(self.file_reader.content[pos[0]:next_pos[0]])

            else:
                self.entries.append(self.file_reader.content[pos[0]:-1])
