# https://docs.python.org/3/library/turtle.html

import turtle 

turtle.shape("square")
turtle.shapesize(1,1)
turtle.color("red")

def stamp(x,y):
    turtle.goto(x,y)
    print(f"stamp({x-250},{250-y})")
    turtle.stamp()
    turtle.stamp()


turtle.penup()
print("#####################################")
stamp(250, 400) 
stamp(240, 390)  
stamp(230, 380) 
stamp(220, 370)  
stamp(210, 360) 
stamp(200, 350)  
stamp(190, 340) 
stamp(180, 330)  
stamp(170, 320)  
stamp(160, 310)  
stamp(150, 300)  
stamp(145, 295)  
stamp(140, 290)  
stamp(135, 285) 
stamp(130, 280) 
stamp(125, 270) 
stamp(122, 260) 
stamp(119, 250) 
stamp(116, 240) 
stamp(116, 230) 
stamp(116, 220) 
stamp(119, 210) 
stamp(122, 200) 
stamp(126, 190) 
stamp(130, 185) 
stamp(135, 180) 
stamp(140, 175) 
stamp(145, 170) 
stamp(150, 167) 
stamp(155, 165) 
stamp(155, 166) 
stamp(158, 164) 
stamp(161, 162) 
stamp(164, 160) 
stamp(168, 160) 
stamp(173, 161) 
stamp(178, 161) 
stamp(183, 161) 
stamp(188, 162) 
stamp(193, 163) 
stamp(198, 163) 
stamp(203, 164) 
stamp(206, 166) 
stamp(210, 168) 
stamp(220, 170) 
stamp(230, 175) 
stamp(240, 183) 
print("#####################################")
stamp(250, 189) 
stamp(260, 183) 
stamp(270, 175) 
stamp(280, 170) 
stamp(290, 168) 
stamp(294, 166) 
stamp(297, 164) 
stamp(302, 163) 
stamp(307, 162) 
stamp(312, 161) 
stamp(317, 161) 
stamp(322, 161) 
stamp(327, 160) 
stamp(331, 160) 
stamp(334, 162) 
stamp(337, 164) 
stamp(340, 165) 
stamp(340, 165) 
stamp(345, 167) 
stamp(350, 170) 
stamp(355, 175) 
stamp(360, 180) 
stamp(365, 185) 
stamp(369, 190) 
stamp(373, 200) 
stamp(376, 210) 
stamp(379, 220) 
stamp(379, 230) 
stamp(379, 240) 
stamp(376, 250) 
stamp(373, 260) 
stamp(370, 270) 
stamp(365, 280) 
stamp(360, 285) 
stamp(355, 290) 
stamp(350, 295) 
stamp(345, 300) 
stamp(340, 310) 
stamp(330, 320) 
stamp(320, 330) 
stamp(310, 340) 
stamp(300, 350) 
stamp(290, 360) 
stamp(280, 370) 
stamp(270, 380) 
stamp(260, 390) 
        
turtle.color("blue")
print("#####################################")
stamp(250, 199)
stamp(240, 191)
stamp(260, 191)

stamp(230, 185)
stamp(270, 185)

stamp(225, 185)
stamp(275, 185)

stamp(220, 180)
stamp(280, 180)

stamp(210, 175)
stamp(250, 175)

stamp(205, 173)
stamp(255, 173)

stamp(200, 170)
stamp(260, 170) 
print("#####################################")
turtle.mainloop()
