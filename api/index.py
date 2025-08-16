from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        Sin = request.values.get("Sin")
        Cos = request.values.get("Cos")
        Tan = request.values.get("Tan")
        Cot = request.values.get("Cot")
        Sec = request.values.get("Sec")
        Cosec = request.values.get("Cosec")
        Sin_Inverse = request.values.get("Sin_Inverse")
        Cos_Inverse = request.values.get("Cos_Inverse")
        Tan_Inverse = request.values.get("Tan_Inverse")
        Cot_Inverse = request.values.get("Cot_Inverse")
        Sec_Inverse = request.values.get("Sec_Inverse")
        Cosec_Inverse = request.values.get("Cosec_Inverse")
        if Sin == "":
            Sin = None
        if Cos == "":
            Cos = None
        if Tan == "":
            Tan = None
        if Cot == "":
            Cot = None
        if Sec == "":
            Sec = None
        if Cosec == "":
            Cosec = None
        if Sin_Inverse == "":
            Sin_Inverse = None
        elif Sin_Inverse != None:
            Sin_Inverse = Sin_Inverse.replace(" ", "_")
        if Cos_Inverse == "":
            Cos_Inverse = None
        elif Cos_Inverse != None:
            Cos_Inverse = Cos_Inverse.replace(" ", "_")
        if Tan_Inverse == "":
            Tan_Inverse = None
        elif Tan_Inverse != None:
            Tan_Inverse = Tan_Inverse.replace(" ", "_")
        if Cot_Inverse == "":
            Cot_Inverse = None
        elif Cot_Inverse != None:
            Cot_Inverse = Cot_Inverse.replace(" ", "_")
        if Sec_Inverse == "":
            Sec_Inverse = None
        elif Sec_Inverse != None:
            Sec_Inverse = Sec_Inverse.replace(" ", "_")
        if Cosec_Inverse == "":
            Cosec_Inverse = None
        elif Cosec_Inverse != None:
            Cosec_Inverse = Cosec_Inverse.replace(" ", "_")
        updated_code = generate_turtle_code(
            Sin,
            Cos,
            Tan,
            Cot,
            Sec,
            Cosec,
            Sin_Inverse,
            Cos_Inverse,
            Tan_Inverse,
            Cot_Inverse,
            Sec_Inverse,
            Cosec_Inverse,
        )
        return jsonify({"python_code": updated_code})
    return render_template("trigonometric_waves_animated_page.html")


def generate_turtle_code(
    Sin,
    Cos,
    Tan,
    Cot,
    Sec,
    Cosec,
    Sin_Inverse,
    Cos_Inverse,
    Tan_Inverse,
    Cot_Inverse,
    Sec_Inverse,
    Cosec_Inverse,
):
    code = f"""from turtle import *
from math import sin,cos,tan,radians,asin,acos,atan
turtles=['Sin','Cos','Tan','Cot','Sec','Cosec','NegSin','NegCos','NegTan','NegCot','NegSec','NegCosec','SinInv','CosInv','TanInv','CotInv','SecInv','CosecInv','NegSinInv','NegCosInv','NegTanInv','NegCotInv','NegSecInv','NegCosecInv']
def main():
        Screen().bgcolor('black')
        Screen().setworldcoordinates(-400,-3,400,3)
        colors=['#ff0000','#4d94ff','#ffa500','#5cd65c','#fff550','#800080','#ff0000','#4d94ff','#ffa500','#5cd65c','#fff550','#800080','#ff0000','#4d94ff','#ffa500','#5cd65c','#fff550','#800080','#ff0000','#4d94ff','#ffa500','#5cd65c','#fff550','#800080']
        for i in range(len(turtles)):
            turtles[i]=Turtle()
            turtles[i].ht()
            turtles[i].color(colors[i])
            turtles[i].speed('fastest')
        Write=Turtle()
        Write.color('white')
        Write.ht()
        Write.speed('fastest')
        Write.forward(360)
        Write.backward(720)
        Write.forward(360)
        Write.left(90)
        Write.forward(2)
        Write.backward(4) 
        up()
        for i in range(0,360):
                if {Sin_Inverse}:
                        try:
                            Sin_Inverse(i)
                        except:
                            pass
                if {Cos_Inverse}:
                        try:
                            Cos_Inverse(i)
                        except:
                            pass
                if {Tan_Inverse}:
                        try:
                            Tan_Inverse(i)
                        except:
                            pass
                if {Cot_Inverse}:
                        try:
                            Cot_Inverse(i)
                        except:
                                pass
                if {Sec_Inverse} and i>=58:
                        try:
                            Sec_Inverse(i)
                            turtles[16].pendown()
                            turtles[22].pendown()
                        except:
                                pass
                if {Cosec_Inverse} and i>=58:
                        try:
                            Cosec_Inverse(i)
                            turtles[17].pendown()
                            turtles[23].pendown()
                        except:
                            pass
                if {Sin}:
                        Sin(i)
                if {Cos}:
                        Cos(i)
                if {Tan}:
                        Tan(i)
                if {Cot}:
                        Cot(i)
                if {Sec}:
                        Sec(i)
                if {Cosec}:
                        Cosec(i)
def up():
    turtles[16].penup()
    turtles[22].penup()
    turtles[17].penup()
    turtles[23].penup()
def Sin_Inverse(x):
    turtles[12].goto(x,asin(radians(x)))
    turtles[18].goto(-x,asin(radians(-x)))
def Cos_Inverse(x):
    turtles[13].goto(x,acos(radians(x)))
    turtles[19].goto(-x,acos(radians(-x)))
def Tan_Inverse(x):
    turtles[14].goto(x,atan(radians(x)))
    turtles[20].goto(-x,atan(radians(-x)))
def Cot_Inverse(x):
    turtles[15].goto(x,atan(1/radians(x)))
    turtles[21].goto(-x,radians(180)+atan(1/radians(-x)))
def Sec_Inverse(x):
    turtles[16].goto(x,acos(1/radians(x)))
    turtles[22].goto(-x,acos(1/radians(-x)))
def Cosec_Inverse(x):
    turtles[17].goto(x,asin(1/radians(x)))
    turtles[23].goto(-x,asin(1/radians(-x))) 
def Sin(x):
    turtles[0].goto(x,sin(radians(x)))
    turtles[6].goto(-x,sin(radians(-x)))
def Cos(x):
    turtles[1].goto(x,cos(radians(x)))
    turtles[7].goto(-x,cos(radians(-x)))
def Tan(x):
    if x%90==0:
        turtles[2].goto(x,0)
        turtles[8].goto(-x,0)
    else:
        turtles[2].goto(x,tan(radians(x)))
        turtles[8].goto(-x,tan(radians(-x)))
def Cot(x):
    if x%90==0:
        turtles[3].goto(x,0)
        turtles[9].goto(-x,0)
    else:
        turtles[3].goto(x,1/(tan(radians(x))))
        turtles[9].goto(-x,1/(tan(radians(-x))))
def Sec(x):
    if x==90 or x==270:
        turtles[4].goto(x,0)
        turtles[10].goto(-x,0)
    else:
        turtles[4].goto(x,1/(cos(radians(x))))
        turtles[10].goto(-x,(1/cos(radians(-x))))
def Cosec(x):
    if x==180 or x==0:
        turtles[5].goto(x,0)
        turtles[11].goto(-x,0)
    else:
        turtles[5].goto(x,1/(sin(radians(x))))
        turtles[11].goto(-x,(1/sin(radians(-x))))
if __name__=='__main__':
    main()"""
    return code
