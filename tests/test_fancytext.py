#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from fancytext.fancytext import FancyText

def test_letters():
    u = FancyText('monospace')
    assert u.translate('TEST') == '𝚃𝙴𝚂𝚃'

def test_numbers():
    u = FancyText('monospace')
    assert u.translate('12345') == '𝟷𝟸𝟹𝟺𝟻'
