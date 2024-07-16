# from urllib import request
# from urllib.request import urlopen
# from rehtt.parser.request import RequestParser
from rehtt.controller import Controller
from rehtt.screen import Screen

screen: Screen = Screen(Controller())
try:
    screen.start()
    # request = RequestParser.build(file_parser.entries[1])
    # with urlopen(request) as response:
    #     print(response.read().decode('utf-8'))

except Exception as e:
    screen.close()
    print(e)
