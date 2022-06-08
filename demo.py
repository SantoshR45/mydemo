a=int(input("enter your credit score - "))
price = 100000
if a >= 790:
    print("Your credit score is excellent and your down payment is $", 0.14*price)
elif a < 790 and a >= 710:
    print("your credit score is good so your down payment is $", 0.29 * price)
elif a<710 and a>=650:
    print("your credit score is average so your down payment is $", 0.36*price)
else:
    print("As your credit score is poor, you are not eligible for this offer but if you are still interested to buy then your minimum down payment is $", 0.65*price)
