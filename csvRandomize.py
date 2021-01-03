f = open("sheet1.csv", "r")

# print(f.read())

lines = f.readlines()

count = 0
for line in lines: 
    count +=1
    # print("Line{}: {}".format(count, line.strip())) 
    line = line.strip()
    if(line == "More than 32"):
        line = "33-50"
    splittedLine  = line.split('-')
    print(splittedLine)

file1 = open('myfile.csv', 'w') 
file1.writelines("ffsdf") 
file1.close() 