import numpy as np

data = np.loadtxt("/home/apricot/Desktop/coef2.csv", delimiter=",")

data5 = data[:, 5]
data6 = data[:, 6]
i = 1

while i <= 40:
    f = open('/home/apricot/Desktop/result7.txt', 'a', encoding='utf-8')
    if i%8 == 1:
        f.write("{\n")
        f.write(str(data6[i-1]))
        f.write(",")
    elif (i%4 == 0) & (i%8 != 0):
        f.write(str(data6[i-1]))
        f.write(",\n")
    elif i%8 == 0:
        f.write(str(data6[i-1]))
        f.write("\n}\n")
    else:
        f.write(str(data6[i-1]))
        f.write(",")
        
    i+=1