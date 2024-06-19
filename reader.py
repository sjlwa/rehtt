from pathlib import Path


"""Reads a .http file"""
class HttpFileReader:

    filepath: Path
    content: str

    def __init__(self, filepath: str) -> None:
        path = Path(filepath)

        if path.suffix != '.http':
            raise Exception('Wrong file extension. Must be .http')

        self.filepath = path


    def read(self):
        file = open(self.filepath, 'r')
        self.content = file.read()
        return self.content
