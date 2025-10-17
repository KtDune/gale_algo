import random

def modified_gale_shapley(men_prefs, women_prefs, n):
    # Initialize all men and women as free
    free_men = list(range(n))
    partner = [None] * n  # Women's partners (None means unengaged)
    proposals = {m: 0 for m in range(n)}  # Track each man's proposal index
    
    while free_men:
        m = free_men[0]  # Pick the first free man
        # Check if man has exhausted his preference list
        if proposals[m] >= n:
            free_men.remove(m)  # No more women to propose to
            continue
        
        w = men_prefs[m][proposals[m]]  # Get the woman he prefers next
        proposals[m] += 1  # Increment man's proposal index
        
        # If woman is free, engage them
        if partner[w] is None:
            partner[w] = m
            free_men.remove(m)
        else:
            # Collect all men proposing to this woman (including current man and her partner)
            competing_men = [partner[w], m]
            # Check other free men proposing to this woman
            for other_m in free_men:
                if other_m != m and proposals[other_m] < n and men_prefs[other_m][proposals[other_m]] == w:
                    competing_men.append(other_m)
            
            # Randomly choose one of the competing men
            chosen_man = random.choice(competing_men)
            
            # Update partnerships
            partner[w] = chosen_man
            
            # Handle all competing men
            for man in competing_men:
                if man == chosen_man:
                    # Chosen man is engaged, remove from free_men if present
                    if man in free_men:
                        free_men.remove(man)
                else:
                    # Non-chosen men become or remain free
                    if man not in free_men:
                        free_men.append(man)
                    # Increment proposal index for non-chosen men who were proposing now
                    if man != partner[w] or man == m:
                        if proposals[man] < n:  # Only increment if they have more women to propose to
                            proposals[man] += 1
    
    # Convert partner list to matches dictionary
    matches = {f"W{w}": f"M{partner[w]}" for w in range(n)}
    return matches

# Example usage
n = 3  # Number of men/women
men_prefs = [
    [0, 1, 2],  # M0's preferences: W0, W1, W2
    [1, 0, 2],  # M1's preferences: W1, W0, W2
    [0, 1, 2]   # M2's preferences: W0, W1, W2
]
women_prefs = [
    [0, 1, 2],  # W0's preferences (not used)
    [1, 0, 2],  # W1's preferences (not used)
    [0, 1, 2]   # W2's preferences (not used)
]

random.seed(42)  # For reproducibility
matches = modified_gale_shapley(men_prefs, women_prefs, n)
print("Matches:", matches)