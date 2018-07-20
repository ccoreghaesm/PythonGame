#               In The Name Of Allah
#                   1396/06/26
#this Program Writed By : Ghasem Ramezani Manesh .@MG_Ramezani
#From Iran,Esfahan,Math House
#My Teacher's In Python :
#                  ~Mr.Bagheri
#                  ~Ms.Radmanesh

#------------------↓Import-Section↓--------------------------
import turtle
import os.path
import random as ran
from tkinter import messagebox
#--------------↑END-Import-Section↑--------------------------
#Win Initialize: ↓
_Win=turtle.Screen()
#Setup Screen: ↓
_Win.setup(900,500)

#Build a Variable For Store The Score:
User_Current_Score=0
##User_List_Score=[]

#Build a Stack:
class Stack:
    def __init__(self):
        self.StackItems = []
    def Push(self,item): #Add_To_Stack
        self.StackItems.append(item)
    def Pop(self): #Take_From_Stack
        return self.StackItems.pop()
    def IsEmpty(self): #Stack_Is_Empty
        return (self.StackItems == [])
stack = Stack()

#Build a File For Store The Score:
if(os.path.isfile('Score.txt')):#Check If File Exist:(True) Append  (False) Creat
    File_w = open('Score.txt','a')
else:
    File_w = open('Score.txt','w')

#Build a Turtle Agent: ↓
T_Agent = turtle.Turtle()
T_Agent.up() #Also You Can Use penup(),pu()
T_Agent.speed('fastest') #The arguments you can pass : 'fastest' or 0 ,'fast' or 10 ,'normal' or 6 ,'slow' or 3,'slowest' or 1
T_Agent.hideturtle() #Also You Can Use ht()

#Build a Turtle ScoreWriter: ↓
T_ScoreWriter = turtle.Turtle()
T_ScoreWriter.up()
T_ScoreWriter.color('darkgreen')
T_ScoreWriter.hideturtle()
T_ScoreWriter.speed(0)
T_ScoreWriter.goto(-230,220)

#Build a Turtle Ball: ↓
T_Ball = turtle.Turtle()
T_Ball.shape('circle')
T_Ball.speed(0)
T_Ball.color('red')
T_Ball.penup() #Also You Can Use up(),pu()
T_Ball.goto(-200,0) #Also You Can Use setposition()

#Build a Turtle Square: ↓
T_Square = turtle.Turtle()
T_Square.shape('turtle')
T_Square.up()
T_Square.speed('fastest')
T_Square.color('green')

#Draw The Game Area: ↓
T_Agent.width(3) #Also You Can Use pensize()
T_Agent.color('blue') 
T_Agent.setposition(-420,220) #Also You Can Use goto()
T_Agent.down() #Also You Can Use pendown(),pd()
T_Agent.forward(450) #Also You Can Use fd()
T_Agent.right(90) #Also You Can Use rt()
T_Agent.forward(450)
T_Agent.right(90)
T_Agent.forward(450)
T_Agent.right(90)
T_Agent.forward(450)
T_Agent.right(90)
#Draw The Game Menu: ↓
T_Agent.up()
T_Agent.width(1)
T_Agent.color('black')
T_Agent.goto(60,-40)
T_Agent.write('1-Reset Game\n2-All Scores Saved\n3-Reset Score\n4-All Score Now\n5-Exit\n\nIf Exit The Game Without \npress \'4\' Your Score\ndont be Save',move=False,align='left',font=('Courier New',20,'bold'))
#Learn More About write():
#     →turtle.write(arg,move=False,align='left',font=('Arial',8,'normal'))
#     →Parameters:
#           ●arg : Object to be Written to the TurtleScreen
#           ●move : True/False
#           ●align : One of the String 'left','center' or 'right'
#           ●font : a Triple (fontname,fontsize,fonttype)

#Game Function: ↓
class Function():
    Game_Pause = False
    def Key_Press_numeric1(self):
        T_Ball.goto(-200,0) #Reset Ball Position
        User_Current_Score=0 #Reset Score
        T_Square.goto(ran.randint(-410,-10),ran.randint(-220,210)) #Change Square Posision
        T_Square.setheading(ran.randint(0,180)) #Also You Can Use seth()
        T_ScoreWriter.clear() #Clear Old Written
        T_ScoreWriter.write('Score->:'+str(User_Current_Score),font=('Courier New',10,'bold')) #Write New Score
    def Key_Press_numeric2(self):
        FILE = open('Score.txt','r') #Open File For Read
        read = FILE.readline() #Read All line in File
        _String='' #Auxillary Variable For Parsing the File
        for i in read:
            if(i != '|'):
                _String+=i
            if(i == '|'):
                _String+='\n'
        messagebox.showinfo('All Score',_String) #Use Tkinter To Show A Message Box
    def Key_Press_numeric3(self):
        User_Current_Score=0 #Reset Score
        T_ScoreWriter.clear() #Clear Old Written
        T_ScoreWriter.write('Score->:'+str(User_Current_Score),font=('Courier New',10,'bold')) #Write New Score
        open('Score.txt','w').close() #Remade File
    def Key_Press_numeric4(self):
        stack_List='' #Auxillari Varibale To keep the values taken from the stack 
        while (stack.IsEmpty()==False):
            sst = stack.Pop()
            stack_List += str(sst) + '\n'
        messagebox.showinfo('All Score now',stack_List)
    def Key_Press_numeric5(self):
        File_w.write(str(User_Current_Score)+'|')
        File_w.close()
        exit()
    def Key_Press_LEFT(self):
        T_Ball.left(20)
    def Key_Press_RIGHT(self):
        T_Ball.right(20)
#Game Action: ↓
_F_=Function()
_Win.listen() #←Set Focus on TurtleScreen(in order to collect key-events).
_Win.onkeypress(_F_.Key_Press_numeric1,'1')
#Learn More About onkeypress():
#     →turtle.write(fun,key=None)
#     →Parameters:
#           ●fun : a Function With No Arguments or None
#           ●key : a String: Key(e.g.'a') or key-symbol(e.g.'space')
_Win.onkeypress(_F_.Key_Press_numeric2,'2')
##_Win.onkey(_F_.Key_Escape,'p')
_Win.onkey(_F_.Key_Press_numeric3,'3')
_Win.onkey(_F_.Key_Press_numeric5,'5')
_Win.onkey(_F_.Key_Press_numeric4,'4')
_Win.onkeypress(_F_.Key_Press_LEFT,'Left')
_Win.onkeypress(_F_.Key_Press_RIGHT,'Right')
#Start Game: ↓
while True:
##    if(_F_.Game_Pause == False):
    T_Ball.forward(1)
    if (T_Ball.xcor()<-410):
        x=T_Ball.xcor()
        y=T_Ball.ycor()
        T_Ball.goto((x+405),y)
##        T_Ball.left(180)
    if (T_Ball.xcor()>10):
        x=T_Ball.xcor()
        y=T_Ball.ycor()
        T_Ball.goto((x-405),y)
##        T_Ball.right(180)
    if (T_Ball.ycor()>210):
        x=T_Ball.xcor()
        y=T_Ball.ycor()
        T_Ball.goto(x,(y-405))
##        T_Ball.left(180)
    if (T_Ball.ycor()<-210):
        x=T_Ball.xcor()
        y=T_Ball.ycor()
        T_Ball.goto(x,(y+405))
##        T_Ball.left(180)
    if (T_Ball.distance(T_Square)<18):
        T_Square.goto(ran.randint(-410,-10),ran.randint(-220,210))
        T_Square.setheading(ran.randint(0,180))
        User_Current_Score+=10
        stack.Push(User_Current_Score)
        T_ScoreWriter.clear()
        T_ScoreWriter.write('Score->:'+str(User_Current_Score),font=('Courier New',10,'bold'))
        T_Ball.circle(20)
