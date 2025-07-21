import datetime
import read
import operations

landlist = read.readfile()
#printing  the rent innvoice



def rentInvoice(landList, customerName, kitta_no):
    generate_invoice = "invoice_" + customerName + ".txt"
    file = open(generate_invoice,"w")
    file.write("\t|---------------------------------|\n")
    file.write("\t|           INVOICE               |\n")
    file.write("\t|---------------------------------|\n")
    file.write("Customer Name: " + customerName + "\n")
    
    file.write("Date of rent: " + str(datetime.datetime.now().year) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day) + "\n")

    for land in landList:
       if int(land[0]) == kitta_no:
           total_price2 = land[4] 
           file.write(total_price2)
     
    

   

    file.write("Rented Land Details:\n")
    file.write("|---------------------------------------------------------------------------|\n")
    file.write("|Kitta no | name of city | direction of Land |  Anna | Price | Availability |\n")
    file.write("|---------------------------------------------------------------------------|\n")

    
    for land in landList:
        if int(land[0]) == kitta_no:
            file.write(land[0] + "\t\t\t\t\t" + land[1] + "\t\t\t\t\t" + land[2] + "\t\t\t\t\t" + land[3] + "\t\t\t\t\t" + land[4] + "\t\t\t\t\t" + land[5] + "\n")
          
            break
   

#function to append to the invoice file if the same customer rents another land 
def rentadd(landList, customerName,  kitta_no):
    generate_invoice = "invoice_" + customerName + ".txt"
    file = open(generate_invoice,"a")
    
  
   
    file.write("Date of rent: " + str(datetime.datetime.now().year) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day) + "\n")
 
    
    
    for land in landList:
       if int(land[0]) == kitta_no:
           total_price = land[4] 
           file.write(total_price)


    
    file.write("Rented Land Details:\n")
    file.write("|---------------------------------------------------------------------------|\n")
    file.write("|Kitta no | name of city | direction of Land |  Anna | Price | Availability |\n")
    file.write("|---------------------------------------------------------------------------|\n")

    for land in landList:
        if int(land[0]) == kitta_no:
            file.write(land[0] + "\t\t\t\t\t" + land[1] + "\t\t\t\t\t" + land[2] + "\t\t\t\t\t" + land[3] + "\t\t\t\t\t" + land[4] + "\t\t\t\t\t" + land[5] + "\n")
            break
    file.write("|---------------------------------------------------------------------------|\n")

#function to calculate the cost of the two lands 


#function to generate invoice if the customer returns a land

def returnInvoice(landList, customerName, kitta_no):
    return_invoice = "invoice_ " + customerName + ".txt"
    file = open(return_invoice, "w")
    file.write("CustomerName " + customerName + "\n")
    file.write("Date of return: " + str(datetime.datetime.now().year) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day) + "\n")
   

    file.write("Land Details:\n")
    file.write("|---------------------------------------------------------------------------|\n")
    file.write("|                              BILL                                         |\n")
    file.write("|---------------------------------------------------------------------------|\n")
    
       
    for land in landList:
       if int(land[0]) == kitta_no:
           total_price = land[4] 
           file.write(total_price)

 

    file.write("Rented Land Details:\n")
    file.write("|---------------------------------------------------------------------------|\n")
    file.write("|Kitta no | name of city | direction of Land |  Anna | Price | Availability |\n")
    file.write("|---------------------------------------------------------------------------|\n")
     
     
   

    for land in landList:
        if int(land[0]) == kitta_no:
            file.write(land[0] + "\t\t\t\t\t" + land[1] + "\t\t\t\t\t" + land[2] + "\t\t\t\t\t" + land[3] + "\t\t\t\t\t" + land[4] + "\t\t\t\t\t" + land[5] + "\n")
            break
      

def returnAdd(landList, customerName, kitta_no):
    return_invoice = "invoice_ " + customerName + ".txt"
    file = open(return_invoice, "a")
   
    file.write("Date of return: " + str(datetime.datetime.now().year) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day) + "\n")
   

    for land in landList:
       if int(land[0]) == kitta_no:
           total_price = land[4] 
           file.write(total_price)

 

    file.write("Rented Land Details:\n")
    file.write("|---------------------------------------------------------------------------|\n")
    file.write("|Kitta no | name of city | direction of Land |  Anna | Price | Availability |\n")
    file.write("|---------------------------------------------------------------------------|\n")
     
     
   

    for land in landList:
        if int(land[0]) == kitta_no:
            file.write(land[0] + "\t\t\t\t\t" + land[1] + "\t\t\t\t\t" + land[2] + "\t\t\t\t\t" + land[3] + "\t\t\t\t\t" + land[4] + "\t\t\t\t\t" + land[5] + "\n")
            break
      





