#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from fancytext.fancytext import FancyText

def test_punctuation():
    u = FancyText('monospace')
    assert u.translate('TEST.-@*') == '𝚃𝙴𝚂𝚃.-@*'

def test_nofont():
    u = FancyText('hahahahaha')
    assert u.translate('TEST') == False

def test_letters():
    u = FancyText('monospace')
    assert u.translate('TEST') == '𝚃𝙴𝚂𝚃'

def test_numbers():
    u = FancyText('monospace')
    assert u.translate('12345') == '𝟷𝟸𝟹𝟺𝟻'

def test_letters_numbers_and_space():
    u = FancyText('monospace')
    assert u.translate('123 45 TEST') == '𝟷𝟸𝟹 𝟺𝟻 𝚃𝙴𝚂𝚃'
