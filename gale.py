import random


def modified_gale_shapley(student_prefs, n):
    # Initialize all student and women as free
    free_student = list(range(n))
    topic = [None] * n  # (None means not chosen by any student)
    interest = {s: 0 for s in range(n)}  # Track each student's interest index

    while free_student:
        s = free_student[0]  # Pick the first free man
        t = student_prefs[s][interest[s]]  # Get the topic he prefers next

        # Increment man's proposal index
        interest[s] += 1

        # If woman is free, engage them
        if topic[t] is None:
            topic[t] = s
            free_student.remove(s)
        else:
            # If woman is already engaged, collect all student proposing to her (including current man)
            competing_student = [topic[t], s]
            # Check if other free student are also proposing to this woman at their current preference
            for other_s in free_student:
                if other_s != s and student_prefs[other_s][interest[other_s]] == t:
                    competing_student.append(other_s)

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
student_prefs = [
    [0, 1, 2],  # M0's preferences: W0, W1, W2
    [1, 0, 2],  # M1's preferences: W1, W0, W2
    [0, 1, 2]  # M2's preferences: W0, W1, W2
]

random.seed(42)  # For reproducibility
matches = modified_gale_shapley(student_prefs, n)
print("Matches:", matches)