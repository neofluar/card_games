#!python3
# A simulator of the Russian card game "Jug Artist" (aka "Pianitza") 
# for 4 persons.

from random import shuffle
from operator import itemgetter
from collections import deque

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def initialize_deck():
    """Initialazing a standard shuffled 36-cards deck."""
    deck = [(nom, s) for nom in range(6,15) for s in ('♣','♥','♠','♦')]
    shuffle(deck)
    return deck

def get_hands(deck, n=4):
    """Spreading the deck among 4 hands."""
    hands = [deque(deck[i::n]) for i in range(n)]
    return hands

def compare_cards(last_cards, active_players):
    """Comparing the last cards that were put on the table."""
    winners = []
    max_nominal = max(last_cards, key=itemgetter(0))[0]
    logging.debug('Max nominal ' + str(max_nominal))
    for i in range(len(last_cards)):
        if last_cards[i][0] == max_nominal:
            winners.append(active_players[i])
    logging.debug('Winner(s) ' + str(winners))
    return winners

def update_hand(hand, table):
    """
    A winner of a round has to put the cards from the table under his hand.
    The cards should be shuffled to avoid cycles in the game.
    """
    shuffle(table)
    for card in table:
        hand.appendleft(card)
    return hand

def announce_results(hands):
    """
    Announcing who is a looser and a Pianitza!
    There could be more than 1.
    """
    pianitzas = [i+1 for i in range(4) if not hands[i]]
    for pianitza in pianitzas:
        print('Player {0} is a PIANITZA!'.format(pianitza))

def print_cards(cards, note):
    """Prints neatly formatted cards."""
    outp = []
    big_nominals = ('J', 'Q', 'K', 'A')
    for nom, s in cards:
        if nom > 10:
            nom = big_nominals[nom%10-1]
        else:
            nom = str(nom)
        outp.append(nom + s)
    print(note, '  '.join(outp))

def gameplay():
    table = []
    active_players = list(range(4))
    hands = get_hands(initialize_deck())
    for i in range(len(hands)):
        print_cards(hands[i], 'Hand ' + str(i+1) + ':')
    while all(hands):
        table.extend([hands[i].pop() for i in active_players])
        print_cards(table, 'Table:')
        winners = compare_cards(table[-len(active_players):], active_players)
        if len(winners) > 1:
            active_players = winners
        else:
            win = winners[0]
            hands[win] = update_hand(hands[win], table)
            table = []
            active_players = list(range(4))
        print(' '.join([str(len(hand)) for hand in hands]))
    announce_results(hands)
        
if __name__ == '__main__':
    gameplay()
    
