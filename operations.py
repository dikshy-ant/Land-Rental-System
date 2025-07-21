import read


#read data from the landata.txt file
data = read.readfile()

def displayAvailablelands(data):
    try:
        available = False
        availableLands = []
        for row in data:
            if row[5].strip() == "Available":
                availableLands.append(row)
                available = True

        if available:
            print("The available lands")
            print("\t|---------------------------------------------------------------------------|")
            print("\t|Kitta no | name of city | direction of Land |  Anna | Price | Availability |")
            print("\t|---------------------------------------------------------------------------|")

            for row in availableLands:
                kitta_no = row[0]
                nameCity = row[1]
                direction_land = row[2]
                land_anna = row[3]
                land_price = row[4]
                land_availability = row[5]

                print("\t", kitta_no, nameCity, direction_land, land_anna, land_price, land_availability)
        else:
            print("No lands are available for rent")
    except ValueError:
        print("Invalid Input")



#ensuring the kitta number entered is valid to rent land
def validateKittaRent(data):
    success = False
    kittaList = []
    
    while not success:
       
        for row_elements in data:
               
                if row_elements[5].strip() == "Available":
                    kittaList.append(int(row_elements[0].strip()))
                    
        print("Available kitta numbers:", kittaList) 
        try: 
            KittaNumber = int(input("Enter the kitta number: "))
            
            
            if KittaNumber < 0:
                print("Please enter a positive value")
            elif KittaNumber not in kittaList:
                print("Please enter a kitta number that is available")
            elif KittaNumber in kittaList:
                success = True
                print("Kitta number is valid")
                success = True
                return KittaNumber
        except ValueError:
            print("Invalid input")
    

def validateKittaReturn(data):
    success = False
    kittaList = []
    
    while not success:
       
        for row_elements in data:
               
                if row_elements[5].strip() == "Not Available":
                    kittaList.append(int(row_elements[0].strip()))
                    
        print("Available kitta numbers:", kittaList) 
        try: 
            KittaNumber = int(input("Enter the kitta number: "))
            
            
            if KittaNumber < 0:
                print("Please enter a positive value")
            elif KittaNumber not in kittaList:
                print("Please enter a kitta number that is available")
            elif KittaNumber in kittaList:
                success = True
                print("Kitta number is valid")
                return KittaNumber
            
        except ValueError:
            print("Invalid input")






#function to rent land 
def rentLand(data, KittaNumber,customerName):
   
   
    for row in data:
        try:
            kitta = int(row[0])
            if kitta == KittaNumber:
                row[5] = "Not Available"
                row[6] = customerName
              
                print("Land rented!!")
                break
        except ValueError:
            print("Invalid data in row:", row)
    
    with open("landdata.txt", "w") as file:
        for row in data:
            file.write(",".join(row) + "\n")
    

    
  




#function to sellland

def returnLand(data, KittaNumber):
   try: 
      for row in data:
        if int(row[0]) == KittaNumber:
            row[5] = "Available"
            row[6] = "Null"
            print("Land returned!!")
            break
   except ValueError:
            print("Invalid data")



   with open("landdata.txt","w") as file:
    for row in data:
        file.write(",".join(row) + "\n")
    
  



#adding the total cost of the lands borrowed 

def addTotal(customerName,data):
   
    total_price = 0
    for row in data:
        if row[6] == customerName:
            total_price += int(row[4])
  
    generate_invoice = "invoice_" + customerName + ".txt"
    with open(generate_invoice,"a") as file:
    
     file.write("Total Price of the rented lands are: " + str(total_price))
    
    return total_price





    
    





 



