import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flashcards import load_deck, is_correct, Flashcard

def test_load_deck():
    deck = load_deck(os.path.join('decks', 'sample.txt'))
    assert len(deck) == 3
    assert deck[0] == Flashcard(question='What is the capital of France?', answer='Paris')

def test_is_correct():
    assert is_correct('Paris', 'Paris')
    assert is_correct('paris', 'Paris')
    assert not is_correct('London', 'Paris')
