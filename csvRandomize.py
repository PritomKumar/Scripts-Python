import random
f = open("sheet1.csv", "r")

# print(f.read())

lines = f.readlines()
file1 = open('myfile.csv', 'w') 

count = 0
for line in lines: 
    count +=1
    # print("Line{}: {}".format(count, line.strip())) 
    line = line.strip()
    if(line == "More than 32"):
        line = "33-50"
    splittedLine  = line.split('-')
    # print(splittedLine)
    randomInt = random.randint(int(splittedLine[0]),int(splittedLine[1]))
    # print(randomInt)
    file1.write(str(randomInt) + "\n") 



file1.close() 