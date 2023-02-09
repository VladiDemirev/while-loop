# OPTION 1

from math import ceil, floor

change = float(input())

num_coins = 0
remaining_change = change

while remaining_change > 0:
    if change / 2 >= 1:
        num_coins = floor(change / 2)
        remaining_change = round(change % 2, 2)

    if remaining_change >= 1:
        num_coins += 1
        remaining_change = round(remaining_change - 1, 2)

    if remaining_change / 0.5 > 1:
        num_coins += 1
        remaining_change = round(remaining_change - 0.5, 2)

    if remaining_change / 0.2 >= 1:
        num_coins += floor(remaining_change / 0.2)
        remaining_change = round(remaining_change % 0.2, 2)

    if remaining_change >= 0.1:
        num_coins += 1
        remaining_change = round(remaining_change - 0.1, 2)

    if remaining_change / 0.05 >= 1:
        num_coins += 1
        remaining_change = round(remaining_change - 0.05, 2)

    if remaining_change / 0.02 >= 1:
        num_coins += floor(remaining_change / 0.02)
        remaining_change = round(remaining_change % 0.02, 2)

    if remaining_change >= 0.01:
        num_coins += 1
        remaining_change = round(remaining_change - 0.01, 2)

print(num_coins)

# OPTION 2

# change = round(float(input()) * 100)
#
# num_coins = 0
#
# while change > 0:
#     if change >= 200:
#         change -= 200
#     elif change >= 100:
#         change -= 100
#     elif change >= 50:
#         change -= 50
#     elif change >= 20:
#         change -= 20
#     elif change >= 10:
#         change -= 10
#     elif change >= 5:
#         change -= 5
#     elif change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#
#     num_coins += 1
#
# print(num_coins)
