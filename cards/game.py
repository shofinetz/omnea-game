# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function
from functools import total_ordering

@total_ordering
class Suit(object):
    def __lt__(self, other):
        return SUIT_ORDER.index(self) < SUIT_ORDER.index(other)

    def __eq__(self, other):
        return self is other


spades = Suit()
clubs = Suit()
diamonds = Suit()
hearts = Suit()
SUIT_ORDER = [spades, clubs, diamonds, hearts]


class Card(object):

    def __init__(self, suit):
        self.suit = suit
