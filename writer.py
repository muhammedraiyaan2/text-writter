print("Hi Welcome to the writer software")
input1=input("Enter the path: ")
input2=input("Enter the text: ")
root=open(input1,"a")
root.write(input2)
root.close()