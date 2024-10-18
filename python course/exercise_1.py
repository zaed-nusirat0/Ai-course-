list_operations=['+','-','*','/','%']
def sum(num1,num2):
   return f"{num1} + {num2} = {num1+num2}" 
 
def subtraction (num1,num2):
   return f"{num1} - {num2} = {num1-num2}" 

def multiplication (num1,num2):
   return f"{num1} * {num2} = {num1*num2}" 

def divide (num1,num2):
     return f"{num1} / {num2} = {num1/num2}" 
  
def mode (num1,num2):
     return f"{num1} % {num2} = {num1%num2}" 
Flag=True
while Flag :
   num1=float(input("enter the number 1 : ".title()))
   num2=float(input('enter the number 2 :'.title()))

   choice=input('Enter the calculate operation : '.title())
   if  choice in  list_operations:
      if choice=='+':
         print(sum(num1,num2))
      elif choice=='-':
         print(subtraction(num1,num2))
      elif choice=='*':
         print(multiplication(num1,num2))
      elif choice=='/':
         print(divide(num1,num2))
      elif choice=='%':
         print(divide(num1,num2))
   else:
      print('good by system Not found operation in list operation'.title())
      Flag=False
