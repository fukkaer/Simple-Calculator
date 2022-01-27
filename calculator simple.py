#No Error Correction
#Ver 1.00
#Unintuitive design
def sum(x,y):
    result = x + y
    return result
def sub(x,y):
    result = x - y
    return result
def mult(x,y):
    result = x * y
    return result
def div(x,y):
    result = x / y
    return result
print('Calculator v.1.00\n\nCan use 2 numbers Max\n')
loop = True
while loop == True:
    print('\n\n')
    userwrote_1 = int(input(" give 1st number: "))
    userwrote_2 = int(input(" give 2nd number: "))
    print('\n\nCalculation options:\n(1)Addition\n(2)Subtraction\n(3)Multiplication\n(4)Division\n(5)Quit\n\n')
    select = int(input("select calculation type: "))
    if select == 1:
        print("the result is:", end=' ')
        print(sum(userwrote_1,userwrote_2))
    elif select == 2:
        print("the result is:", end=' ')
        print(sub(userwrote_1,userwrote_2))
    elif select == 3:
        print("the result is:", end=' ')
        print(mult(userwrote_1,userwrote_2))
    elif select == 4:
        print("the result is:", end=' ')
        print(div(userwrote_1,userwrote_2))
    elif select == 5:
        loop = False
else:
    input('Press ENTER to Exit')
