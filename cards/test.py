# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function

from unittest import TestCase

from . import game


class GameTestCase(TestCase):

    def test_has_suit(self):
        card = game.Card(game.hearts, game.jack)
        self.assertIs(card.suit, game.hearts)

    def test_has_number(self):
        card = game.Card(game.hearts, game.jack)
        self.assertIs(card.number, game.jack)


class NumberTestCase(TestCase):

    def test_number_order(self):
        self.assertLess(game.two, game.three)
        self.assertLess(game.three, game.four)
        self.assertLess(game.four, game.five)
        self.assertLess(game.five, game.six)
        self.assertLess(game.six, game.seven)
        self.assertLess(game.seven, game.eight)
        self.assertLess(game.eight, game.nine)
        self.assertLess(game.nine, game.ten)
        self.assertLess(game.ten, game.jack)
        self.assertLess(game.jack, game.queen)
        self.assertLess(game.queen, game.king)
        self.assertLess(game.king, game.ace)


class SuitTestCase(TestCase):

    def test_suit_order(self):
        self.assertLess(game.spades, game.clubs)
        self.assertLess(game.clubs, game.diamonds)
        self.assertLess(game.diamonds, game.hearts)
