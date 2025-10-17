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
            chosen_student = random.choice(competing_student)

            # Free all other student who were competing
            for student in competing_student:
                if student != chosen_student:
                    if student == topic[t]:
                        free_student.append(student)  # Free the previously engaged man
                    # If man was in free _student , he's already there, no need to add
                    elif student != t:
                        free_student.append(student)  # Free other competing men
                        interest[student] += 1  # Increment their proposal index

            # Assign the chosen man
            topic[t] = chosen_student
            free_student.remove(chosen_student)

            # If the chosen man was not the current man m, ensure m remains free
            if chosen_student != s:
                if s not in free_student:
                    free_student.append(s)

    # Convert topic list to matches dictionary
    matches = {f"W{t}": f"M{topic[t]}" for t in range(n)}
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