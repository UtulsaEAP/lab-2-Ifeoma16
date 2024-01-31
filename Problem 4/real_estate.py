'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm-3:15pm
'''

def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    price_change = current_price - last_month_price
    mortgage = (current_price * 0.051) / 12
    print("This house is", "$" + str(current_price) + ".", "The change is", \
           "$" + str(price_change), "since last month.")
    print("The estimated monthly mortgage is", "${:.2f}".format(mortgage) + ".")
if __name__ == "__main__":
    real_estate()