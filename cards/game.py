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

class Player(object):

    def __init__(self):
        self.cards = []

    def give_card(self, card):
        self.cards.append(card)


class Game(object):
    PACK = [
        Card(spades, two),
        Card(spades, three),
        Card(spades, four),
        Card(spades, five),
        Card(spades, six),
        Card(spades, seven),
        Card(spades, eight),
        Card(spades, nine),
        Card(spades, ten),
        Card(spades, jack),
        Card(spades, queen),
        Card(spades, king),
        Card(spades, ace),

        Card(clubs, two),
        Card(clubs, three),
        Card(clubs, four),
        Card(clubs, five),
        Card(clubs, six),
        Card(clubs, seven),
        Card(clubs, eight),
        Card(clubs, nine),
        Card(clubs, ten),
        Card(clubs, jack),
        Card(clubs, queen),
        Card(clubs, king),
        Card(clubs, ace),

        Card(diamonds, two),
        Card(diamonds, three),
        Card(diamonds, four),
        Card(diamonds, five),
        Card(diamonds, six),
        Card(diamonds, seven),
        Card(diamonds, eight),
        Card(diamonds, nine),
        Card(diamonds, ten),
        Card(diamonds, jack),
        Card(diamonds, queen),
        Card(diamonds, king),
        Card(diamonds, ace),

        Card(hearts, two),
        Card(hearts, three),
        Card(hearts, four),
        Card(hearts, five),
        Card(hearts, six),
        Card(hearts, seven),
        Card(hearts, eight),
        Card(hearts, nine),
        Card(hearts, ten),
        Card(hearts, jack),
        Card(hearts, queen),
        Card(hearts, king),
        Card(hearts, ace),
    ]

    def __init__(self, players):
        self.players = players

