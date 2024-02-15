#!/usr/bin/env python3
import argparse
import random
import secrets


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--must', help="character which is a must", required=True)
    parser.add_argument('--extra', '-e', nargs="*", help="extra characters", required=True)
    parser.add_argument('--hints', type=int, help='number of words to generate (max)', required=True)
    args = parser.parse_args()

    if len(args.extra) != 6:
        print('error: must provide 6 extra characters')
        exit(1)

    return args


def get_cide_dataset_words(must_char: str, extras: list[str]):
    initial_words = []
    # read the DB
    with open('cide_words_4.txt', 'r') as cide_db:
        return cide_db.readlines()


def get_relevant_words(must_char: str, extras: list[str], cide_words: list[str]):
    relevant_chars = extras + [must_char]
    relevant_words = []
    for word in cide_words:
        clean_word = word.lower().strip()
        if all(ch in relevant_chars for ch in clean_word):
            if must_char in clean_word:
                relevant_words.append(clean_word)

    return relevant_words


def generate_hints(relevant_words: list[str], hints: int):
    secure_random = random.SystemRandom()
    return secure_random.sample(relevant_words, hints)


def spellingbee_hints_main():
    args = get_args()
    cide_words = get_cide_dataset_words(must_char=args.must, extras=args.extra)
    relevant_words = get_relevant_words(must_char=args.must, extras=args.extra, cide_words=cide_words)
    hints = generate_hints(relevant_words=relevant_words, hints=args.hints)
    for hint in hints:
        print(hint)


if __name__ == "__main__":
    spellingbee_hints_main()
