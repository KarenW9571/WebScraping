from collections import namedtuple


Locator = namedtuple('Locator', ['by', 'value'])
ParserLoc = namedtuple('ParserLoc', ['name', 'text', 'class_', 'num', 'next'])
ParserLoc.__new__.__defaults__ = ("", "", "", 0, 0)

