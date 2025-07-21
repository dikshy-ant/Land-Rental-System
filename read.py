def readfile():
    file = open("landdata.txt", "r")
    value=[]
    for row in file.readlines():
        row = row.replace("\n","").split(",")
        value.append(row)
    file.close()
    return value
print(readfile())

# Convert the content in landdata into a dictionary format 
def dic_cont(content):
    d1 = {}
    for i in range(len(readfile())):
        d1[i+1] = readfile()[i].replace("\n", "").split(",")
       
    return d1 
'''
def buy_land():
    content =  readfile()
    d2 = dic_cont() 
    print("\t|---------------------------------------------------------------------------|")
    print("\t|Kitta no | name of city | direction of Land |  Anna | Price | Availability |")
    print("\t|---------------------------------------------------------------------------|")

    for key, value in d2.items():
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3],"\t",value[4],"\t",value[5])

buy_land()

'''