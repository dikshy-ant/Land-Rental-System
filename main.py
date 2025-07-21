import operations
import write
import read
import display

def main():
    
    data = read.readfile()

    print("\t|--------------------------------------|")
    print("\t|The information of TechnoPropertyNepal|")
    print("\t|--------------------------------------|")
   
   
    display.displayLand()

    KeepRunning = True
    while KeepRunning:
        print("|-------------------------------|")
        print("|Enter 1 to Rent a Land         |") 
        print("|-------------------------------|")
        print("|Enter 2 to return Land         |")
        print("|-------------------------------|")
        print("|Enter 3 to exit the System     |")
        print("|-------------------------------|")


        userOption = int(input("Enter a Value here"))
        customerRent = [] 
        customerReturn = [] 
        if userOption == 1:
            
           renting = True
           while renting:
            kittaNumber = operations.validateKittaRent(data)
            print(kittaNumber)
            customerName = input("Enter your name: ")
           
           
            operations.rentLand(data, kittaNumber,customerName )

            if customerName not in customerRent:
               write.rentInvoice(data, customerName,  kittaNumber)
               customerRent.append(customerName)
               (customerName + " has Rented Land")
            elif  customerName in customerRent:
                write.rentadd(data, customerName,  kittaNumber)
                print(customerName + " has Rented Land")
            
                operations.addTotal(customerName,data)
                print(operations.addTotal(customerName,data))
           

            userContinue = input("Do you want to Continue: ")
            if userContinue == "no":
               renting = False
            elif userContinue == "yes":
               renting = True
          
          
        elif userOption == 2:
           renting = True
           while renting:
            kittaNumber = operations.validateKittaReturn(data)
            print(kittaNumber)
            customerName = input("Enter your name: ")
            
            
            operations.returnLand(data,kittaNumber)
            if  customerName not in customerReturn:
                 
              write.returnInvoice(data, customerName,kittaNumber)
              customerReturn.append(customerName)

              print(customerName+"Has Returned Land")

            elif customerName in customerReturn:
                 
             write.returnAdd(data,customerName,kittaNumber)
             print(customerName + "Has Returned SAME NAME Land")

            userContinue = input("Do you want to Continue")
            if userContinue == "no":
               renting = False
            elif  userContinue == "yes":
                 renting = True    

        elif userOption == 3:
           
           print("You are exiting the system")
           print("|-------------------------------|")
           print("| PLEASE COME AGAIN             |")
           print("|-------------------------------|")
           KeepRunning = False
        else:
           
           print("Enter valid input Only 1, 2 or 3")
main()