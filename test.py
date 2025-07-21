import read

data = read.readfile()

def addTotal(customerName,data):
  
    total_price = 0
    for row in data:
        if row[6] == customerName:
            total_price += int(row[4])
  
    
    generate_invoice = "invoice_" + customerName + ".txt"
    file = open(generate_invoice,"a")
    
    file.write("Total Price of the rented lands are: " + str(total_price))
    file.close()
    return total_price





