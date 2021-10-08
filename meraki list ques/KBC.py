

print("          -AIYE DEKHTE HAI KON BANEGA CROREPATI-          "            )
print("HOW TO PLAY - ")
print("you will be given four options for each question and you need to CHOOSE ONE option")
question_list=[ "How many continents are there?",              
     "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"  ]
options_list = [
    ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
lifelines=["50-50"]


q1_op1="1"
q1_op2="2"
q1_op3="3"
q1_op4="4"
q2_op1="1"
q2_op2="2"
q2_op3="3"
q2_op4="4"
q3_op1="1"
q3_op2="2"
q3_op3="3"
q3_op4="4"
print("SO HERE YOU GO WITH THE FIRST QUESTION")

print("QUESTION 1 - ")
print(question_list[0])
print("YOUR OPTIONS ARE : ")
for i in options_list[0]:
    print(i)
print("CHOOSE ONE OPTION")
# print("you have LIFELINE AS FOLLOWS : ")
print(" 50-50 is the only LIFELINE you have")
lifeline1=input("say yes if you want lifeline - ")
if lifeline1=="yes":
    print(options_list[0][2] , options_list[0][3])
answer1=input("enter the answer of the first question : ")
i=0
while i<1:
  if answer1==q1_op3:
    print("WOAH!! CORRECT ANSWER, YOU CAN MOVE FORWARD")
  else:
    print("ALAS!, WRONG ANSWER")
    break
  i+=1
print("QUESTION 2 - ")
print(question_list[1])
print("YOUR OPTIONS ARE : ")
for i in options_list[1]:
    print(i)
print("CHOOSE ONE OPTION")
print(" 50-50 is the only LIFELINE you have")
lifeline2=input("say yes if you want lifeline - ")
if lifeline2=="yes":
    print(options_list[1][2] , options_list[1][3])
# if lifeline<1:
#     print("you can't use lifeline again")
# else:
#     print("50-50 lifeline is available")
answer2=input("enter the answer of question 2 : ")
i=0
while i<1:
  if answer2==q2_op4:
    print("WOAH!! CORRECT ANSWER, YOU CAN MOVE FORWARD")
  else:
    print("ALAS!, WRONG ANSWER")
  i+=1
print("QUESTION 3 : ")
print(question_list[2])
print("YOUR OPTIONS ARE : ")
for i in options_list[2]:
    print(i)
print("CHOOSE ONE OPTION")
print(" 50-50 is the only LIFELINE you have")
lifeline3=input("say yes if you want lifeline - ")
if lifeline3=="yes":
    print(options_list[2][0] , options_list[2][3])
answer3=input("enter the answer of question 3 : ")
i=0
while i<1:
  if answer3==q3_op1:
    print("WOAH!! CORRECT ANSWER")
  else:
    print("ALAS!, WRONG ANSWER")
  i+=1
