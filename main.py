
input1=dict(input('Insert a dictionary: '))


def calculateAverage(myFinalMarks):
    length=len(myFinalMarks)
    vals=myFinalMarks.values()
    total=0

    for i in vals:
        total=total+i
    average=total/length
    return average

print(calculateAverage(input1))
