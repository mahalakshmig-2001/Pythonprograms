
#r-->read(read only not modify) 
# w-->write(write new information,modify existing information) 
# a-->append(can't modify the file can add some information at end of file) 
# r+-->read&write

#readable(returns boolean values)
employee_file = open("employee.txt","r")

print(employee_file.readable())

employee_file.close()

print("\n")

#read a file
employee_file = open("employee.txt","r")

print(employee_file.read())

employee_file.close()

print("\n")

#Reading a single line in a file
employee_file = open("employee.txt","r")

print(employee_file.readline()) #read first line
print(employee_file.readline()) #read second line

employee_file.close()

#Readlines(reads all the lines in the form of array)
employee_file = open("employee.txt","r")

print(employee_file.readlines())

employee_file.close()
