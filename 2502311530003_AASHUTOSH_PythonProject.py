print("==================================================")
print("   SMARTCAMPUS UTILITY & ASSES PASS GENERATOR   ")
print("==================================================")
category=int(input("select user category(1: Student,2: Faculty/staff) :"))
if category == 1:
    sub_category = input("Enter sub-category(UG/PG) :")
    if sub_category =="UG":
        base_fee = 500
    elif sub_category =="PG":
        base_fee = 350
    else:
        print(" Invalid sub_category (UG/PG)")

elif category == 2:
    sub_category = (input("Enter sub_category (Residential/Visiting) :"))
    if sub_category == "Residential":
        base_fee = 800
    elif sub_category =="Visiting":
        base_fee =1200
    else:
          print("Invalid sub_category")
else:
    print("Invalid category")


discout = 0
if category == 1:
    cgpa = float(input("Enter student cgpa :"))
    if cgpa >= 8.5:
       discount = base_fee* 20/100
    elif cgpa >= 7.5:
            discount = base_fee *10/100
    elif category == 2:
            year = int(input("Enter year of service :"))
            if year > 10:
                dscount = base_fee *15/100
                 
parking = int(input("Enter parking option (0-None, 2-Two wheeler, 4-four wheeler) :"))
if parking == 0:
        parking_fee = 0
elif parking == 2:
        parking_fee = 200
elif parking == 4:
        parking_fee = 600
else:
     print("Invalid parking option ")

peak_surcharge = 0
if category == 1 and parking == 4:
    peak_surcharge = 150

units = float(input("Enter per month electricity consume (in khw) :"))
if units < 0:
    print("No electricity consume ")
if units <= 100:
    electricity_bill = units * 3 + 50
elif units <= 300:
    electricity_bill = ((100*3) + ((units - 100)*5) +100)
elif units <= 500:
    electricity_bill = ((100*3) + (200*5)+ ((units-300)*7.5)+150)
else:
    electricity_bill = ((100*3) + (200*5) + (200*7.5)+((units-500)*10) + 250)

net_pass_fee = base_fee - discount
net_pass_parking = net_pass_fee + parking_fee + peak_surcharge
total_pay = net_pass_parking + electricity_bill

print()
print("--------------------------------------------")
print("   CALCULATED INVOICE BREAK DOWN ")
print("--------------------------------------------")
print(f"Base Asses Pass Fee :{base_fee:.2f}")
print(f"Discount:{discount:.2f}")
print(f"Parking Fee :{parking_fee:.2f}")
print(f"Peak Surcharge :{peak_surcharge:.2f}")
print("--------------------------------------------")
print(f"Net Pass & Parking & Parking total: {net_pass_parking:.2f}")
print(f"Electricity Bill :{electricity_bill:.2f}")
print("--------------------------------------------")
print(f" TOTAL MONTHLY PAY :{total_pay:.2f}")
print("============================================")