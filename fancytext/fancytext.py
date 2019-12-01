#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import struct
import doctest


class FancyText:
    """ Translate ascii to Unicode characters.
        >>> u = FancyText('monospace')
        >>> print(u.translate('TEST'))
        𝚃𝙴𝚂𝚃
        """

    def __init__(self, font='monospace'):
        """ Translation matrix via Moses Moore ( https://github.com/mozai/ ),
            http://mozai.com/programming/dandytype.html
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
        """ First draft of a method to turn letters into monospace letters.
            What about other fonts? What about non-letter characters? That's later.
            """
        translated = ''
        if self.font not in self.translation:
            return False

        for i in text:
            chrnum = ord(i)

            # The spacebar exception.
            if chrnum == 32:
                translated += ' '
                continue

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

            try:
                translated += chr(self.translation[self.font][charset][1] + offset)
            except:
                i = self.translation[self.font][charset][1] + offset
                s = "\\U%08x" % i
                translated += s.decode('unicode-escape')
                

        return translated

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='$ python fancytext.py --font fraktur HI YOU',
                                     description='''Change the font of your terminal text. Font options:
ascii
parens
circled
bold
italic
bolditalic
script
boldscript
fraktur
doublestruck
boldfraktur
sansserif
sserifbold
sserifitalic
sserifboldi
monospace
fullwidth''',
                                     epilog='')
    parser.add_argument("-f", "--font", dest="font")
    parser.add_argument("words", action="append", nargs="*")
    parser.add_argument("-v", "--verbose", dest="verbose", default=False, action="store_true")
    args = parser.parse_args()

    if args.verbose:
        doctest.testmod(verbose=args.verbose)

    if args.font:
        u = FancyText(args.font)
    else:
        u = FancyText()
    w = ''
    for arg in args.words[0]:
        w += '%s ' % u.translate(arg)
    print(w)
