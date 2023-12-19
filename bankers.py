def is_safe(processes, alloc, max, avail):
    n = len(processes)
    m = len(avail)
    work = avail.copy()
    finish = [False] * n
    need = [[max[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    safe_sequence = []
    while True:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += alloc[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    found = True
        if not found:
            break
    return all(finish), safe_sequence
n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))
processes = list(range(n))
print("Enter the allocation matrix:")
alloc = [list(map(int, input().strip().split())) for _ in range(n)]
print("Enter the max matrix:")
max = [list(map(int, input().strip().split())) for _ in range(n)]
avail = list(map(int, input("Enter the available resources: ").strip().split()))
safe_state, sequence = is_safe(processes, alloc, max, avail)
if safe_state:
    print("The system is in a safe state.")
    print("Safe Sequence:", " -> ".join(f"P{p}" for p in sequence))
else:
    print("The system is NOT in a safe state.")
