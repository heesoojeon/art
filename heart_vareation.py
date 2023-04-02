import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import time
class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500) # 위치와 크기 설정/ 파리미터 변경
        self.setWindowTitle('My_heart_Canvas') #  gui이름 정하기
        self.show() # 출력

    def getx(self,x):
        return int((x/200*500)+250)
    def gety(self,y):
        return int(((200-y)/200*500)-250)
        
             
    def paintEvent(self, event):
        painter = QPainter()
        
        # 팔레트 색상을 만들기
        red = QPen(QColor(255,167, 167), 10, Qt.SolidLine) # HSV Color Format ( 0~255 ) , size(10)
        b = QPen(QColor(250, 237, 125), 10, Qt.SolidLine)
        
        #색을 정하기
        
        #점을 찍기
        painter.begin(self)
        painter.setPen(red)
        painter.drawLine(self.getx(-90), self.gety(0),self.getx(90), self.gety(0))
        painter.drawLine(self.getx(0), self.gety(-90),self.getx(0), self.gety(90))
        #painter.end()
        
        painter.setPen(red)
        r=70
        for x in range(-70,71):
            y=int((r**2-x**2)**0.5)
            painter.drawPoint(self.getx(x), self.gety(y))
            painter.drawPoint(self.getx(x), self.gety(-y))
            time.sleep(1)
            
        painter.end()
"""  
        painter.drawPoint(100, 100) , painter.drawPoint(500, 300) , painter.drawPoint(500, 300) # 점 그리기
        painter.drawPoint(200, 100) , painter.drawPoint(300, 200) , painter.drawPoint(500, 300)
        painter.drawPoint(400, 500) , painter.drawPoint(500, 200) , painter.drawPoint(500, 300)
        painter.drawPoint(500, 300) , painter.drawPoint(500, 300) , painter.drawPoint(500, 300)
        
        painter.drawPoint(500, 500) , painter.drawPoint(500, 500) , painter.drawPoint(500, 500)
        painter.drawPoint(300, 300) , painter.drawPoint(300, 300) , painter.drawPoint(300, 300)
        painter.drawPoint(350, 350) , painter.drawPoint(350, 350) , painter.drawPoint(350, 350)
        painter.drawPoint(250, 400) , painter.drawPoint(250, 400) , painter.drawPoint(250, 400)
        painter.drawPoint(240, 390) , painter.drawPoint(240, 390) , painter.drawPoint(240, 390)
        painter.drawPoint(230, 380) , painter.drawPoint(230, 380) , painter.drawPoint(230, 380)
        painter.drawPoint(220, 370) , painter.drawPoint(220, 370) , painter.drawPoint(220, 370)
        painter.drawPoint(210, 360) , painter.drawPoint(210, 360) , painter.drawPoint(210, 360)
        painter.drawPoint(200, 350) , painter.drawPoint(200, 350) , painter.drawPoint(200, 350)
        painter.drawPoint(190, 340) , painter.drawPoint(190, 340) , painter.drawPoint(190, 340)
        painter.drawPoint(180, 330) , painter.drawPoint(180, 330) , painter.drawPoint(180, 330)
        painter.drawPoint(170, 320) , painter.drawPoint(170, 320) , painter.drawPoint(170, 320)
        painter.drawPoint(160, 310) , painter.drawPoint(160, 310) , painter.drawPoint(160, 310)
        painter.drawPoint(150, 300) , painter.drawPoint(150, 300) , painter.drawPoint(150, 300)
        painter.drawPoint(145, 295) , painter.drawPoint(145, 295) , painter.drawPoint(145, 295)
        painter.drawPoint(140, 290) , painter.drawPoint(140, 290) , painter.drawPoint(140, 290)
        painter.drawPoint(135, 285) , painter.drawPoint(135, 285) , painter.drawPoint(135, 285)
        painter.drawPoint(130, 280) , painter.drawPoint(130, 280) , painter.drawPoint(130, 280)
        painter.drawPoint(125, 270) , painter.drawPoint(125, 270) , painter.drawPoint(125, 270)
        painter.drawPoint(122, 260) , painter.drawPoint(122, 260) , painter.drawPoint(122, 260)
        painter.drawPoint(119, 250) , painter.drawPoint(119, 250) , painter.drawPoint(119, 250)
        painter.drawPoint(116, 240) , painter.drawPoint(116, 240) , painter.drawPoint(116, 240)
        painter.drawPoint(116, 230) , painter.drawPoint(116, 230) , painter.drawPoint(116, 230)
        painter.drawPoint(116, 220) , painter.drawPoint(116, 220) , painter.drawPoint(116, 220)
        painter.drawPoint(119, 210) , painter.drawPoint(119, 210) , painter.drawPoint(119, 210)
        painter.drawPoint(122, 200) , painter.drawPoint(122, 200) , painter.drawPoint(122, 200)
        painter.drawPoint(126, 190) , painter.drawPoint(126, 190) , painter.drawPoint(126, 190)
        painter.drawPoint(130, 185) , painter.drawPoint(130, 185) , painter.drawPoint(130, 185)
        painter.drawPoint(135, 180) , painter.drawPoint(135, 180) , painter.drawPoint(135, 180)
        painter.drawPoint(140, 175) , painter.drawPoint(140, 175) , painter.drawPoint(140, 175)
        painter.drawPoint(145, 170) , painter.drawPoint(145, 170) , painter.drawPoint(145, 170)
        painter.drawPoint(150, 167) , painter.drawPoint(150, 167) , painter.drawPoint(150, 167)
        painter.drawPoint(155, 165) , painter.drawPoint(155, 165) , painter.drawPoint(155, 165)
        painter.drawPoint(155, 166) , painter.drawPoint(155, 166) , painter.drawPoint(155, 166)
        painter.drawPoint(158, 164) , painter.drawPoint(158, 164) , painter.drawPoint(158, 164)
        painter.drawPoint(161, 162) , painter.drawPoint(161, 162) , painter.drawPoint(161, 162)
        painter.drawPoint(164, 160) , painter.drawPoint(164, 160) , painter.drawPoint(164, 160)
        painter.drawPoint(168, 160) , painter.drawPoint(168, 160) , painter.drawPoint(168, 160)
        painter.drawPoint(173, 161) , painter.drawPoint(173, 161) , painter.drawPoint(173, 161)
        painter.drawPoint(178, 161) , painter.drawPoint(178, 161) , painter.drawPoint(178, 161)
        painter.drawPoint(183, 161) , painter.drawPoint(183, 161) , painter.drawPoint(183, 161)
        painter.drawPoint(188, 162) , painter.drawPoint(188, 162) , painter.drawPoint(188, 162)
        painter.drawPoint(193, 163) , painter.drawPoint(193, 163) , painter.drawPoint(193, 163)
        painter.drawPoint(198, 163) , painter.drawPoint(198, 163) , painter.drawPoint(198, 163)
        painter.drawPoint(203, 164) , painter.drawPoint(203, 164) , painter.drawPoint(203, 164)
        painter.drawPoint(206, 166) , painter.drawPoint(206, 166) , painter.drawPoint(206, 166)
        painter.drawPoint(210, 168) , painter.drawPoint(210, 168) , painter.drawPoint(210, 168)
        painter.drawPoint(220, 170) , painter.drawPoint(220, 170) , painter.drawPoint(220, 170)
        painter.drawPoint(230, 175) , painter.drawPoint(230, 175) , painter.drawPoint(230, 175)
        painter.drawPoint(240, 183) , painter.drawPoint(240, 183) , painter.drawPoint(240, 183)
        painter.drawPoint(250, 189) , painter.drawPoint(250, 189) , painter.drawPoint(250, 189)
        painter.drawPoint(260, 183) , painter.drawPoint(260, 183) , painter.drawPoint(260, 183)
        painter.drawPoint(270, 175) , painter.drawPoint(270, 175) , painter.drawPoint(270, 175)
        painter.drawPoint(280, 170) , painter.drawPoint(280, 170) , painter.drawPoint(280, 170)
        painter.drawPoint(290, 168) , painter.drawPoint(290, 168) , painter.drawPoint(290, 168)
        painter.drawPoint(294, 166) , painter.drawPoint(294, 166) , painter.drawPoint(294, 166)
        painter.drawPoint(297, 164) , painter.drawPoint(297, 164) , painter.drawPoint(297, 164)
        painter.drawPoint(302, 163) , painter.drawPoint(302, 163) , painter.drawPoint(302, 163)
        painter.drawPoint(307, 162) , painter.drawPoint(307, 162) , painter.drawPoint(307, 162)
        painter.drawPoint(312, 161) , painter.drawPoint(312, 161) , painter.drawPoint(312, 161)
        painter.drawPoint(317, 161) , painter.drawPoint(317, 161) , painter.drawPoint(317, 161)
        painter.drawPoint(322, 161) , painter.drawPoint(322, 161) , painter.drawPoint(322, 161)
        painter.drawPoint(327, 160) , painter.drawPoint(327, 160) , painter.drawPoint(327, 160)
        painter.drawPoint(331, 160) , painter.drawPoint(331, 160) , painter.drawPoint(331, 160)
        painter.drawPoint(334, 162) , painter.drawPoint(334, 162) , painter.drawPoint(334, 162)
        painter.drawPoint(337, 164) , painter.drawPoint(337, 164) , painter.drawPoint(337, 164)
        painter.drawPoint(340, 165) , painter.drawPoint(340, 165) , painter.drawPoint(340, 165)
        painter.drawPoint(340, 165) , painter.drawPoint(340, 165) , painter.drawPoint(340, 165)
        painter.drawPoint(345, 167) , painter.drawPoint(345, 167) , painter.drawPoint(345, 167)
        painter.drawPoint(350, 170) , painter.drawPoint(350, 170) , painter.drawPoint(350, 170)
        painter.drawPoint(355, 175) , painter.drawPoint(355, 175) , painter.drawPoint(355, 175)
        painter.drawPoint(360, 180) , painter.drawPoint(360, 180) , painter.drawPoint(360, 180)
        painter.drawPoint(365, 185) , painter.drawPoint(365, 185) , painter.drawPoint(365, 185) 
        painter.drawPoint(369, 190) , painter.drawPoint(369, 190) , painter.drawPoint(369, 190)
        painter.drawPoint(373, 200) , painter.drawPoint(373, 200) , painter.drawPoint(373, 200)
        painter.drawPoint(376, 210) , painter.drawPoint(376, 210) , painter.drawPoint(376, 210)
        painter.drawPoint(379, 220) , painter.drawPoint(379, 220) , painter.drawPoint(379, 220)
        painter.drawPoint(379, 230) , painter.drawPoint(379, 230) , painter.drawPoint(379, 230)
        painter.drawPoint(379, 240) , painter.drawPoint(379, 240) , painter.drawPoint(379, 240)
        painter.drawPoint(376, 250) , painter.drawPoint(376, 250) , painter.drawPoint(376, 250)
        painter.drawPoint(373, 260) , painter.drawPoint(373, 260) , painter.drawPoint(373, 260)
        painter.drawPoint(370, 270) , painter.drawPoint(370, 270) , painter.drawPoint(370, 270)
        painter.drawPoint(365, 280) , painter.drawPoint(365, 280) , painter.drawPoint(365, 280)
        painter.drawPoint(360, 285) , painter.drawPoint(360, 285) , painter.drawPoint(360, 285)
        painter.drawPoint(355, 290) , painter.drawPoint(355, 290) , painter.drawPoint(355, 290)
        painter.drawPoint(350, 295) , painter.drawPoint(350, 295) , painter.drawPoint(350, 295)
        painter.drawPoint(345, 300) , painter.drawPoint(345, 300) , painter.drawPoint(345, 300)
        painter.drawPoint(340, 310) , painter.drawPoint(340, 310) , painter.drawPoint(340, 310)
        painter.drawPoint(330, 320) , painter.drawPoint(330, 320) , painter.drawPoint(330, 320)
        painter.drawPoint(320, 330) , painter.drawPoint(320, 330) , painter.drawPoint(320, 330)
        painter.drawPoint(310, 340) , painter.drawPoint(310, 340) , painter.drawPoint(310, 340)
        painter.drawPoint(300, 350) , painter.drawPoint(300, 350) , painter.drawPoint(300, 350)
        painter.drawPoint(290, 360) , painter.drawPoint(290, 360) , painter.drawPoint(290, 360)
        painter.drawPoint(280, 370) , painter.drawPoint(280, 370) , painter.drawPoint(280, 370)
        painter.drawPoint(270, 380) , painter.drawPoint(270, 380) , painter.drawPoint(270, 380)
        painter.drawPoint(260, 390) , painter.drawPoint(260, 390) , painter.drawPoint(260, 390)
        
        painter.setPen(b)
        painter.drawPoint(250, 199) , painter.drawPoint(250, 199) , painter.drawPoint(250, 199)
        
        painter.drawPoint(240, 191) , painter.drawPoint(240, 191) , painter.drawPoint(240, 191)
        painter.drawPoint(260, 191) , painter.drawPoint(260, 191) , painter.drawPoint(260, 191)
        
        painter.drawPoint(230, 185) , painter.drawPoint(230, 185) , painter.drawPoint(230, 185)
        painter.drawPoint(270, 185) , painter.drawPoint(270, 185) , painter.drawPoint(270, 185)
        
        painter.drawPoint(225, 185) , painter.drawPoint(225, 185) , painter.drawPoint(225, 185)
        painter.drawPoint(275, 185) , painter.drawPoint(275, 185) , painter.drawPoint(275, 185)
        
        painter.drawPoint(220, 180) , painter.drawPoint(220, 180) , painter.drawPoint(220, 180)
        painter.drawPoint(280, 180) , painter.drawPoint(280, 180) , painter.drawPoint(280, 180)
        
        painter.drawPoint(210, 175) , painter.drawPoint(210, 175) , painter.drawPoint(210, 175)
        painter.drawPoint(250, 175) , painter.drawPoint(250, 175) , painter.drawPoint(250, 175)
        
        painter.drawPoint(205, 173) , painter.drawPoint(205, 173) , painter.drawPoint(205, 173)
        painter.drawPoint(255, 173) , painter.drawPoint(255, 173) , painter.drawPoint(255, 173)
        
        painter.drawPoint(200, 170) , painter.drawPoint(200, 170) , painter.drawPoint(200, 170)
        painter.drawPoint(260, 170) , painter.drawPoint(260, 170) , painter.drawPoint(260, 170)
    """
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyCanvas()
    sys.exit(app.exec_())