def calculate_expected_hires(n):

    if n < 1:
        return 0.0

    expected_sum = 0.0

    for i in range(1, n + 1):
        expected_sum += 1 / i
        
    return expected_sum

while True:
    n_input = input("Enter the number of candidates: ")
    try:
        n = int(n_input)
        if n >= 0:
            break
        else:
            print("Please enter a non-negative integer")
    except ValueError:
        print("Invalid input please enter an integer")

result = calculate_expected_hires(n)


print(f"\nResult: ")
print(f"For n = {n} candidates, the expected number of hires is:")
print(f"{result:.4f}") 