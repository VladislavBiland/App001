from . import choose_deck, load_deck, study


def main() -> None:
    deck_path = choose_deck('decks')
    deck = load_deck(deck_path)
    study(deck)


if __name__ == '__main__':
    main()
