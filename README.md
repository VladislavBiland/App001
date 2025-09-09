# Flashcards App

A simple command-line flashcards application.

## Features

- Import flashcards from a text file (`question::answer` format).
- Study mode: reveal the answer or type it in for validation.
- Statistics tracking: correct vs wrong answers and accuracy percentage.
- Deck management: select different sets of flashcards from a directory.

## Usage

1. Add text files to the `decks/` folder (`question::answer` per line).
2. Run the app:

   ```bash
   python -m flashcards
   ```

3. Choose a deck and start studying.

## Development

Install dependencies (for tests only) and run tests:

```bash
pip install -r requirements.txt
pytest
```
