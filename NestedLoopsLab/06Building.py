num_floors = int(input())
num_rooms_per_floor = int(input())

for i in range(num_floors, 0, -1):
    for j in range(num_rooms_per_floor):

        if i == num_floors:
            print(f"L{i}{j}", end=" ")

        elif i % 2 == 0:
            print(f"O{i}{j}", end=" ")

        else:
            print(f"A{i}{j}", end=" ")
    print("")



