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

def expected_hires(n: int) -> float:

    if n < 1:
        return 0.0
    candidate_ranks = list(range(1, n + 1))

    all_permutations = list(permutations(candidate_ranks))
    num_permutations = len(all_permutations)
    
    total_hires = 0

    for ranks in all_permutations:
        total_hires += count_hires_in_array(ranks)

    average_hires = total_hires / num_permutations
    return average_hires


while True:
    n_input = input("enter the number of candidates: ")

    try:
        n = int(n_input)
        if n > 0:
            break
        else:
            print("please enter a positive integer.")
    except ValueError:
        print("please enter a valid integer.")

exact_average_hires = expected_hires(n)



print(f"\nResults")
print(f"Number of Candidates: {n}")
print(f"Total Permutations: {math.factorial(n):,}")
print(f"\nAverage Hires from Enumerating all n! Permutations: {exact_average_hires:.6f}")
