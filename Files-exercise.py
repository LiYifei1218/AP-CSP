total = 0.0
num = 0
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.split() # change the string into list
        level = float(line[1])
        total += level
        num += 1
average = total/num
print("average = " + str(average))
