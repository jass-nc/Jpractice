print("Welcome to GST calculator") #Greeting user
print("Enter the amount") #Taking input from user on amount
amount = int(input()) 
Is_igst = input("Is the transaction interstate? (y/n)") #taking input from user on interstate transaction
if Is_igst == "y":
    print("Enter the IGST rate") #taking input from user on igst rate
    gst = int(input())
    base_price = amount * 100 / (100 + gst) #calculating the base price
    igst = base_price * gst / 100 #calculating igst
    print("Base price = ", round(base_price,2))
    print("IGST = ", round(igst,2))
    print("Total price = ", round(base_price + igst,2))
else:
    print("Enter the GST rate") #taking input from user on gst rate
    gst = int(input())
    base_price = amount * 100 / (100 + gst) #calculating the base price
    cgst = base_price * gst / 2/100 #calculating central tax
    sgst = base_price * gst / 2/100 #calculating state tax
    print("Base price = ", round(base_price,2)) 
    print("CGST = ", round(cgst,2))
    print("SGST = ", round(sgst,2))
    print("Total price = ", round(base_price + cgst + sgst,2))


