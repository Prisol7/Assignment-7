import random

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

def expected_hires(n, num_trials):

    if n < 1:
        return 0.0

    total_hires = 0
    candidate_ranks = list(range(1, n + 1)) 
    
    for _ in range(num_trials):
        random.shuffle(candidate_ranks)
        hires_in_trial = count_hires_in_array(candidate_ranks)
        total_hires += hires_in_trial
        

    average_hires = total_hires / num_trials
    return average_hires



NUM_TRIALS = 10000

while True:
    n_input = input("Enter the number of candidates")
    try:
        n = int(n_input)
        if n >= 1:
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
        print("Invalid input. Please enter an integer")


estimated_expected_hires = expected_hires(n, NUM_TRIALS)


print(f"\nResuts: ")
print(f"Number of Candidates: {n}")
print(f"Number of Trials: {NUM_TRIALS:,}")
print(f"\nEstimated Expected Number of Hires: {estimated_expected_hires:.4f}")