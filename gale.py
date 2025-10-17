import random

def modified_gale_shapley(student_prefs, n):
    # Initialize all students and topics as free
    free_students = list(range(n))
    topic = [None] * n  # Topics' assigned students (None means unassigned)
    interest = {s: 0 for s in range(n)}  # Track each student's interest index

    while free_students:
        s = free_students[0]  # Pick the first free student
        # Check if student has exhausted their preference list
        if interest[s] >= n:
            free_students.remove(s)  # No more topics to propose to
            continue

        t = student_prefs[s][interest[s]]  # Get the topic the student prefers next
        interest[s] += 1  # Increment student's interest index

        # If topic is free, assign the student
        if topic[t] is None:
            topic[t] = s
            free_students.remove(s)
        else:
            # Collect all students proposing to this topic (including current student and assigned student)
            competing_students = [topic[t], s]
            # Check other free students proposing to this topic
            for other_s in free_students:
                if other_s != s and interest[other_s] < n and student_prefs[other_s][interest[other_s]] == t:
                    competing_students.append(other_s)

            # Randomly choose one of the competing students
            chosen_student = random.choice(competing_students)

            # Update assignments
            topic[t] = chosen_student

            # Handle all competing students
            for student in competing_students:
                if student == chosen_student:
                    # Chosen student is assigned, remove from free_students if present
                    if student in free_students:
                        free_students.remove(student)
                else:
                    # Non-chosen students become or remain free
                    if student not in free_students:
                        free_students.append(student)
                    # Increment interest index for non-chosen students who were proposing now
                    if student == s or (student in free_students and student_prefs[student][interest[student]] == t):
                        if interest[student] < n:  # Only increment if they have more topics to propose to
                            interest[student] += 1

    # Convert topic list to matches dictionary
    matches = {f"T{t}": f"S{topic[t]}" for t in range(n)}
    return matches

# Example usage
n = 3  # Number of students/topics
student_prefs = [
    [0, 1, 2],  # S0's preferences: T0, T1, T2
    [1, 0, 2],  # S1's preferences: T1, T0, T2
    [0, 1, 2]   # S2's preferences: T0, T1, T2
]

random.seed(42)  # For reproducibility
matches = modified_gale_shapley(student_prefs, n)
print("Matches:", matches)