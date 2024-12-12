import copy
from FCFS import *
from SJF import *
from RR2 import *
from RR5 import *
import random

def generate_jobs(filename, num_jobs, max_length):
    with open(filename, 'w') as f:
        for i in range(1, num_jobs + 1):
            job_name = f"Job{i}"
            job_length = random.randint(1, max_length)  # Generate random job length
            f.write(f"{job_name}\n{job_length}\n")

#Parameters
filename = '15.txt'
num_jobs = 15
max_length = 20



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

FCFS_avg, SJF_avg, RR2_avg, RR5_avg = 0,0,0,0

for n in range (20):
    generate_jobs(filename, num_jobs, max_length)
    jobs = read_jobs(filename)

    # Run FCFS Scheduling
    print("First-Come-First-Serve (FCFS):")
    #print("Job\tStart\tEnd\tJob Completion")
    fcfs_jobs = copy.deepcopy(jobs)
    fcfs_schedule, fcfs_avg_turnaround = fcfs(fcfs_jobs)

    # for item in fcfs_schedule:
    #     print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[0]} completed @{item[2]}")
    print("Average Turnaround Time:", fcfs_avg_turnaround)
    FCFS_avg += fcfs_avg_turnaround

    # Run SJF Scheduling
    print("Shortest-Job-First (SJF):")
    #print("Job\tStart\tEnd\tJob Completion")
    sjf_jobs = copy.deepcopy(jobs)
    sjf_schedule, sjf_avg_turnaround = sjf(sjf_jobs)
    # for item in sjf_schedule:
    #     print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[0]} completed @{item[2]}")
    print("Average Turnaround Time:", sjf_avg_turnaround)
    SJF_avg += sjf_avg_turnaround
    # Run Round-Robin (Time Slice = 2) Scheduling
    print("Round-Robin with Time Slice = 2 (RR-2):")
    #print("Job\tStart\tEnd\tJob Completion")
    rr2_jobs = copy.deepcopy(jobs)
    rr2_schedule, rr2_avg_turnaround = round_robin(rr2_jobs, 2)
    # next_start = 0
    # for item in rr2_schedule:
    #     if item[3] == 0:
    #         print(f"{item[0]}\t{next_start}\t{item[2]}\t{item[0]} completed @{item[2]}")
    #     else:
    #         print(f"{item[0]}\t{next_start}\t{item[2]}")
    #     next_start = item[2]
    print("Average Turnaround Time:", rr2_avg_turnaround)
    RR2_avg += rr2_avg_turnaround

    # Run Round-Robin (Time Slice = 5) Scheduling
    print("Round-Robin with Time Slice = 5 (RR-5):")
    #print("Job\tStart\tEnd\tJob Completion")
    rr5_jobs = copy.deepcopy(jobs)
    rr5_schedule, rr5_avg_turnaround = round_robin(rr5_jobs, 5)
    # next_start = 0
    # for item in rr5_schedule:
    #     if item[3] == 0:
    #         print(f"{item[0]}\t{next_start}\t{item[2]}\t{item[0]} completed @{item[2]}")
    #     else:
    #         print(f"{item[0]}\t{next_start}\t{item[2]}")
    #     next_start = item[2]
    print("Average Turnaround Time:", rr5_avg_turnaround)
    RR5_avg += rr5_avg_turnaround

print(FCFS_avg/20,SJF_avg/20,RR2_avg/20,RR5_avg/20)