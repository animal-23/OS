def sjf(processes):
    n=len(processes)
    completion_time=[0]*n
    waiting_time=[0]*n
    turnaround_time=[0]*n
    #processes.sort(key=lambda x:x[1])
    completion_time[0]=processes[0][1]
    for i in range(1,n):
        completion_time[i]=completion_time[i-1]+processes[i][1]
    for i in range(n):
        turnaround_time[i]=waiting_time[i]+processes[i][1]
    for i in range(n):
        waiting_time[i]=completion_time[i]-processes[i][1]
    print("process\tcompletion time\t\t burst time\twaiting time\tTAT")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{completion_time[i]}\t\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print("gantt chart is:")
    print("p2|p3|p4|p5|p1")
    print("0"," ",completion_time[0]," ",completion_time[1]," ",completion_time[2]," ",completion_time[3]," ",completion_time[4])
processes=[("p1",10),("p2",1),("p3",2),("p4",4),("p5",5)]
sjf(processes)