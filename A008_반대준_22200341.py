def psj(a):
    sum = 0
    num = a[0]
    ps = 0
    del a[0]

    for i in range(len(a)):
        sum += a[i]
    avg = sum / len(a)

    for num in a:
        if num > avg:
            ps += 1

    result = ps / len(a) * 100

    print(f'{result:.3f}%')

rp = int(input())

for _ in range(rp):
    a = input().split()
    a = list(map(int,a))
    psj(a)