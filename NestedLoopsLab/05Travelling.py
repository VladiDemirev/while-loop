
money_saved = 0

while True:
    destination = input()
    min_budget = float(input())
    while money_saved < min_budget:
        money_saved += float(input())
