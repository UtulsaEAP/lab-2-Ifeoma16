'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm-3:15pm
'''

def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    print("After 6 hours:", format((caffeine_mg/2), ".2f"), "mg")
    print("After 12 hours:", format((caffeine_mg/4), ".2f"), "mg")
    print("After 24 hours:", format((caffeine_mg/16), ".2f"), "mg")
    
if __name__ == "__main__":
    caffeine()