# report.py
#
# Exercise 2.4 & 2.5 & 2.6 & 2.7 & 2.9 & 2,10 & 2.11 & 2.12 & 2.16
import csv


def read_portfolio(filename):
    """
    Read a portfolio file into a list of dicts with keys name, shares and price.
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i,row in enumerate(rows):
            record = dict(zip(headers, row))
            name = record['name']
            nshares = int(record['shares'])
            price = float(record['price']) 
            holding = {
                'name' : name,
                'shares' : nshares,
                'price' : price
            }
            portfolio.append(holding)
    return portfolio
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)


with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_buy_in = 0
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(headers,row))
            nshares = int(record['shares'])
            price = float(record['price']) 
            total_buy_in += nshares * price 
        print(total_buy_in)

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
now_prices = read_prices('Data/prices.csv')
print(now_prices)

now_assets = 0
for s in portfolio:
    now_assets += now_prices[s['name']] * s['shares']
print(now_assets)

earn = now_assets - total_buy_in
print(earn)

def make_report(portfolio, now_prices):
    all_change = []
    per_stock = ()  # Create a list, shouldn't be in for loop!!!!!
    for s in portfolio:
        change = now_prices[s['name']] - s['price']  # Calculate the change
        per_stock = s['name'], s['shares'], now_prices[s['name']], change
        all_change.append(per_stock)
    return all_change

all_change = make_report(portfolio, now_prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print_headers = ''
separator = '-'*10
separators = ''
for h in headers:
    if h != 'Change':
       h = f'{h:>10s}{' '}'
       print_headers += h
       separator = f'{separator:10s}'
       separators += separator
       separators += ' '
    else:
        h = f'{h:>10s}'
        print_headers += h
        separator = f'{separator:10s}'
        separators += separator

print(print_headers)
print(separators)

for name, shares, price, change in all_change:
    s = f'${price:.2f}'
    print(f'{name:>10s} {shares:>10d} {s:>10s} {change:>10.2f}')
