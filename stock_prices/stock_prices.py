#!/usr/bin/python

import argparse


def find_max_profit(prices):
    print(prices)
    current_min_price = None
    max_profit = None
    for a in range(len(prices)):
        for b in prices[a + 1: len(prices)]:
            if max_profit is None or b - prices[a] > max_profit:
                max_profit = b - prices[a]
                current_min_price = b
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
