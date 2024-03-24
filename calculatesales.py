
def calculate_sales(sales_per_week):
    total_sales = sum(sales_per_week) * 4  # Assuming 4 weeks in a month
    commission = 0
    remarks = ''


    if total_sales >= 80000:
        remarks = 'Excellent'
        commission = total_sales * 0.05
    elif total_sales >= 60000:
        remarks = 'Good'
        commission = total_sales * 0.05
    elif total_sales >= 40000:
        remarks = 'Average'
        commission = total_sales * 0.05
    else:
        remarks = 'Work Hard'


    return total_sales, commission, remarks




totaldetail=[]
n=int(input("Enter no of Salesmen : "))
for i in range(n):
    name=input("Enter name : ")
    singledetail=[]
    for j in range(4):
        s=int(input(f"Enter sales for week {j+1} : "))
        singledetail.append(s)
    t,c,r=calculate_sales(singledetail)
    totaldetail.append((name,singledetail,t,c,r))


print("details")
print(totaldetail)










