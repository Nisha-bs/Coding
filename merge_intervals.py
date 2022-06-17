#!/usr/bin/python3

intervals = [[1,3],[2,6],[8,16],[15,18]]
for pnt in range(len(intervals)-1):
    #print(intervals[pnt])
    list1 = []
    if intervals[pnt][1] >= intervals[pnt+1][0]:
        first = intervals[pnt][0]
        second = intervals[pnt+1][1]
        list1.append(first)
        list1.append(second)
        #print(list1)
        intervals.remove(intervals[pnt])
        intervals.remove(intervals[pnt])
        intervals.insert(pnt,list1)
        print(intervals)

