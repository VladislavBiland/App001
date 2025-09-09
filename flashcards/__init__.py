import os
from dataclasses import dataclass
from typing import List

@dataclass
class Flashcard:
    question: str
    answer: str


def load_deck(path: str) -> List[Flashcard]:
    """Load flashcards from a text file with 'question::answer' per line."""
    cards: List[Flashcard] = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or '::' not in line:
                continue
            q, a = line.split('::', 1)
            cards.append(Flashcard(question=q.strip(), answer=a.strip()))
    return cards


def is_correct(user_input: str, answer: str) -> bool:
    """Return True if user's answer matches the card answer (case-insensitive)."""
    return user_input.strip().lower() == answer.strip().lower()


def study(deck: List[Flashcard]) -> None:
    """Run through the deck, allowing the user to answer or reveal."""
    correct = 0
    total = 0
    for card in deck:
        total += 1
        print(f"\nQuestion {total}: {card.question}")
        user_input = input("Your answer (press Enter to reveal): ")
        if user_input.strip():
            if is_correct(user_input, card.answer):
                print("Correct!")
                correct += 1
            else:
                print(f"Wrong. Correct answer: {card.answer}")
        else:
            print(f"Answer: {card.answer}")
            mark = input("Did you get it right? (y/n): ").strip().lower()
            if mark == 'y':
                correct += 1
    print("\nStudy session complete.")
    print(f"Correct: {correct}")
    print(f"Wrong: {total - correct}")
    accuracy = (correct / total * 100) if total else 0
    print(f"Accuracy: {accuracy:.2f}%")


def choose_deck(directory: str) -> str:
    """Allow user to choose a deck file from directory."""
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not files:
        raise FileNotFoundError("No deck files found.")
    print("Available decks:")
    for idx, name in enumerate(files, 1):
        print(f"{idx}. {name}")
    while True:
        choice = input("Select deck number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(files):
                return os.path.join(directory, files[idx - 1])
        print("Invalid selection. Try again.")


if __name__ == '__main__':
    deck_path = choose_deck('decks')
    deck = load_deck(deck_path)
    study(deck)
