def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

filesList = ['figure1.txt', 'figure2.txt', 'figure3.txt', 'figure4.txt', 'figure5.txt', 'figure6.txt']
yourFile = {'figure1.txt'}

for i in filesList:
    with open(i) as fig:
        data = fig.readlines()
        print('Изображение', i, int(len(data) - 2), 'x', int(len(data[3])/2), 'пикселей. \t(', toFixed((len(data)-2)/3, 2), 'x', toFixed(((len(data[3])-1)/2)/3, 2), ' мм.)', end="\n")