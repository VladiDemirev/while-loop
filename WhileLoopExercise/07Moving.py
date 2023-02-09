free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_volume = free_space_width * free_space_length * free_space_height

while free_space_volume > 0:
    user_input = input()
    if user_input != "Done":
        free_space_volume -= int(user_input)
    else:
        break

if free_space_volume > 0:
    print(f"{free_space_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space_volume)} Cubic meters more.")