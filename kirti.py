#print("hello world")
#print('what\'s up')
#print("who's you")
#var_a=raw_input("what is your : ")
#print("my name" +var_a+ "student of MCA: ")
#spy_salutation=raw_input("what should we call you(Mr or Ms.)?")
#print (spy_salutation +" "+ var_a)
#var_a=spy_salutation+" "+var_a
#print (len('hello'))
#if len(var_a)>0:
   # print("hello everyone")
#else:
    #print("not enter the name")
#var_b=("Mr or Ms")
#if(var_b)=="Mr" and (var_b)=="Ms.":
  #  print (spy_salutation + " " + var_a)
#
#else:
 #   print("it is not valid")

#var_c="juhi"
#if len(var_c)>0:
 #   com_a="this is right"
  #  print(com_a)

   # if len("computer")>10:
    #    print("this is nested if statement")
     #   print("it is like comment")
    #else:
     #   print("this is else statement")

#if len(" ")>0:
 #   print("this is empty if statement")
  #  print("it is another if statement")

#print("it is out of if statement")


#spy_rating=raw_input("what is your rating")
#print type(spy_rating)
#spy_rating=int(spy_rating)
#print type(spy_rating)
#spy_a=int(raw_input ("enter the first number"))
#spy_b=raw_input("ener the second number")
#spy_c=raw_input("enter the third number")

#if(spy_a)>(spy_b):
 #    print(spy_a)
#elif(spy_b)>(spy_c):
 #    print(spy_b)
#else:
 #    print(spy_c)

#from helper import var_k,var_l,var_n
#print("my name is %s and my age is %s and my rating are %s")%(var_k,var_l,var_n)


from demo import start_chat# import start_chat

print("welcome to spychat application")
temp=("do you want to continue as"+" "+"(Y\N):")
temp_choice=str(raw_input(temp))

if (temp_choice).upper()=="Y":          #if-elif condition are apply
    from helper import detail        # values are import from another file i.e helper
    start_chat()                   #start_chat function call

elif (temp_choice).upper()=="N":
        spy_age=0                #intilaising the variable
        spy_rating=0.0
        spy_is_online=False

        spy_name=raw_input("enter your name:")

        if  len(spy_name)>0 :                          #check that user can enter any name or not
           spy_salutation=raw_input("what we should call you(MR or MS)? :")
           if(spy_salutation).upper()=="MR" or (spy_salutation).upper()=="MS":
              spy_name = spy_salutation + " " + spy_name
              print("hello %s you welcome in the spychat") % (spy_name)



              spy_age=raw_input("please enter your age:")
              spy_age=int(spy_age)                            #change the string into integer

              if spy_age>12 and spy_age<50:
                 spy_rating=raw_input("please provide your rating:")
                 spy_rating=float(spy_rating)                 #change the string into float

                 if spy_rating>4.5:
                   print("greate one keep it up")

                 elif spy_rating>=3.4 and spy_rating<=4.5:
                   print("you are the good one")

                 elif spy_rating>=2.4 and spy_rating<=3.5:
                   print("you can always do better")
                 else:
                   print("you can use someone in office")
                 spy_is_online=True
                 print("authantication is complete.welcome %s age %s rating %s proud to have on board")%(spy_name,spy_age,spy_rating)
                 start_chat()                    #calling the start start_chat function

              else:
                  print("it is not valid")
           else:
             print("you are not eligable to become a spy")
        else:
          print("enter the name")
else:
       print("please try again later")










