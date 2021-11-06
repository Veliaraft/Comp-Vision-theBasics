a = ['img1.txt', 'img2.txt']

with open(a[0]) as img1:
    with open(a[1]) as img2:
        data1 = img1.readlines()
        data2 = img2.readlines()
i = 0
while data1[i]==data2[i]:
    i+=1
j = i
while max(data2[j]) > max(data1[i]):
    i+=1
while max(data1[i]) > max(data2[j]):
    j+=1

if i > j:
    print(a[0], 'смещён по y на', i-j)
elif j>i:
    print(a[1], 'смещён по y на', j-i)
else:
    print('Смещения по y нет.')

k, o = 0, 0
while data1[i][k]!='1':
    k+=1
while data2[j][o]!='1':
    o+=1
if k > o:
    print(a[0], 'смещён по x на', int((k-o)/2))
elif o > k:
    print(a[1], 'смещён по x на', int((o-k)/2))
else:
    print("Смещения по x нет")