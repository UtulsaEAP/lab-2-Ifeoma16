'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm-3:15pm
'''

def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    if len(str(phone_number)) != 10:
        print("Enter a 10-digit phone number. Restart")
    else:
        last_four = phone_number % 10000
        middle_three = (phone_number % 10000000) // 10000
        first_three = phone_number // 10000000
        print("({}) {}-{}".format(first_three, middle_three, last_four))
if __name__ == "__main__":
    telephone()