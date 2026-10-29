def monthly_bills (bills :list [float] ):
  if  len(bills) > 0:
   avr_monthly_bills = sum(bills)/len(bills)
   return avr_monthly_bills 
  else:
    print ("please input the monthly bills")

l=monthly_bills([])
print(l)