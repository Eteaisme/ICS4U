myList = []
oddNumbers = 0
evenNumbers = 0
for i in range(10): 
  myList.append(int(input("Enter an Integer: ")))
  if((myList[i] % 2) == 0):
    evenNumbers += 1  
  else:
    oddNumbers += 1


print("\nThe sum of the array is :", sum(myList))  
print("The average value of the array is:", (sum(myList)/len(myList)))  
print("The highest value is: ", max(myList))  
print("The lowest value is: ", min(myList))  
print("The amount of odd numbers: ", oddNumbers)
print("The amount of even numbers: ", evenNumbers)