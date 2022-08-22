
_Calc = 100
import turtle
from turtle import Screen

cor_x_y = []

_screen = Screen()
_screen.title("NewYork-Criminal")
image = "x.gif"
_screen.addshape(image)
turtle.shape(image)
Male = []
Female = []
data = []
data2 = []
data3 = []
data4 = []
data5 = []
import pandas

_pandas = pandas.read_csv("NYPD_Complaint_Data_Current__Year_To_Date_.csv")
_pandas2 = _pandas.BORO_NM.to_list()
pandas3 = _pandas.SUSP_SEX.to_list()
for i in pandas3:
    if i == "M":
       Male.append(i)
    elif i == "F":
        Female.append(i)




for i in _pandas2:
    if i == "BROOKLYN":
        data.append(i)

for i in _pandas2:
    if i == "BRONX":
        data2.append(i)

for i in _pandas2:
    if i == "QUEENS":
        data3.append(i)

for i in _pandas2:
    if i == "MANHATTAN":
        data5.append(i)

print(len(_pandas2))

BROOKLYN = (len(data) * _Calc) / int(len(_pandas2))
BRONX = (len(data2) * _Calc) / int(len(_pandas2))
QUEENS = (len(data3) * _Calc) / int(len(_pandas2))
STATEN = 4.259395553686375
MANHATTAN = (len(data5) * _Calc) / int(len(_pandas2))

print((len(data) * _Calc) / int(len(_pandas2)) + (len(data2) * _Calc) / int(len(_pandas2)) + (len(data3) * _Calc) / int(
    len(_pandas2)) + (4.259395553686375) + (len(data5) * _Calc) / int(len(_pandas2)))

_percent = [MANHATTAN, BRONX, QUEENS, BROOKLYN, STATEN]
array_cor = []
cor_x = []
cor_y = []


def get_mouse_click_coor(x, y):
    cor = x, y
    cor_x_y.append(x)
    cor_x.append(x)
    cor_y.append(y)

    if len(cor_x_y) == 5:
        with open("txt", mode="w") as _txt:
            for i in cor_x_y:
                _write = _txt.writelines(str(i))
                array_cor.append(str(i))
                tim = turtle.Turtle()
                tim.hideturtle()
                tim.color("Black")
                tim.penup()

        print(cor_x)

        for i in range(5):
            print(i)
            print(_percent[i])
            print(f"x :{cor_x[i], cor_y[i]}: y")
            tim.goto(cor_x[i], cor_y[i])
            tim.write(f"%{_percent[i]}", font=("arial", 10, "normal"), align="center")


Female_Male = turtle.Turtle()
Female_Male.goto(-400,12)
Female_Male.hideturtle()
Female_Male.penup()

Female_Male.write(f"Suçlu Erkek Oranı :{len(Male)} Suçlu Kadın Oranı:{len(Female)}")

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
