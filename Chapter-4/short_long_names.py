msg = input('Enter your name: ')
count = len(msg)
if count >=9:
    print('Hi ' +msg+', you have a long name')
elif count <=3:
    print('Hi' +msg+', you have a short name')
elif count >=4:
    print('Hi'+msg+', nice to meet you')