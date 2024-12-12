#shortest job first
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

def sjf(jobs):
    time = 0
    completed_jobs = 0
    schedule = []
    jobs = sorted(jobs, key=lambda x: x.burst_time)
    
    while completed_jobs < len(jobs):
        for job in jobs:
            if job.remaining_time > 0:
                job.start_time = time
                time += job.burst_time
                job.end_time = time
                job.turnaround_time = job.end_time
                schedule.append((job.name, job.start_time, job.end_time))
                job.remaining_time = 0
                completed_jobs += 1
    avg_turnaround = sum(job.turnaround_time for job in jobs) / len(jobs)
    return schedule, avg_turnaround

# File containing job burst times
filename = '5.txt'
jobs = read_jobs(filename)

# Run SJF Scheduling
# print("Shortest-Job-First (SJF):")
# print("Job\tStart\tEnd\tJob Completion")
# sjf_jobs = copy.deepcopy(jobs)
# sjf_schedule, sjf_avg_turnaround = sjf(sjf_jobs)
# for item in sjf_schedule:
#     print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[0]} completed @{item[2]}")
# print("Average Turnaround Time:", sjf_avg_turnaround)