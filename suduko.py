#Generates a 9*9 grid such that no two elements along any row or collum or diagonal are the same


import random
def element_status(list_full,i):
    for j in list_full:
   	 if i == j:
   		 return True
    return False
def remove_elements(list2,answer_list,answer):
    list_full = [1,2,3,4,5,6,7,8,9]
    for i in list2:
   	 j = i[1]
   	 row = answer_list[j]
   	 value = row[i[0]]
   	 list_full.remove(value)
    if len(answer) == 0:
   	 return list_full
    else:
   	 for i in answer:
   		 if element_status(list_full,i):
   			 list_full.remove(i)
   	 return list_full
def createlist(i,j,answer,answer_list):
    list_full = [1,2,3,4,5,6,7,8,9]
    list1 = []
    list2 = []
    if len(answer) ==  0:
   	 for y in range(0,j):
   		 list1.append(i)
   		 list1.append(y)     
   		 list2.append(list1)
   		 list1 = []
   	 list_full = remove_elements(list2,answer_list,answer)
   	 return list_full
    else:
   	 for y in range(0,j):
   		 list1.append(i)
   		 list1.append(y)
   		 list2.append(list1)
   		 list1 = []
   	 list1 = []   				 
   	 list3 = []
   	 if i%3 == 0 and j%3 == 0:
   		 just_to_do_something = 1
   	 elif i%3 == 1 and j%3 == 1:
   		 list1 = [i-1,j-1]
   		 list2.append(list1)
   	 elif i%3 == 2 and j%3 == 1:
   		 list1 = [i-2,j-1]
   		 list2.append(list1)
   		 list1 = [i-1,j-1]
   		 list2.append(list1)
   	 elif i%3 == 1 and j%3 == 2:
   		 list1 = [i-1,j-2]
   		 list2.append(list1)
   		 list1 = [i-1,j-1]
   		 list2.append(list1)
   	 elif j%3 == 2 and i%3 == 2:
   		 list1 = [i-2,j-2]
   		 list2.append(list1)
   		 list1 = [i-1,j-1]
   		 list2.append(list1)
   		 list1 = [i-1,j-2]
   		 list2.append(list1)
   		 list1 = [i-2,j-1]
   		 list2.append(list1)
   	 list_full = remove_elements(list2,answer_list,answer)
   	 return list_full
list_full = [1,2,3,4,5,6,7,8,9]
answer = []
answer_list = []
for j in range(0,9):
    if j == 0:
   	 for i in range(0,9):
   		 value = random.choice(list_full)
   		 answer.append(value)
   		 list_full.remove(value)
   	 answer_list.append(answer)
    else:
   	 answer = []
   	 successful = 0
   	 while successful != 8:
   		 for i in range(0,9):
   			 list_full = createlist(i,j,answer,answer_list)
   			 if len(list_full) == 0 :
   				 break
   			 else:
   				 value = random.choice(list_full)
   				 answer.append(value)
   				 successful = successful + 1
   			 answer_list.append(answer)
   	 print answer_list
