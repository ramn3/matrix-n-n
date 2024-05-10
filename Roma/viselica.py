a = str(input())
k = len(a)
s = ''
for i in range(k):
    s = s + "*"
print(s)
b = str(input())
i = 0
while a != s:
    for i in range(len(a)):
        if a[i] == b:
            s = s[:i] + b + s[i+1:]
            print(a[i], b)
    print(s)
    if a == s:
        print('УРА!')
        break
    b = str(input())