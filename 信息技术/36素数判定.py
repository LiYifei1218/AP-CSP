n = int(input())
for i in range(n-1,1,-1):
    if n%i == 0:
        print("no")
        break
else:
    print("yes")