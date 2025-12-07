# todoitems=input("Enter item to add")
# if todoitems:
#     print(todoitems)
# else:
#     print('No input provided')
todolist=[]
i=1
while i >0:
    todolist.append (input("Enter todo items"))
    if todolist[i-1]:
        i+=1
    else:
        i=0
print("Your todo list is:")
print("------------------")
for j in range(len(todolist)):
       print(todolist[j])
    


