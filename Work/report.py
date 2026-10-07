# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    """
    Computes the total cost (share*price) of a portfolio file
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            holding = (row[0], nshares, price)
            portfolio.append(holding)
        print(portfolio)
    return portfolio