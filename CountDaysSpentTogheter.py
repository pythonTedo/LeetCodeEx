from datetime import datetime

def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    dtArriveA = datetime.strptime(arriveAlice, "%m-%d")
    dtLeaveA = datetime.strptime(leaveAlice, "%m-%d")
    dtArriveB = datetime.strptime(arriveBob, "%m-%d")
    dtLeaveB = datetime.strptime(leaveBob, "%m-%d")
    

    if dtLeaveA < dtArriveB or dtLeaveB < dtArriveA:
        return 0
    else:
        startdate = max(dtArriveA, dtArriveB)
        enddate = min(dtLeaveA, dtLeaveB)
        
        return (enddate - startdate).days + 1
    
arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"

print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))

'''
Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19.
They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
'''
