from re import compile


class Progs:
    """Defines the regular expressions used to follow syntax and find occurences"""

    METHODS = compile('(GET|POST|DELETE|PUT)')
    VARS_DEFINITION = compile('@\\w*=[^\n\r]*')
    VARS_REPLACEMENT = compile('{{\\w*}}')
