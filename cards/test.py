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


class PlayerTestCase(TestCase):

    def test_player_has_cards(self):
        player = game.Player()
        player.give_card(game.jack)
        player.give_card(game.ace)
        self.assertEqual(player.cards, [game.jack, game.ace])


class GameTestClass(TestCase):

    def test_game_has_players(self):
        p1 = game.Player()
        p2 = game.Player()
        g = game.Game([p1, p2])
        self.assertTrue(g.players, [p1, p2])

    def test_game_has_deck(self):
        p1 = game.Player()
        p2 = game.Player()
        g = game.Game([p1, p2])
        self.assertTrue(len(g.pack), len(game.NUMBER_ORDER) * len(game.SUIT_ORDER))

    def test_deal(self):
        p1 = game.Player()
        p2 = game.Player()
        g = game.Game([p1, p2])
        g.deal()
        self.assertEqual(len(p1.cards), len(p2.cards))

    def test_is_shuffled(self):
        p1 = game.Player()
        p2 = game.Player()
        g = game.Game([p1, p2])
        self.assertNotEqual(g.PACK, g.pack)
