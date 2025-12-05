#old method

# todolist=[]
# i=1
# while i >0:
#     todolist.append (input("Enter todo items"))
#     if todolist[i-1]:
#         i+=1
#     else:
#         i=0
# print("Your todo list is:")
# print("------------------")
# for j in range(len(todolist)):
#        print(todolist[j])
    
#old method ends here

#REcommended code from copilot
todolist = []

while True:
    item = input("Enter todo item (leave blank to stop): ")
    if item:
        todolist.append(item)
    else:
        break

print("\nYour todo list is:")
print("------------------")
for idx, task in enumerate(todolist, start=1):
    print(f"{idx}. {task}")













    