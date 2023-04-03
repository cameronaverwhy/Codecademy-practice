#!/usr/bin/env python
# coding: utf-8

# The Quiz!

# In[1]:


print("Welcome to The Quiz! Hope you are ready for some serious general knowledge quizzing. Get as high a score as you can! First of all, would you mind telling me your name?")


# In[2]:


player_name = input("Player, what is your name?")
print("Hello, " + player_name + "! Get ready for some quizzing!")
print("You will be asked a series of multiple-choice questions, when selecting your answer, only provide the letter of your answer selection")


# In[3]:


class Quizmaster:
    def __init__(self, questions, answers, multiplechoice):
        self.questions = questions
        self.answers = answers
        self.multiplechoice = multiplechoice
    
    def __repr__(self):
        return '{'+ self.questions +', '+ self.answers +', '+ str(self.multiplechoice) +'}'


quiz_questions = [Quizmaster("Question 1: How many bones are there in the average adult human body?", "b", ["(a) 207", "(b) 206", "(c) 300", "(d) 270"]), 
                  Quizmaster("Question 2: What is the capital of Canada?", "a", ["(a) Ottawa", "(b) Toronto", "(c) Winnipeg", "(d) Banff"]),
                  Quizmaster("Question 3: In which Shakespeare play does a character compare the world to a stage?", "a", ["(a) As You Like It", "(b) The Merchant of Venice", "(c) A Winter's Tale", "(d) Hamlet"]),
                  Quizmaster("Question 4: How many human Herpesviruses are there?", "d", ["(a) 6", "(b) 8", "(c) 20", "(d) 9"]),
                  Quizmaster("Question 5: Which TV series was Netflix's number 1 watched show (by hours watched) in 2022?", "b", ["(a) The Sandman", "(b) Stranger Things", "(c) Wednesday", "(d) Bridgerton"])]


# In[4]:


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

player = Player(player_name)


# In[5]:


for question in quiz_questions:
    if (question.multiplechoice != None):
        print(f"{question.questions}")
        for option in question.multiplechoice:
            print(option)
        userAnswer = input()

    if (userAnswer.lower() == question.answers.lower()):
        print("That is correct!")
        player.score = player.score +1
    else:
        print(f"Sorry, that was wrong, the correct answer is {question.answers}")
    print("So far, " + player_name +", your score is " + str(player.score))


# In[6]:


print("Well done player! Your final score is " + str(player.score) + ". Thanks for playing!")

