# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, 
# and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.
# Exercise 1.9
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if (extra_payment_start_month - 1 <= total_month <= extra_payment_end_month - 1):
      total_paid = total_paid + payment + extra_payment
      total_month = total_month + 1
      principal = principal * (1+rate/12) - payment - extra_payment

    else:
      total_paid = total_paid + payment
      total_month = total_month + 1
      principal = principal * (1+rate/12) - payment

print('Total paid', total_paid)
print('Total month', total_month)


# off-by-one error fixed