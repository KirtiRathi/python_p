from steganography.steganography import Steganography
from datetime import (datetime)
from new import add_status  # from new file import the add_status function
from userdetail import Spy,chatmessage,spy,user_friend


friends=["juhi","davi","savita","jyoti","sudiksha","anu","swati"]# list of friends
def add_friend(): # define function for add new friend
 #   new_friend={
  #      "name":" ",
   #     "salutation":" ",
    #    "age":0,
     #   "rating":0.0
    #} #make a dictionary for add new friend
    new_friend = Spy('', '', 0, 0.0)
    new_friend.name=raw_input("please add your friend name:")
    if len(new_friend.name) > 0:
       new_friend.salutation=raw_input("are they MR. or MS. ?:")
       if(new_friend.salutation.upper()) == "MR" or (new_friend.salutation.upper()) == "MS":
          new_friend.name=new_friend.salutation+" "+new_friend.name
          new_friend.age=int(raw_input("age:"))
          if new_friend.age > 12 and new_friend.age<50:
              new_friend.rating=float(raw_input("enter your rating:"))
              if type(new_friend.rating)==float:
                print("your friend name is %s and age is %s with the rating %s")  %(new_friend.name,new_friend.age,new_friend.rating)
                friends.append(new_friend)
                return len(friends)
              else:
                print("sorry ! invalid entry.we can't add spy with detail you provided")
                return len(friends)

          else:
           print("please enter valid age")
       else:
        print("please enter the valid salutation")
    else:
      print("enter the name please")

    #if len(new_friend['name']) > 0 and (new_friend['age'] > 12 and new_friend < 50):
     # friends.append(new_friend)
      #return len(friends)

    #else:
     #   print("sorry ! invalid entry.we can't add spy with detail you provided")
      #  return len(friends)

def select_friend(): #define function for add new friend
    item_number=0
    for temp in friends:
      print ('%d %s' %((item_number+1),temp))
      item_number=(item_number+1)
    friend_choice=int(raw_input("choice from your friends\n"))
    if len(friends)>=friend_choice:
        friend_choice_position=int(friend_choice)-1
        return friend_choice_position
    else:
        print("please choose the friend again")





#new_chat = {         #create dictionary
 #   "message": 'text',
  #  "time": datetime.now(),
   # "send_by_me": True
    #    }
def send_message():# define function for send secrect message to friend
     friend_choice = select_friend()
     original_image = raw_input(" what is the name of the image?")
     output_path="output.jpg"#image with image extension
     text = raw_input("what do you want to say?")
     Steganography.encode(original_image,output_path, text)
     new_chat=chatmessage(text,True)

     user_friend.append(new_chat)
     print("your secret message has been ready!")

def read_message():# define function to read a secrect message send by another person to the user
            sender=select_friend()
            file_n = raw_input("Enter File Name:")
            file_e = raw_input("Enter File extension without .")
            full_path = ("%s.%s") % (file_n, file_e)
            secret_text = Steganography.decode(full_path)
            print("%s Mesaage in image named:  ") % (full_path)
            print secret_text
           # new_chat = {            #    "message": secret_text,
             #   "time": datetime.now(),
              #  "send_by_me": False

            #}
            new_chat=chatmessage(secret_text,False)
            user_friend.append(new_chat)
            print("your secret message has been saved!")


def read_chat_history():#define function to read history of the chat
    read_for = select_friend()
    print '\n6'
    for chat in user_friend[read_for].chats:
        if chat.sent_by_me:
            print("[%s]%s:%s"%(chat.time.strftime("%d %B %Y"),"you said :",chat.message))
        else:
            print("[%s]%s said:%s"%(chat.time.strftime("%d %B %Y"),user_friend.name,chat.message))









def start_chat():       #start_chat function define

   menu=("what do you want to do \n 1.add a status update \n 2.add a friend \n 3.select a friend \n 4.send a message \n 5.read a message \n 6.read chat history \n")
   menu_choice=int(raw_input(menu))                 #take input from user

   if(menu_choice)==1:                   #if-elif condition are apply
       add_status(current_status_message)    #calling add_status function

   elif(menu_choice)==2:
       add_friend()                          #calling the add_friend function

   elif(menu_choice)==3:
       select_friend()                            #calling the select_friend function
   elif(menu_choice)==4:
       send_message()                                 #calling the send_message function
   elif(menu_choice)==5:
       read_message()                                      #calling the read_message function
   elif(menu_choice)==6:
       read_chat_history()                                    #calling the read_chat_history

   else:
        print("try again later")
current_status_message = None
#start_chat function end










