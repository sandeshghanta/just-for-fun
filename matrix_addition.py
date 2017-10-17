
matrix1 = []
matrix2 = []
result = []
for i in range(0,3):
    list1 = []
    for j in range(0,3):
        num = random.randint(0,9)
        list1.append(num)
    matrix1.append(list1)
for i in range(0,3):
    list1 = []
    for j in range(0,3):
        num = random.randint(0,9)
        list1.append(num)
    matrix2.append(list1)
for i in range(0,3):
    print matrix1[i],
    if i == 1:
        print " + ",
    else:
        print "   ",
    print matrix2[i],
    list1 = []
    for j in range(0,3):
        s = matrix1[i][j] + matrix2[i][j]
        list1.append(s)
    if i == 1:
        print " = ",
    else:
        print "   ",
    print list1
