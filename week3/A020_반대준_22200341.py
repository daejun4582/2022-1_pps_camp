max = -99
total = 0
for i in range(4):
    outbus,inbus = list(map(int,input().split()))
    total -= outbus
    total += inbus
    if max< total:
        max = total
print(max)
    