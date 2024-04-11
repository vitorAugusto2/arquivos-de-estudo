l1 = [1, 2, 4, 5, 6]
l2 = [1, 3, 4, 8, 10]
l3 = []

for i in range(len(l1)):
    if l1[i] != l2[i]:
        l3.append(l1[i])
        l3.append(l2[i])
    else:
        continue

print(f"l3 : {l3}")           