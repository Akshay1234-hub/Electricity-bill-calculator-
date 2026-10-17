print("current bill checker")
units=int(input("enter your bill"))
if units<=100:
    print("no bill")
elif units<=200:
    bill=(units-100)*5
    print("bill :-",bill)
else:
    bill=100*5+(units-200)*10
    print("bill:-",bill)
