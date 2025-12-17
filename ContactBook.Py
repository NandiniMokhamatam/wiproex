class use :
    
    def __init__(self,names,phone_numbers,num):
        self.phone_numbers=phone_numbers
        self.names=names
        self.num=num

###############################################################################################################################
   
    def add(self): 
        num=int(input("Enter how many numbers you want to add in the book : "))
        for i in range(num):
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ") 
            print("\n")
            names.append(name)
            phone_numbers.append(phone_number)  
            print("Contact saved sucessfully !\n\n")   

#################################################################################################################################
                        
    def search(self):
        search_term = input("\nEnter search term: ")
        print("Search result:")
        if search_term in names:
                index = names.index(search_term)
                phone_number = phone_numbers[index]
                print("Contact Found !!\n")
                print("Name: {}, Phone Number: {}\n\n".format(search_term, phone_number))
                
        else:
                print("Name Not Found, Try again\n") 

##################################################################################################################           

    def modify(self):
            search_t= input("\nEnter the name for modifying: ")
            ind=0
    
            if search_t in names: 
                ind = names.index(search_t)
                
            else :
                print("Contact not found, Please try again")               
            loc=ind
            print("Enter the following options")
            print("1.Update name\n2.Update Number\n")
            c=int(input("Enter your choice :"))
            if c==1 :
                str1=str(input("Enter Name :"))
                names[loc]=str1
            else :
                str2=int(input("Enter number :"))
                phone_numbers[loc]=str2

#####################################################################################################################################################
    
    def delete(self):
        delete_term = input("\nEnter delete term: ")
        print("\n")
        if delete_term in names:
            index = names.index(delete_term)
            names.remove(delete_term)
            phone_number = phone_numbers[index]
            phone_numbers.remove(phone_number)
            
            print("Contact Deleted sucessfully !!\n")
        else:
            print("Name Not Found, Try again\n") 

#####################################################################################################################################################
        
    def display(self):
        if len(names)==0:
            print("No Contacts Found\n")
        else :
            print("\nHere is the result\n")
            print("\nName\t\t\tPhone Number\n")
        for i in range(len(names)):
            print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
            print("\n")

##################################################################################################################################################################   


print("********* Welcome to Telephone Directory Book *********")
names = []
phone_numbers = []
num=0
u=use(names,phone_numbers,num)
a=1
while a:
    print("Select the following operations")
    print("1.Add a number\n2.Search a number\n3.Modify a number\n4.Delete a number\n5.Display contacts")
    option=int(input("Enter your choice :"))
    if(option==1):
        u.add()
    elif(option==2):
        u.search()
    elif(option==3):
        u.modify()
    elif (option==4):
        u.delete()
    elif(option==5):
        u.display()
    else :
        print("Invalid Option, Please choose the correct option again")
    a=int(input("Do want to continue ?, If yes press 1 or else press 0 :")) 
    print("\n") 

print("******** Thank You **********")
