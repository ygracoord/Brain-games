#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games import brain_progression_logic


def main():
    run_game(brain_progression_logic)


if __name__ == '__main__':
    main()
