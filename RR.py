def findWaiting(processes, n, bt, wt, quantum):
    rem_bt=[n];
    for i in range(0,n):
        rem_bt[i] = bt[i]
    t = 0
    i = 0
    while(1):
        done = true
        for i in range(0,n):
            if rem_bt[i] > 0:
                done = false
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done == true:
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(0,n):
        tat[i] = bt[i] + wt[i]

def findAvgTime(processes, n, bt, quantum):
    wt = [n]
    tat = [n]
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt, quantum)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes\t  Burst time\t  Waiting Time\t  Turn Around Time" )
    for i in range(0,n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(str(processes[i]+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
    #total_wt = float(total_wt)/n
    #total_tat = float(total_tat)/n
    print("Average waiting time is: "+str(float(total_wt)/n))
    print("Average turn around time is: "+str(float(total_tat)/n))        
    
def main():
    print("Enter the number of process: ")
    n=int(input())
    print(" Enter the quantum time: ")
    quantum=int(input())
    processes=[]
    bt=[]
    for i in range(0,n):
        processes.insert(i,i+1)
    print("Enter the burst time of the processes: ")
    bt = list(map(int, raw_input().split()))
    findAvgTime(processes, n, bt, quantum)
