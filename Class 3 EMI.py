P=float(input("Amulya's Principle Amt="))
r=float(input("Interest Rate="))
n=float(input("Number of months="))
EMI=((P*r)*(1+r)**n)/((1+r)**n-1)
print (EMI)
