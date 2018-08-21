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
        'bg_black': 40,
        'bg_red': 41,
        'bg_green': 42,
        'bg_brown': 43,
        'bg_blue': 44,
        'bg_magenta': 45,
        'bg_cyan': 46,
        'bg_gray': 47,
    }

    __style = {
        'bold': 1,
        'italic': 3,
        'underline': 4,
        'blink': 5,
        'reverse_color': 7,
    }

    __reset = {
        'all': 0,
        'bold': 22,
        'italic': 23,
        'underline': 24,
        'blink': 25,
        'reverse_color': 27
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
        if attributes in self.__style:
            self._fontstyle = self.__style.get(attributes)
            return self

    def setcolorandformat(self, colour, background, style=""):
        if style == "":
            if colour in self.__colour:
                self._colour = self.__colour.get(colour)

            if background in self.__background:
                self._background = self.__background.get(background)

        return self
# TODO torvare l'errore per la stampa corretta nella string, la sequenza comandi modificatori è corretta
    def __str__(self):
        if self._colour != 30 and self._background == 0:
            return "\x1b[{!s}m{!s}\x1b[0m".format(self._colour, self.text)
        elif self._background != 0:
            return "\x1b[{!s}m{!s}\x1b[0m".format(self._background, self.text)
        elif self._fontstyle != 0:
            return "\x1b[{!s}m{!s}\x1b[0m".format(self._fontstyle, self.text)
        elif self._colour != 30 and self._background != 0:
            return "\x1b[{!s};{!s};{!s}m{!s}\x1b[0m".format(self._colour, self._fontstyle, self._background, self.text)


if __name__ == '__main__':
    print(PrintColour("hello world").setbackground("bg_red"))
    print(PrintColour("hello world").setcolorandformat("white", "bg_red", ""))
    print(PrintColour("hello world").setfontstyle("italic"))
