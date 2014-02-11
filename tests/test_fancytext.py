#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from fancytext.fancytext import FancyText
#import fancytext

def func(x):
    return x + 1

def test_fancytext():
    u = FancyText('monospace')
    assert u.translate('TEST') == '𝚃𝙴𝚂𝚃'
