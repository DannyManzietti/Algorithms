#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    play = []
    rps = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return [play]

    if n == 1:
        return rps

    for rpslist in rock_paper_scissors(n - 1):
        for plays in rps:
            play.append(rpslist + plays)

    return play


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
