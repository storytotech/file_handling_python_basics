# x = input("enter your name")
# print(x)
# with open("name.txt","a") as f:
#     f.write(x + "\n")
#     print("name saved succesfully")



# def main():
#     x = input("enter your name")
#     with open("name.txt", "a") as f:
#         f.write(x + "\n")
#     print
    
def write_to_file(filename,x):
    try:
        with open(filename , "a") as f:
             f.write(x + "\n")
        print("saved succesfully")
            
       
    except Exception as e:
        print("any error",e)
        
    
def main():
    
    x = input("enter your name")
    write_to_file("name.txt",x)
main()