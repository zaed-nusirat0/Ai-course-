list_operations=['+','-','*','/','%']
def Calculator(symbol,input1,input2,):
     if symbol=='+':
        print('addition :',end=' ')
        print(f"{input1} {symbol} {input2} = {input1+input2}")

     elif symbol=='-':
        print('subtraction :',end=' ')
        print(f"{input1} {symbol} {input2} = {input1-input2}")

     elif symbol=='*':
        print('multiplication :',end=' ')
        print(f"{input1} {symbol} {input2} = {input1*input2}")

     elif symbol=='/':
        print('division :',end=' ')
        print(f"{input1} {symbol} {input2} = {input1/input2}")
     else :
        print('modulus :',end=' ') 
        print(f"{input1} {symbol} {input2} = {input1%input2}")
        
Flag=True
while Flag:
     symbol,n1,n2=input('Entar the input for function Calculator : '.title()).split()
     if symbol in list_operations:
          Calculator(symbol,int(n1),int(n2))


     else:
      Flag=False
      print('not found operations in math .'.title())
if Flag==False:
     print('Good by Calculator')