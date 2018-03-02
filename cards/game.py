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


@total_ordering
class Number(object):
    def __lt__(self, other):
        return NUMBER_ORDER.index(self) < NUMBER_ORDER.index(other)

    def __eq__(self, other):
        return self is other


two = Number()
three = Number()
four = Number()
five = Number()
six = Number()
seven = Number()
eight = Number()
nine = Number()
ten = Number()
jack = Number()
queen = Number()
king = Number()
ace = Number()

NUMBER_ORDER = [
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten,
    jack,
    queen,
    king,
    ace,
]


class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
