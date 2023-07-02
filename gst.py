print("Welcome to GST calculator")
print("Enter the amount")
amount = int(input())
print("Enter the GST rate")
gst = int(input())
base_price = amount * 100 / (100 + gst)
cgst = base_price * gst / 2/100
sgst = base_price * gst / 2/100
print("Base price = ", round(base_price,2))
print("CGST = ", round(cgst,2))
print("SGST = ", round(sgst,2))
print("Total price = ", round(base_price + cgst + sgst,2))
:x

