# from urllib import request
# from urllib.request import urlopen
# from rehtt.parser.parser import HttpFileParser
# from rehtt.parser.request import RequestParser
from rehtt.controller import Controller
from rehtt.screen import Screen

try:

    screen = Screen(Controller())
    screen.start()

    # file_reader = HttpFileReader('examples/example-01.http')
    # file_parser = HttpFileParser(file_reader)
    # file_parser.parse_variables()
    # file_parser.replace_variables()
    # file_parser.parse_entries()

    # request = RequestParser.build(file_parser.entries[1])
    # with urlopen(request) as response:
    #     print(response.read().decode('utf-8'))

except Exception as e:
    print(e)
