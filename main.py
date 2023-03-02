'''
Main file
========



'''


def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
     fp=open('data.txt','a')
     n=input("Enter the name :")
     mn=input("Enter the number :")
     res=validate_mob(mn)
        
     if res==1:
         a,b=searchmob(mn)
         if b==1:
             print("Number Already Exist")
         else:
             d=n+":"+mn+"\n"
             fp.write(d)
             fp.close()
             print("Contact Created successfully !!!!")
     else:
         print("Please enter valid mobile ")

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("")
    print("=========== Contact Directory ===========")
    print()
    print(d)

def searchmob(n):
          
           fp=open('data.txt','r')
           data=fp.readlines()
           for x in data:
               l=x.split(":")
               if  int (n)==int (l[1]):
               # print(x)

                return x,1
           else:
                return '',0

def searchname():
            print("Search contact number by name :")
            ns=input("Enter name :")
            fp=open('data.txt','r')
            data=fp.readlines()
            print()
            print(data)
            flag=0
            for x in data:
                l=x.split(":")
                if ns.upper ()==l [0] .upper ():
                 print(x)
                flag=1
            if flag==0:
             print("Contact Not found..")
             fp.close()
    
      

    
    
print("Wel - Come to contact Directory console Application ")
print()

while True :
    
    print()
    print()
    print("1.Create contact")
    print("2.View contact ")
    print("3.Search by name")
    print("4.Search by mobile number ")
    print("5.Exit")
    print()
    print()
    ch=int(input("Enter your choice :"))

    if ch==1:
          create_contact()
    elif ch==2:
          display()
    elif ch==3:
        searchname()
    elif ch==4:
        ms=input("Enter mobile number to be searched :")
        a,b=searchmob(ms)
         # print(a)
         # print(b)
        if b==1:
              print(" Contact Found :")
              print(a)
        else:
              print("RECORD NOT FOUND......!!! ")
    elif ch==5:
          break

    else:
            print("Please enter valid options...")
       
print("Thank you for using Aplication ")
