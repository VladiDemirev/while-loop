from sys import maxsize

min_number = maxsize

while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num < min_number:
        min_number = num

print(min_number)
