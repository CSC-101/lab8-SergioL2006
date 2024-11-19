import sys

def file():
    #Opens the file
    file = open(sys.argv[1], "r")
    #Puts content into variable(like list)
    content = file.readlines()

    #Iteratest through each lines
    for i in range(len(content)):
        #Checks if it is capable of adding the two expected values then prints
        try:
            eachline = float(content[i].split(" ")[0]) + float(content[i].split(" ")[1])
            print(eachline, " For line: ", i)
        #if it does not work then will add the error code for the line
        except:
            print("Error Line: ", i)
    #closes file after being read
    file.close()

print(file())