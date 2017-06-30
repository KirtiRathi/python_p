def start_chat(spy_name,spy_age,spy_rating):
     current_status_message = None


def add_status(current_status_message):#function create for add status
    if current_status_message!=None:
        print("your current status message is" +current_status_message+"\n")
    else:
        print("you don't have any status message currently")



    default=raw_input("do you want to select from the older status(Y/N)?")
    status_message = ['hello everyone','busy','urgent call only','at work','in a meeting','always smile']   #list of old message
    if default.upper()=="N":
        new_status_message=raw_input("what status message do you want to set ?")

        if len (new_status_message)>0 and (new_status_message)==status_message:
            update_status_message=new_status_message
            status_message.append(update_status_message)
        else:
            print("you don't enter any message or message is already avaliable")

    elif default.upper()=="Y":
            item_position = 1
            for message in status_message:
                print (str(item_position) + " " + message)
                item_position=(item_position +1)
            message_selection=int(raw_input("\n choice from the above message:"))

            if len(status_message)>=(message_selection):
                  update_status_message=str(status_message[message_selection-1])
                  print(update_status_message)
                  return  update_status_message
            else:
                   print("not correct")
            current_status_message=add_status(current_status_message)
    else:
      print("entry invalid")




