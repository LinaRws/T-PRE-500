# Define the starting number of bottles
bottles = 99

while bottles > 0:
    print(f"{bottles} bottles of age-appropriate bottles on the wall,")
    print(f"{bottles} bottles of age-appropriate bottles.")
    print("Take one down, pass it around,")
    bottles -= 1
    if bottles == 0:
        print("No more bottles of age-appropriate bottles on the wall.")
    else:
        print(f"{bottles} bottles of age-appropriate bottles on the wall.")
    print()