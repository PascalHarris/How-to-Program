name = raw_input("What is your name? ")
print ("Hello "+name)
answer = raw_input("How are you feeling today? (well / unwell) ")
if (answer == "well"):
    print ("Good")
elif (answer == "unwell"):
    print ("I'm sorry to hear that") 
else:
    print ("I'm sorry, I didn't understand that.")