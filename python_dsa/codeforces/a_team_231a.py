no_problems = int(input())
count = 0
for i in range(0, no_problems):
    a = input()
    if a.count("1") >= 2:
        count += 1

print(count)
