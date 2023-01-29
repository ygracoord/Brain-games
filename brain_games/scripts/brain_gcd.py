#!/usr/bin/env python3

from brain_games.brain_engine import playing
from brain_games.games import brain_gcd_logic


def main():
    playing(brain_gcd_logic)


if __name__ == '__main__':
    main()
