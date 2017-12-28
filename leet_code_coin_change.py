# find the total combination possible for the number of ints in coins ie 3^3
# run a for loop that figures out if any of the coins are > amount, discard coins
# run a for loop that grabs any coins equal to amount and count that and then discard coin
# while loop to grab the first number and add it to itself until it is >= to amount
# find len of amount ie 5
# create a list of amount_n [a, b, c, d, e]
# for loop fills each item in list with first coin
# append amounts to coint_totals list
# for loop replaces each item with coin returning amount to coin_totals
#

amount = 7
coins = [1, 2, 5, 10, 15]
use_coins = []
coin_combo = 0
amount_len = amount
amount_calc = []
coin_it = 0
coin_index = amount_calc.index(coin_it)

for coin in coins:
    if coin == amount:
        coin_combo += 1
        coins.remove(coin)
    elif coin < amount:
        use_coins.append(coin)

# populates the amount_calc with 0
while amount_len > 0:
    amount_calc.append(0)
    amount_len -= 1

for coin_index in amount_calc:
    amount_calc[coin_index:coin_index] = [1]

print(coin_combo)



# single digit adds to self
# for coin in use_coins:
#     coin_total = 0
#     while coin_total <= amount:
#         coin_total = coin + coin_total
#         if coin_total == amount:
#             coin_combo += 1
#             break
#         elif coin_total > amount:
#             amount_a = coin_total - amount
#             coin_total = coin_total - coin
#             if amount_a in use_coins:
#                 amount_b = amount_a + coin_total
#                 coin_combo += 1
#                 break
#             else:
#                 break
