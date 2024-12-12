#Round Robin with time slice = 2
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

def round_robin(jobs, time_slice):
    time = 0
    schedule = []
    queue = copy.deepcopy(jobs)
    
    # Track the last end time for each job to use as the next start time
    last_end_times = {job.name: 0 for job in queue}
    
    while any(job.remaining_time > 0 for job in queue):
        for job in queue:
            if job.remaining_time > 0:
                # Use the previous end time as the new start time for this time slice
                job.start_time = last_end_times[job.name]
                
                # Process the job for a time slice
                if job.remaining_time <= time_slice:
                    time += job.remaining_time
                    job.remaining_time = 0
                    job.end_time = time
                    job.turnaround_time = job.end_time  # Set turnaround time when job completes
                else:
                    time += time_slice
                    job.remaining_time -= time_slice
                    job.end_time = time
                
                # Append current status to the schedule and update last_end_times
                schedule.append((job.name, job.start_time, job.end_time, job.remaining_time))
                last_end_times[job.name] = job.end_time  # Update last end time for the job
    
    # Calculate average turnaround time
    avg_turnaround = sum(job.turnaround_time for job in queue) / len(queue)
    return schedule, avg_turnaround, last_end_times

# File containing job burst times
filename = '5.txt'
jobs = read_jobs(filename)

# Run Round-Robin (Time Slice = 2) Scheduling
print("Round-Robin with Time Slice = 2:")

rr2_jobs = copy.deepcopy(jobs)
rr2_schedule, rr2_avg_turnaround, last_end_times = round_robin(rr2_jobs, 2)
for item in rr2_schedule:
    print(f"{item[0]} ran from {item[1]} to {item[2]}, remaining time {item[3]}")
print("Average Turnaround Time:", rr2_avg_turnaround)
