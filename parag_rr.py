chart=[]
class process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.arrival = at
        self.burst = bt

def shiftCL(alist):
    temp = alist[0]
    for i in range(len(alist)-1):
        alist[i]=alist[i+1]
    alist[len(alist)-1]=temp
    return alist

def rr(tq,plist,n):
    global chart
    queue=[]
    time=0
    ap=0
    rp=0
    done=0
    q=tq
    start=0
    while(done<n):
        for i in range(ap,n):
            if time>=plist[i].arrival:
                queue.append(plist[i])
                ap+=1
                rp+=1

        if rp<1:
            chart.append(0)
            time+=1
            continue

        if start:
            queue = shiftCL(queue)

        if queue[0].burst>0:
            if queue[0].burst>q:
                for g in range(time, time+q):
                    chart.append(queue[0].pid)
                time+=q
                queue[0].burst-=q
            else:
                for g in range(time, time+queue[0].burst):
                    chart.append(queue[0].pid)
                time+=queue[0].burst
                queue[0].burst=0
                done+=1
                rp-=1
            start=1
plist=[]
plist.append(process(1,0,250))
plist.append(process(2,0,170))
plist.append(process(3,0,75))
plist.append(process(4,0,100))
plist.append(process(5,0,130))
plist.append(process(6,0,50))


rr(5,plist,len(plist))

print(chart)
