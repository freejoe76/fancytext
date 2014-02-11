#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from optparse import OptionParser


class FancyText:
    """ Translate ascii to Unicode characters.
        >>> u = FancyText('monospace')
        >>> print u.translate('TEST')
        𝚃𝙴𝚂𝚃
        """

    def __init__(self, font='monospace'):
        """ Translation matrix via Moses Moore (https://github.com/mozai/), http://mozai.com/programming/dandytype.html
            """
        self.translation = {
            'ascii':[["!",33,"~"]],
            'parens':[["A",9372,"Z"],["a",9372,"z"],["1",9332,"9"]],
            'circled':[["A",9398,"Z"],["a",9424,"z"],["0",9450,"0"],["1",9312,"9"]],
            'bold':[["A",119808,"Z"],["a",119834,"z"],["0",120782,"9"]],
            'italic':[["A",119860,"Z"],["a",119886,"z"]],
            'bolditalic':[["A",119912,"Z"],["a",119938,"z"]],
            'script':[["A",119964,"Z"],["a",119990,"z"]],
            'boldscript':[["A",120016,"Z"],["a",120042,"z"]],
            'fraktur':[["A",120068,"Z"],["a",120094,"z"]],
            'doublestruck':[["A",120120,"Z"],["a",120146,"z"],["0",120792,"9"]],
            'boldfraktur':[["A",120172,"Z"],["a",120198,"z"]],
            'sansserif':[["A",120224,"Z"],["a",120250,"z"],["0",120802,"9"]],
            'sserifbold':[["A",120276,"Z"],["a",120302,"z"],["0",120812,"9"]],
            'sserifitalic':[["A",120328,"Z"],["a",120354,"z"]],
            'sserifboldi':[["A",120380,"Z"],["a",120406,"z"]],
            'monospace':[["A",120432,"Z"],["a",120458,"z"],["0",120822,"9"]],
            'fullwidth':[["!",65281,"~"]]
        }
        self.font = font

    def translate(self, text):
        """ First draft of a method to convert letters into unicode equivalents.
            """
        translated = ''
        if self.font not in self.translation:
            return False

        for i in text:
            chrnum = ord(i)

            # Non-letter exceptions
            if chrnum < 48 or 57 < chrnum < 65 or 90 < chrnum < 97 or 122 < chrnum:
                translated += i
                continue

            if i.isdigit():
                offset = chrnum - 48
                charset = 2
            elif i.lower() == i:
                offset = chrnum - 97
                charset = 1
            elif i.upper() == i:
                offset = chrnum - 65
                charset = 0

            translated += unichr(self.translation[self.font][charset][1] + offset)

        return translated

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--font", dest="font")
    (options, args) = parser.parse_args()

    if options.font:
        u = FancyText(options.font)
    else:
        u = FancyText()
    for arg in args:
        print u.translate(arg), 
