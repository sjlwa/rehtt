from parser.parser import HttpFileParser
from reader import HttpFileReader


try:
    file_reader = HttpFileReader('examples/example-01.http')
    file_parser = HttpFileParser(file_reader)
    file_parser.parse_variables()
    file_parser.replace_variables()
    file_parser.parse_entries()
    print(file_parser.entries)

except Exception as e:
    print(e)
