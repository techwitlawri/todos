import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # get user input and strip space chars from it
    user_action=input('type add, show, edit,complete or exit: ')
    user_action= user_action.strip()

   
    if user_action.startswith('add'):
        todo= user_action[4:]
#[4:] is called list sslicing

        todos= functions.get_todos()

        todos.append(todo + "\n") 

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos=functions.get_todos()

        new_todo=[]
    #   for item in todos:
    #       new_item = item.strip('\n')
    #       new_todo.append(new_item)
        new_todo=[item.strip('\n') for item in todos]     

        for index,item in enumerate(new_todo):             
            item= item.strip('\n')
            row= (f"{index +1}-{item}")
            print(row)
                        
    elif user_action.startswith ('edit'):
        try: 
            number=int( user_action[5:])
            print(number)
            number = number -1

            todos=functions.get_todos()

            new_todo= input("Enter a new todo : ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
            

        except ValueError:
            print( " your command is not valid.")
            continue
        

    elif user_action.startswith('complete'):  
        try:
            number= int( user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove= todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
           

            message= f' {todo_to_remove} was removed from the list.'
            print(message)

        except IndexError:
            print(' there is no item with that number')
            continue
    elif user_action.startswith('exit'):
            break
    else:
        print("command is not vaild")    
   
print('bye')      