import random

def modified_gale_shapley(men_prefs, women_prefs, n):
    # Initialize all men and women as free
    free_men = list(range(n))
    partner = [None] * n  # Women's partners (None means unengaged)
    proposals = {m: 0 for m in range(n)}  # Track each man's proposal index
    
    while free_men:
        m = free_men[0]  # Pick the first free man
        w = men_prefs[m][proposals[m]]  # Get the woman he prefers next
        
        # Increment man's proposal index
        proposals[m] += 1
        
        # If woman is free, engage them
        if partner[w] is None:
            partner[w] = m
            free_men.remove(m)
        else:
            # If woman is already engaged, collect all men proposing to her (including current man)
            competing_men = [partner[w], m]
            # Check if other free men are also proposing to this woman at their current preference
            for other_m in free_men:
                if other_m != m and men_prefs[other_m][proposals[other_m]] == w:
                    competing_men.append(other_m)
            
            # Randomly choose one of the competing men
            chosen_man = random.choice(competing_men)
            
            # Free all other men who were competing
            for man in competing_men:
                if man != chosen_man:
                    if man == partner[w]:
                        free_men.append(man)  # Free the previously engaged man
                    # If man was in free_men, he's already there, no need to add
                    elif man != m:
                        free_men.append(man)  # Free other competing men
                        proposals[man] += 1  # Increment their proposal index
            
            # Assign the chosen man
            partner[w] = chosen_man
            free_men.remove(chosen_man)
            
            # If the chosen man was not the current man m, ensure m remains free
            if chosen_man != m:
                if m not in free_men:
                    free_men.append(m)
    
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