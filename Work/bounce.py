# bounce.py
#
# Exercise 1.5
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.
ball_height=100.0
time=1
for i in range(10): 
   time=time+1
   ball_height= ball_height*(3/5)
   round_height= round(ball_height, ndigits=4)
   print (round_height)
