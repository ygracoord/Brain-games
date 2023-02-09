#!/usr/bin/env python3

from brain_games.games import calculate
from brain_games.engine import run_game


def main():
    run_game(calculate)


if __name__ == '__main__':
    main()
