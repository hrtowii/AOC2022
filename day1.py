listNum = []
sumNumber = 0
with open("day1input.txt",'r') as readfile:
    for line in readfile:
        if line.strip():
            sumNumber += int(line)
            listNum.append(sumNumber)
        else:
            listNum.append(sumNumber)
            sumNumber = 0

print("the highest number is " + str(max(listNum)))

#part 2
#sort from largest to smallest
listNum.sort(reverse=True)
top3sum = listNum[0] + listNum[2] + listNum[4]
print("the sum of the three highest calories is " + str(top3sum))