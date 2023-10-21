def job_sequencing(jobs):
    # Sort the jobs by their profits in descending order.
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    max_deadline = max(jobs, key=lambda x: x[1])[1]  # Find the maximum deadline.

    # Initialize an array to track job slots.
    job_slots = [-1] * (max_deadline + 1)

    selected_jobs = []
    total_profit = 0

    # Iterate through the sorted jobs and fill job slots.
    for job in sorted_jobs:
        job_id, deadline, profit = job

        # Find a suitable slot for the job before its deadline.
        for i in range(deadline, 0, -1):
            if job_slots[i] == -1:
                job_slots[i] = job_id
                total_profit += profit
                selected_jobs.append(job)
                break

    return selected_jobs, total_profit


jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
result, profit = job_sequencing(jobs)
print("Selected Jobs:", result)
print("Total Profit:", profit)
