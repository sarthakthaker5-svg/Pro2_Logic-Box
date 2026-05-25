print("Welcome to the Pattern Generator and Number Analyzer!")
print("Select an option:")
print("1. Generate a pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

while True:
    choice = input("Enter your choice:")
    if choice == '1':
        n = int(input("Enter the number of rows for the pattern:"))
        print("Pattern:")
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
        print("\n")
    elif choice == '2':
        start = int(input("Enter the start of the range:"))
        end = int(input("Enter the end of the range:"))
        total = 0
        for num in range(start, end+1):
            if num % 2 == 0:
                print(f"{num} is an Even.")
            else:
                print(f"{num} is an Odd.")
            total += num
        print(f"Sum of all numbers from {start} to {end} is: {total}")
        print("\n")
    elif choice == '3':
        print("Exit the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select from 1, 2, or 3.")