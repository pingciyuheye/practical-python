# report.py
#
# Exercise 2.4 & 2.5 & 2.6 & 2.7
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

def read_prices(filename):
    with open(filename, 'rt') as d:
        rows = csv.reader(d)
        prices = {}
        for row in rows:
            """
            try: 
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Couldn't load", row)
            """
            if len(row) > 0:
                prices[row[0]] = float(row[1])

    return prices