A = [0] * 34
for i in range(34):
    A[i] = 3 * i + 1
j = 0
for i in range(34):
    if j == 1:
        break
    number_of_floor = A[i]
    print(f"is borken in {number_of_floor}th floor?")
    answer = int(input("enter '1' if egg is broken and '0' if it is not broken: "))
    if answer == 1:
        for k in range(2):
            number_of_floor = A[i] - (k + 1)
            print(f"is borken in {number_of_floor}th floor?")
            answer = int(input("enter '1' if egg is broken and '0' if it is not broken: "))
            if answer == 0:
                print(f"***The {number_of_floor + 1}th floor is correct answer***")
                j = 1
                break
            elif k == 1:
                print(f"***The {number_of_floor}th floor is correct answer***")
                j = 1
                break