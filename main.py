from urllib import request
from urllib.request import urlopen
from parser.parser import HttpFileParser
from parser.request import RequestParser
from reader import HttpFileReader
from screen import Screen

try:
    # file_reader = HttpFileReader('examples/example-01.http')
    # file_parser = HttpFileParser(file_reader)
    # file_parser.parse_variables()
    # file_parser.replace_variables()
    # file_parser.parse_entries()

    # request = RequestParser.build(file_parser.entries[1])
    # with urlopen(request) as response:
    #     print(response.read().decode('utf-8'))


    screen = Screen()
    screen.start()

except Exception as e:
    print(e)
