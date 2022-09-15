num = int(input("Enter number of integers to be generated: "))
num_list = []
for i in range(num):
    i = int(input())
    num_list.append(i)

print("max:" , max(num_list))
print("min:" , min(num_list))

#avg = sum(num_list)/len(num_list)
#print("The average is ", round(avg,2))

sum = 0
for num in num_list:
    sum += num
average = sum / len(num_list)
print("The average of num_list is ",average)

    






  
    
   
    
