'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm-3:15pm
'''

def right_arrow():
    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    ''' Type your code here. '''
    row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char \
            + head_char
    row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char \
            + head_char + head_char
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()