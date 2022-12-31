#firstloops 1
# Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for value in numbers:
    if value % 5 == 0:
        if value <= 150:
            print(value)
            continue
        if value > 500:
            break
