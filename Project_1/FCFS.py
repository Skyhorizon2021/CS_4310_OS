#first-come-first-serve

import copy

class Job:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.end_time = None
        self.turnaround_time = 0

def read_jobs(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    jobs = []
    for i in range(0, len(lines) - 1, 2):
        name = lines[i].strip()       # Job name, e.g., "Job1"
        burst_time = int(lines[i + 1].strip())  # Burst time, e.g., 7
        jobs.append(Job(name, burst_time))
    return jobs


def fcfs(jobs):
    time = 0
    schedule = []
    for job in jobs:
        job.start_time = time
        job.end_time = time + job.burst_time
        job.turnaround_time = job.end_time
        time += job.burst_time
        schedule.append((job.name, job.start_time, job.end_time))
    avg_turnaround = sum(job.turnaround_time for job in jobs) / len(jobs)
    return schedule, avg_turnaround

# File containing job burst times
filename = '5.txt'
jobs = read_jobs(filename)

# Run FCFS Scheduling
# print("First-Come-First-Serve (FCFS):")
# print("Job\tStart\tEnd\tJob Completion")
# fcfs_jobs = copy.deepcopy(jobs)
# fcfs_schedule, fcfs_avg_turnaround = fcfs(fcfs_jobs)

# # for item in fcfs_schedule:
# #     print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[0]} completed @{item[2]}")
# # print("Average Turnaround Time:", fcfs_avg_turnaround)