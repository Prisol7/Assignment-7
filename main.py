import random
import time
from itertools import permutations
import math


def count_hires_in_array(ranks):
    if not ranks:
        return 0

    hires = 1
    best_rank_so_far = ranks[0]
    
    for i in range(1, len(ranks)):
        current_rank = ranks[i]
        if current_rank < best_rank_so_far:
            hires += 1
            best_rank_so_far = current_rank
            
    return hires

def method_1(n):
    if n < 1:
        return 0.0
    return sum(1 / i for i in range(1, n + 1))



def method_2(n):
    if n < 1:
        return 0.0, 0.0

    start_time = time.time()
   
    candidate_ranks = list(range(1, n + 1))
    all_permutations = permutations(candidate_ranks)
    
    total_hires = 0
    num_permutations = math.factorial(n)

    for ranks in all_permutations:
        total_hires += count_hires_in_array(ranks)
        
    average_hires = total_hires / num_permutations
    end_time = time.time()
    
    return average_hires, end_time - start_time


def method_3(n, num_trials):
    if n < 1:
        return 0.0, 0.0

    start_time = time.time()
    total_hires = 0
    
    candidate_ranks = list(range(1, n + 1))
    
    for _ in range(num_trials):
        random.shuffle(candidate_ranks)
        total_hires += count_hires_in_array(candidate_ranks)
        
    average_hires = total_hires / num_trials
    end_time = time.time()
    
    return average_hires, end_time - start_time

while True:
    n_input = input("Enter the number of candidates: ")
    try:
        n = int(n_input)
        if n >= 1:
            break
        else:
            print("Please enter a positive integer ")
    except ValueError:
        print("Invalid input. Please enter an integer")


NUM_TRIALS = 10000

29
exact_hires = method_1(n)


_hires, mc_time = method_3(n, NUM_TRIALS)

brute_force_hires = None
bf_time = None
if n <= 10:
    brute_force_hires, bf_time = method_2(n)

print("\n" + "="*50)
print(f"RESULTS FOR n = {n} CANDIDATES")
print("="*50)


print(f"1.")
print(f"   Expected Hires: {exact_hires:.6f}")
print("-" * 50)


print(f"2. ({NUM_TRIALS:,} trials)")
print(f"   Estimated Hires: {_hires:.6f}")
print(f"   Running Time:    {mc_time:.6f})")
print("-" * 50)

# Output Method 3 (Conditional)
print(f"3. (All {math.factorial(n):,} permutations )")
if n <= 15:
    print(f"   Average Hires:   {brute_force_hires:.6f}")
    print(f"   Running Time:    {bf_time:.6f} seconds )")
else:
    print(f"   N={n} is too large for method 3")
    print(f"   Skipped to avoid excessive run time ({n}! is too big)")

print("="*50)