def activity_selection(activities):
    # Sort the activities by their end times in ascending order.
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected_activities = [sorted_activities[0]]  # Select the first activity.

    # Iterate through the sorted activities and select non-overlapping ones.
    for i in range(1, len(sorted_activities)):
        current_activity = sorted_activities[i]
        last_selected_activity = selected_activities[-1]

        # If the current activity's start time is greater than or equal to the last selected activity's end time,
        # it doesn't overlap, so we can select it.
        if current_activity[0] >= last_selected_activity[1]:
            selected_activities.append(current_activity)

    return selected_activities

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
result = activity_selection(activities)
print(result)
