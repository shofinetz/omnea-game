# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

from unittest import TestCase

from . import game


class GameTestCase(TestCase):

    def test_has_suit(self):
        card = game.Card()


class SuitTestCase(TestCase):

    def test_suit_order(self):
        self.assertLess(game.spades, game.clubs)
        self.assertLess(game.clubs, game.diamonds)
        self.assertLess(game.diamonds, game.hearts)
