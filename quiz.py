import random # import someone elses library for generating random numbers - we don't want to write this ourselves.
score = 0
correctanswer = True # This is a Boolean - True or False, 0 or 1.
questions = [["What continent did Christopher Columbus Discover","America"],["In which city is Nelson's Column","London"],["What is the Capital city of France","Paris"]]
while correctanswer:
    questionnumber = random.randint(0,len(questions)-1) # There's no need to track the number of questions in Python - Python will do this for us
    answer = raw_input(questions[questionnumber][0]+"? ") 
    if (answer == questions[questionnumber][1]):
        print("Well Done")
        score = score + 1 
    else:
        correctanswer = False
        print ("No - the correct answer is "+questions[questionnumber][1]) 
print("You scored "+str(score))