Portfolio Diversification Checker :§

A Python program I made to check how spread out a portfolio is.
# How I built it :
I wrote the code myself while learning Python, and used Claude as a tutor
to explain things when I got stuck. The parts I found hardest were nested
dictionaries and using max() with key=.

# What it does : 
You enter your holdings (company name, sector, and how much you invested).
The program then:
- works out the total value
- shows what percentage of the money is in each sector
- warns you if one sector is over 40%
- shows your biggest holding
- gives a diversification score out of 100

# How the score works:
I square each sector's percentage and add them up. Big sectors count for
more this way. Then I do 1 minus that number and multiply by 100, so a
higher score means the money is more spread out.

Type each holding when it asks, and type `done` when you finish.

# Example:
Apple (tech, 5000), Microsoft (tech, 4000), Shell (energy, 2000),
Unilever (consumer, 1500) gives:

    Total value: £12,500.00
    tech has a weight of 72.0% - over-concentrated
    Largest holding: Apple (40.0%)
    Diversification score: 44/100

# Things I want to improve : 
- It crashes if you type text instead of a number for the value
- Entering the same company twice replaces the first one
- Using real price data to measure risk
