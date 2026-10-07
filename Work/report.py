# report.py
#
# Exercise 2.4 & 2.5
import csv


def read_portfolio(filename):
    """
    Read a portfolio file into a list of dicts with keys name, shares and price.
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])    
            holding = {
                'name' : row[0],
                'shares' : nshares,
                'price' : price
            }
            portfolio.append(holding)
    return portfolio