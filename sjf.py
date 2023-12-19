def sjf_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort based on burst time

    waiting_time = [0] * n
    turnaround_time = [0] * n
    executed_processes = []  # To track the sequence of executed processes

    current_time = 0

    for i in range(n):
        executed_processes.append(processes[i][0])
        waiting_time[i] = current_time
        current_time += processes[i][1]
        turnaround_time[i] = current_time

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return (
        waiting_time,
        turnaround_time,
        average_waiting_time,
        average_turnaround_time,
        executed_processes
    )
# Example usage:
process_list = [
    (1, 6),
    (2, 8),
    (3, 7),
    (4, 3)
]

waiting, turnaround, avg_waiting, avg_turnaround, sequence = sjf_non_preemptive(process_list)

print("Process\t  Waiting Time\t  Turnaround Time")
for i in range(len(process_list)):
    print(f"{process_list[i][0]}\t\t{waiting[i]}\t\t{turnaround[i]}")
print(f"\nAverage Waiting Time: {avg_waiting}")
print(f"Average Turnaround Time: {avg_turnaround}")
print(f"\nProcess Execution Sequence: {' -> '.join(str(p) for p in sequence)}")