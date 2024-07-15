from os import path
from pathlib import Path
from typing import Iterator


class HttpFileReader:
    """Reads a .http file"""

    filepath: Path
    content: str = ""

    def __init__(self, filepath: str) -> None:
        path = Path(filepath)

        if path.suffix != '.http':
            raise Exception('Wrong file extension. Must be .http')

        self.filepath = path


    def read(self):
        if self.content == "":
           file = open(self.filepath, 'r')
           self.content = file.read()

        return self.content



class DirectoryScanner:

    @staticmethod
    def scan(path: Path) -> Iterator:

        if not path.exists():
            raise IsADirectoryError('Directory does not exists')

        if not Path.is_dir(path):
            raise IsADirectoryError('{} is not a directory'.format(path))

        return Path.iterdir(path)


    @staticmethod
    def filter_http(item: Path):
        return item.is_dir() or (item.is_file() and item.suffix == '.http')


    @staticmethod
    def filter(iterdir: Iterator):
        return list(filter(DirectoryScanner.filter_http, iterdir))
