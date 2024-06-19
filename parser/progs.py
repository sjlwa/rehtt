from re import compile


"""Defines the regular expressions used to follow syntax and find occurences"""
class Progs:

    METHODS = compile('(GET|POST|DELETE|PUT)')
    VARS_DEFINITION = compile('@\\w*=[^\n\r]*')
    VARS_REPLACEMENT = compile('{{\\w*}}')
