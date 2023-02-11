interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combinations_count = 0
combination_found = False

for i in range(interval_start, interval_end + 1):
    for j in range(interval_start, interval_end + 1):
        combinations_count += 1

        if i + j == magic_number:
            print(f"Combination N:{combinations_count} ({i} + {j} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break

if not combination_found:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
