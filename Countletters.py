expr = input()
ch = expr[0]
cnt = 1
for i in range(1, len(expr)):
    if expr[i] == ch:
        cnt += 1
    else:
        print(ch, cnt, sep='', end='')
        ch = expr[i]
        cnt = 1
print(ch, cnt, sep='', end='')
