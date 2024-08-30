l = [1,7,0,8,0,4,0,325,6,5,3,1-1,0,340,0,6,0,3,0,2,2,1]

for i in range(len(l)):
    if l[i] == 0:
        l.append(l[i])
        l.remove(l[i])
        count = l.count(0)

print(l)
print(count)
