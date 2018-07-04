#               In The Name Of Allah
#                   1396/06/27
#this Program Writed By : Ghasem Ramezani Manesh .@ASFisher
#From Iran,Esfahan,Math House
#My Teacher's In Python :
#                  ~Ms.Radmanesh
#                  ~Mr.Bagheri

#------------------↓Import-Section↓--------------------------
import turtle
from tkinter import messagebox
#--------------↑END-Import-Section↑--------------------------
#Win Initialize: ↓
_Win=turtle.Screen()
#Setup Screen: ↓
_Win.setup(500,800)
#Change Title: ↓
_Win.title('Simulation of Mobile Calculator')

#Build a Turtle Numeric1: ↓
T_Numeric_1=turtle.Turtle()
T_Numeric_1.color('gray')
T_Numeric_1.up()
T_Numeric_1.shape('square')
T_Numeric_1.speed(0)
T_Numeric_1.shapesize(2,5,20) #Also You Can Use turtlesize()

#Build a Turtle Numeric2: ↓
T_Numeric_2=turtle.Turtle()
T_Numeric_2.color('gray')
T_Numeric_2.up()
T_Numeric_2.shape('square')
T_Numeric_2.speed(0)
T_Numeric_2.shapesize(2,5,20) 

#Build a Turtle Numeric3: ↓
T_Numeric_3=turtle.Turtle()
T_Numeric_3.color('gray')
T_Numeric_3.up()
T_Numeric_3.shape('square')
T_Numeric_3.speed(0)
T_Numeric_3.shapesize(2,5,20)

#Build a Turtle Numeric4: ↓
T_Numeric_4=turtle.Turtle()
T_Numeric_4.color('gray')
T_Numeric_4.up()
T_Numeric_4.shape('square')
T_Numeric_4.speed(0)
T_Numeric_4.shapesize(2,5,20)

#Build a Turtle Numeric5: ↓
T_Numeric_5=turtle.Turtle()
T_Numeric_5.color('gray')
T_Numeric_5.up()
T_Numeric_5.shape('square')
T_Numeric_5.speed(0)
T_Numeric_5.shapesize(2,5,20)

#Build a Turtle Numeric6: ↓
T_Numeric_6=turtle.Turtle()
T_Numeric_6.color('gray')
T_Numeric_6.up()
T_Numeric_6.shape('square')
T_Numeric_6.speed(0)
T_Numeric_6.shapesize(2,5,20)

#Build a Turtle Numeric7: ↓
T_Numeric_7=turtle.Turtle()
T_Numeric_7.color('gray')
T_Numeric_7.up()
T_Numeric_7.shape('square')
T_Numeric_7.speed(0)
T_Numeric_7.shapesize(2,5,20)

#Build a Turtle Numeric8: ↓
T_Numeric_8=turtle.Turtle()
T_Numeric_8.color('gray')
T_Numeric_8.up()
T_Numeric_8.shape('square')
T_Numeric_8.speed(0)
T_Numeric_8.shapesize(2,5,20)

#Build a Turtle Numeric9: ↓
T_Numeric_9=turtle.Turtle()
T_Numeric_9.color('gray')
T_Numeric_9.up()
T_Numeric_9.shape('square')
T_Numeric_9.speed(0)
T_Numeric_9.shapesize(2,5,20)

#Build a Turtle Numeric0: ↓
T_Numeric_0=turtle.Turtle()
T_Numeric_0.color('gray')
T_Numeric_0.up()
T_Numeric_0.shape('square')
T_Numeric_0.speed(0)
T_Numeric_0.shapesize(2,5,20)

#Build a Turtle Operator_PLUS: ↓
T_Operator_PLUS=turtle.Turtle()
T_Operator_PLUS.color('darkgreen')
T_Operator_PLUS.up()
T_Operator_PLUS.shape('square')
T_Operator_PLUS.speed(0)
T_Operator_PLUS.shapesize(2,5,20)

#Build a Turtle Operator_MINUS: ↓
T_Operator_MINUS=turtle.Turtle()
T_Operator_MINUS.color('darkgreen')
T_Operator_MINUS.up()
T_Operator_MINUS.shape('square')
T_Operator_MINUS.speed(0)
T_Operator_MINUS.shapesize(2,5,20)

#Build a Turtle Operator_MUL: ↓
T_Operator_MUL=turtle.Turtle()
T_Operator_MUL.color('darkgreen')
T_Operator_MUL.up()
T_Operator_MUL.shape('square')
T_Operator_MUL.speed(0)
T_Operator_MUL.shapesize(2,5,20)

#Build a Turtle Operator_DIV: ↓
T_Operator_DIV=turtle.Turtle()
T_Operator_DIV.color('darkgreen')
T_Operator_DIV.up()
T_Operator_DIV.shape('square')
T_Operator_DIV.speed(0)
T_Operator_DIV.shapesize(2,5,20)

#Build a Turtle Okay: ↓
T_Okay=turtle.Turtle()
T_Okay.color('darkred')
T_Okay.up()
T_Okay.shape('square')
T_Okay.speed(0)
T_Okay.shapesize(2,5,20)

#Build a Turtle Agent: ↓
T_Agent = turtle.Turtle()
T_Agent.up() #Also You Can Use penup(),pu()
T_Agent.speed('fastest') #The arguments you can pass : 'fastest' or 0 ,'fast' or 10 ,'normal' or 6 ,'slow' or 3,'slowest' or 1
T_Agent.color('black')
T_Agent.hideturtle() #Also You Can Use ht()

#Buile a Turtle Printer: ↓
T_Printer = turtle.Turtle()
T_Printer.up() #Also You Can Use penup(),pu()
T_Printer.speed('fastest') #The arguments you can pass : 'fastest' or 0 ,'fast' or 10 ,'normal' or 6 ,'slow' or 3,'slowest' or 1
T_Printer.color('black')
T_Printer.hideturtle() #Also You Can Use ht()

#Draw a Square Whit Function: ↓
def Square(TurtleName,Forward_Length,Second_Forward_Length=0,LEFT=False):
    if(Second_Forward_Length==0):
        Second_Forward_Length = Forward_Length
    TurtleName.forward(Forward_Length) #Also You Can Use fd()
    if(LEFT == False):
        TurtleName.right(90) #Also You Can Use rt()
    else:
        TurtleName.left(90) #Also You Can Use lt()
    TurtleName.forward(Second_Forward_Length)
    if(LEFT == False):
        TurtleName.right(90)
    else:
        TurtleName.left(90)
    TurtleName.forward(Forward_Length)
    if(LEFT == False):
        TurtleName.right(90)
    else:
        TurtleName.left(90)
    TurtleName.forward(Second_Forward_Length)
    if(LEFT == False):
        TurtleName.right(90)
    else:
        TurtleName.left(90)
        
#Draw The Mobile Calculator Area: ↓
##T_Agent.color('white')
T_Agent.goto(-240,390) #Also You Can Use setposition()
T_Agent.down() #Also You Can Use pendown(),pd()
T_Agent.width(3) #Also You Can Use pensize()
Square(T_Agent,470,770)
T_Agent.goto(-240,350)
T_Agent.forward(470)
T_Agent.up()
T_Agent.goto(-60,355)
T_Agent.write('SUMSUNG',move=False,align='left',font=('Courier New',20,'normal'))
#Learn More About write():
#     →turtle.write(arg,move=False,align='left',font=('Arial',8,'normal'))
#     →Parameters:
#           ●arg : Object to be Written to the TurtleScreen
#           ●move : True/False
#           ●align : One of the String 'left','center' or 'right'
#           ●font : a Triple (fontname,fontsize,fonttype)
T_Agent.up()
T_Agent.goto(200,360)
T_Agent.down()
T_Agent.begin_fill()
T_Agent.circle(8)
T_Agent.end_fill()
T_Agent.up()
T_Agent.goto(-240,-320)
T_Agent.down()
T_Agent.forward(470)
T_Agent.up()
T_Agent.goto(-40,-340)
T_Agent.down()
T_Agent.begin_fill()
Square(T_Agent,80,20)
T_Agent.end_fill()
#Sort to the Left: ↓
T_Numeric_1.goto(-160,0)
T_Numeric_4.goto(-160,-70)
T_Numeric_7.goto(-160,-140)
T_Operator_PLUS.goto(-160,-210)
T_Operator_MINUS.goto(-160,-280)
#Sort to the Center: ↓
T_Numeric_5.goto(0,-70)
T_Numeric_8.goto(0,-140)
T_Numeric_0.goto(0,-210)
T_Okay.goto(0,-280)
#Sort to the Right: ↓
T_Numeric_3.goto(160,0)
T_Numeric_6.goto(160,-70)
T_Numeric_9.goto(160,-140)
T_Operator_MUL.goto(160,-210)
T_Operator_DIV.goto(160,-280)

#Action Function: ↓
class Function:
    _String_Numbers=''
    _Print= ''
    def Tell_Me_To_Print(self,What):
        self._Print+=What
        T_Printer.clear()
        T_Printer.goto(-100,200)
        T_Printer.write(self._Print,font=('Courier New',40,'normal'))
    def Clear(self,x,y):
        T_Printer.clear()
        self._Print=''
    def Click_Numeric_1(self,x,y):
        self._String_Numbers+='1'
        self.Tell_Me_To_Print('1')
    def Click_Numeric_2(self,x,y):
        self._String_Numbers+='2'
        self.Tell_Me_To_Print('2')
    def Click_Numeric_3(self,x,y):
        self._String_Numbers+='3'
        self.Tell_Me_To_Print('3')
    def Click_Numeric_4(self,x,y):
        self._String_Numbers+='4'
        self.Tell_Me_To_Print('4')
    def Click_Numeric_5(self,x,y):
        self._String_Numbers+='5'
        self.Tell_Me_To_Print('5')
    def Click_Numeric_6(self,x,y):
        self._String_Numbers+='6'
        self.Tell_Me_To_Print('6')
    def Click_Numeric_7(self,x,y):
        self._String_Numbers+='7'
        self.Tell_Me_To_Print('7')
    def Click_Numeric_8(self,x,y):
        self._String_Numbers+='8'
        self.Tell_Me_To_Print('8')
    def Click_Numeric_9(self,x,y):
        self._String_Numbers+='9'
        self.Tell_Me_To_Print('9')
    def Click_Numeric_0(self,x,y):
        self._String_Numbers+='0'
        self.Tell_Me_To_Print('0')
    def Click_Operator_Plus(self,x,y):
        self._String_Numbers+='+'
        self.Tell_Me_To_Print('+')
    def Click_Operator_Minus(self,x,y):
        self._String_Numbers+='-'
        self.Tell_Me_To_Print('-')
    def Click_Operator_Mul(self,x,y):
        self._String_Numbers+='*'
        self.Tell_Me_To_Print('*')
    def Click_Operator_Div(self,x,y):
        self._String_Numbers+='/'
        self.Tell_Me_To_Print('/')
    def Click_Okay(self,x,y):
        num_1='' ; num_2='' ; ope_0=''
        counter=0
        while True:
            if(self._String_Numbers[counter].isdigit()==True):
                num_1+=self._String_Numbers[counter]
            else:
                break
            counter+=1
        while True:
            if(self._String_Numbers[counter].isdigit()==False):
                ope_0+=self._String_Numbers[counter]
            else:
                break
            counter+=1
        while True:
            try:
                if(self._String_Numbers[counter].isdigit()==True):
                    num_2+=self._String_Numbers[counter]
                else:
                    break
            except:
                break
            counter+=1
        self._Print=''
        if(ope_0=='+'):
            self.Tell_Me_To_Print(str(int(num_1)+int(num_2)))
        elif(ope_0=='-'):
            self.Tell_Me_To_Print(str((int(num_1))-(int(num_2))))
        elif(ope_0=='*'):
            self.Tell_Me_To_Print(str(int(num_1)*int(num_2)))
        elif(ope_0=='/'):
            if(int(num_1)!=0 and int(num_2)!=0):
                self.Tell_Me_To_Print(str(int(num_1)/int(num_2)))
            else:
                self.Tell_Me_To_Print('Wrong Input')
        else:
            self.Tell_Me_To_Print('Wrong Input')
        self._String_Numbers=''
fun=Function()
#Mobile Calculator Action: ↓
T_Numeric_1.onclick(fun.Click_Numeric_1)
T_Numeric_2.onclick(fun.Click_Numeric_2)
T_Numeric_3.onclick(fun.Click_Numeric_3)
T_Numeric_4.onclick(fun.Click_Numeric_4)
T_Numeric_5.onclick(fun.Click_Numeric_5)
T_Numeric_6.onclick(fun.Click_Numeric_6)
T_Numeric_7.onclick(fun.Click_Numeric_7)
T_Numeric_8.onclick(fun.Click_Numeric_8)
T_Numeric_9.onclick(fun.Click_Numeric_9)
T_Numeric_0.onclick(fun.Click_Numeric_0)

T_Operator_PLUS.onclick(fun.Click_Operator_Plus)
T_Operator_MINUS.onclick(fun.Click_Operator_Minus)
T_Operator_MUL.onclick(fun.Click_Operator_Mul)
T_Operator_DIV.onclick(fun.Click_Operator_Div)

T_Okay.onclick(fun.Click_Okay)

T_Agent.onclick(fun.Clear)
#Write The Turtle Number's: ↓
T_Agent.up()
#Write Left Side: ↓
T_Agent.goto(-170,-20)
T_Agent.write('1',font=('Courier New',25,'bold'))
T_Agent.goto(-170,-90)
T_Agent.write('4',font=('Courier New',25,'bold'))
T_Agent.goto(-170,-160)
T_Agent.write('7',font=('Courier New',25,'bold'))
T_Agent.goto(-170,-230)
T_Agent.write('+',font=('Courier New',25,'bold'))
T_Agent.goto(-170,-300)
T_Agent.write('-',font=('Courier New',25,'bold'))
#Write Center Side: ↓
T_Agent.goto(0,-20)
T_Agent.write('2',font=('Courier New',25,'bold'))
T_Agent.goto(0,-90)
T_Agent.write('5',font=('Courier New',25,'bold'))
T_Agent.goto(0,-160)
T_Agent.write('8',font=('Courier New',25,'bold'))
T_Agent.goto(0,-230)
T_Agent.write('0',font=('Courier New',25,'bold'))
T_Agent.goto(0,-300)
T_Agent.write('OK',font=('Courier New',25,'bold'))
#Write Right Side: ↓
T_Agent.goto(150,-20)
T_Agent.write('3',font=('Courier New',25,'bold'))
T_Agent.goto(150,-90)
T_Agent.write('6',font=('Courier New',25,'bold'))
T_Agent.goto(150,-160)
T_Agent.write('9',font=('Courier New',25,'bold'))
T_Agent.goto(150,-230)
T_Agent.write('*',font=('Courier New',25,'bold'))
T_Agent.goto(150,-300)
T_Agent.write('/',font=('Courier New',25,'bold'))

T_Agent.goto(0,-350)
T_Agent.shape('square')
T_Agent.color('cyan')
T_Agent.showturtle()
T_Agent.shapesize(2,6,1)
turtle.up()
turtle.speed(0)
turtle.hideturtle()
turtle.goto(-45,-370)
turtle.write('Clear',font=('Courier New',16,'bold'))
Need_To_Tell='''
بسم الله الرحمن الرحيم
براي استفاده از ماشين حساب
کافي است با استفاده از ماوس
عدد ها را انتخاب کرده
پس از وارد کردن معادله
قالب وارد کردن معادله :
12+2
در يک معادله بيش از يک
عملگر نمي تواند قرار بگيرد
دکمه ok را بزنيد
براي تميز کردن صفحه از
دکمه Clear استفاده کنيد
'''
messagebox.showinfo('Need To Tell',Need_To_Tell) #Use Tkinter To Show A Message Box
