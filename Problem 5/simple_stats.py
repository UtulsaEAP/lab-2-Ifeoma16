'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm-3:15pm
'''

def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''
    product = num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4)/4
    print(format(product, ".0f"), format(average, ".0f"))
    print(format(product, ".3f"), format(average, ".3f"))
if __name__ == "__main__":
    simple_stats()