# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

from unittest import TestCase

from .game import Card


class GameTestCase(TestCase):

    def test_has_suit(self):
        card = Card()
