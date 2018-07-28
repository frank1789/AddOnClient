class PrintColour:
    __colour = {
        'reset': 0,
        'black': 30,
        'red': 31,
        'green': 32,
        'brown': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'gray': 37,
        'darkgray': 90,
        'lightred': 91,
        'Lightgreen': 92,
        'Lightyellow': 93,
        'Lightblue': 94,
        'Lightmagenta': 95,
        'Lightcyan': 96,
        'White': 97,
    }

    __background = {
        'bg_black': "\e[40m",
        'bg_red': "\e[41m",
        'bg_green': "\e[42m",
        'bg_brown': "\e[43m",
        'bg_blue': "\e[44m",
        'bg_magenta': "\e[45m",
        'bg_cyan': "\e[46m",
        'bg_gray': "\e[47m",
    }

    __fontstyle = {
        'bold': 1,
        'italic': 3,
        'underline': 4,
        'blink': 5,
        'reverse_color': 7,
    }

    __reset = {
        'all': "\e[0m",
        'bold': "\e[22m",
        'italic': "\e[23m",
        'underline': "\e[24m",
        'blink': "\e[25m",
        'reverse_color': "\e[27m"
    }

    text = ""

    _colour = 30

    _background = 0

    _fontstyle = 0

    def __init__(self, message):
        super(PrintColour, self).__init__()
        self.text = message

    def setcolour(self, colour):
        if colour in self.__colour:
            self._colour = self.__colour.get(colour)
            return self

    def setbackground(self, background):
        if background in self.__background:
            self._background = self.__background.get(background)
            return self

    def setfontstyle(self, attributes):
        if attributes in self.__fontstyle:
            self._fontstyle = self.__fontstyle.get(attributes)
            return self

    def setcolorandformat(self, colour=0, background=0, attributes=0):
        print("\e[1;31;47m #{self} #{RESET[all]}")
        return self

    def __str__(self):
        return "\x1b[{!s}m{!s}\x1b[0m".format(self._colour, self.text)



if __name__ == '__main__':
    print(PrintColour("hello world").setcolour('red'))
