import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt



class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500) # 위치와 크기 설정/ 파리미터 변경
        self.setWindowTitle('My_heart_Canvas') #  gui이름 정하기
        self.show() # 출력

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 팔레트 색상을 만들기
        red = QPen(QColor(255, 167, 167), 10, Qt.SolidLine) # HSV Color Format ( 0~255 ) , size(10)
        b = QPen(QColor(250, 224, 140), 10, Qt.SolidLine)
        
        #색을 정하기
        painter.setPen(red)
        #점을 찍기
        # 점 그리기
        painter.setPen(red)
        
        
        
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
        painter.drawPoint(290, 175)
       
        
        painter.drawPoint(200, 170) 
        painter.drawPoint(300, 170)
        
        painter.drawPoint(190, 167)
        painter.drawPoint(310, 167)
        
        painter.drawPoint(180, 167)
        painter.drawPoint(320, 167)
        
        painter.drawPoint(170, 168)
        painter.drawPoint(330, 168)
        
        painter.drawPoint(160, 170)
        painter.drawPoint(340, 170)
        
        painter.drawPoint(150, 175)
        painter.drawPoint(350, 175)
        
        painter.drawPoint(145, 180)
        painter.drawPoint(355, 180)
        
        painter.drawPoint(140, 185)
        painter.drawPoint(360, 185)
        
        painter.drawPoint(135, 190)
        painter.drawPoint(365, 190)
        
        painter.drawPoint(130, 195)
        painter.drawPoint(367, 195)
        
        painter.drawPoint(127, 200)
        painter.drawPoint(369, 200)
        
        painter.drawPoint(126, 210)
        painter.drawPoint(371, 210)
        
        painter.drawPoint(122, 220)
        painter.drawPoint(374, 220)
        
        painter.drawPoint(121, 230)
        painter.drawPoint(374, 230)
        
        painter.drawPoint(123, 240)
        painter.drawPoint(374, 240)
        
        painter.drawPoint(124, 250)
        painter.drawPoint(372, 250)
        
        painter.drawPoint(130, 260)
        painter.drawPoint(369, 260)
        
        painter.drawPoint(135, 270)
        painter.drawPoint(365, 270)
        
        painter.drawPoint(141, 280)
        painter.drawPoint(360, 280)
        
        painter.drawPoint(150, 290)
        painter.drawPoint(355, 290)
       
        painter.drawPoint(160, 300)
        painter.drawPoint(345, 300)
        
        painter.drawPoint(170, 310)
        painter.drawPoint(340, 310)
        
        painter.drawPoint(180, 320)
        painter.drawPoint(332, 320)
        
        painter.drawPoint(190, 330)
        painter.drawPoint(322, 330)
        
        painter.drawPoint(200, 340)
        painter.drawPoint(312, 340)
        
        painter.drawPoint(210, 350)
        painter.drawPoint(302, 350)
        
        painter.drawPoint(220, 360)
        painter.drawPoint(292, 360)
        
        painter.drawPoint(230, 370)
        painter.drawPoint(282, 370)
        
        painter.drawPoint(240, 380)
        painter.drawPoint(272, 380)
        
        painter.drawPoint(250, 390)
        #################################################
        painter.setPen(red)
        painter.drawPoint(250, 209)
        
        painter.drawPoint(240, 200)
        painter.drawPoint(260, 200)
        
        painter.drawPoint(230, 195)
        painter.drawPoint(270, 195)
        
        painter.drawPoint(229, 194)
        painter.drawPoint(269, 194)
        
        painter.drawPoint(220, 190)
        painter.drawPoint(278, 190)
        
        painter.drawPoint(210, 185)
        painter.drawPoint(288, 185)
        
        painter.drawPoint(201, 179)
        painter.drawPoint(297, 179)
        
        painter.drawPoint(192, 175)
        painter.drawPoint(306, 175)
        
        painter.drawPoint(184, 174)
        painter.drawPoint(314, 174)
        
        painter.drawPoint(176, 175)
        painter.drawPoint(322, 175)
        
        painter.drawPoint(168, 176)
        painter.drawPoint(330, 176)
        
        painter.drawPoint(161, 178)
        painter.drawPoint(337, 178)
        
        painter.drawPoint(156, 181)
        painter.drawPoint(342, 181)
        
        painter.drawPoint(153, 184)
        painter.drawPoint(345, 184)
        
        painter.drawPoint(150, 187)
        painter.drawPoint(348, 187)
        
        painter.drawPoint(147, 190)
        painter.drawPoint(351, 190)
        
        painter.drawPoint(144, 193)
        painter.drawPoint(354, 193)
        
        painter.drawPoint(140, 196)
        painter.drawPoint(358, 196)
        
        painter.drawPoint(136, 200)
        painter.drawPoint(362, 200)
        
        painter.drawPoint(134, 210)
        painter.drawPoint(364, 210)
        
        painter.drawPoint(132, 220)
        painter.drawPoint(366, 220)
        
        painter.drawPoint(131, 230)
        painter.drawPoint(367, 230)
        
        painter.drawPoint(132, 240)
        painter.drawPoint(366, 240)
        
        painter.drawPoint(133, 250)
        painter.drawPoint(365, 250)
        
        painter.drawPoint(136, 260)
        painter.drawPoint(362, 260)
        
        painter.drawPoint(140, 270)
        painter.drawPoint(358, 270)
        
        painter.drawPoint(147, 280)
        painter.drawPoint(353, 280)
        
        painter.drawPoint(155, 290)
        painter.drawPoint(346, 290)
        
        painter.drawPoint(165, 300)
        painter.drawPoint(336, 300)
        painter.setPen(yellow)
        painter.drawPoint(255, 380)
        painter.setPen(pink)
        painter.drawPoint(265, 380)
       
        ####################################370
        painter.setPen(yellow)
        painter.drawPoint(245, 370)
        painter.setPen(pink)
        painter.drawPoint(254, 370)
        painter.setPen(yellow)
        painter.drawPoint(262, 370)
        painter.setPen(pink)
        painter.drawPoint(270, 370)
        painter.setPen(yellow)
        painter.drawPoint(277, 370)
        painter.setPen(pink)
        painter.drawPoint(284, 370)
        painter.setPen(yellow)
        painter.drawPoint(288, 370)
        ########################################360
        painter.setPen(pink)
        painter.drawPoint(280, 360)
        painter.setPen(yellow)
        painter.drawPoint(275, 360)
        painter.setPen(pink)
        painter.drawPoint(265, 360)
        painter.setPen(yellow)
        painter.drawPoint(255, 360)
        painter.setPen(pink)
        painter.drawPoint(245, 360)
        painter.setPen(yellow)
        painter.drawPoint(235, 360)
        ##########################################350
        painter.setPen(yellow)
        painter.drawPoint(225, 350)
        painter.setPen(pink)
        painter.drawPoint(235, 350)
        painter.setPen(yellow)
        painter.drawPoint(245, 350)
        painter.setPen(pink)
        painter.drawPoint(255, 350)
        painter.setPen(yellow)
        painter.drawPoint(265, 350)
        painter.setPen(pink)
        painter.drawPoint(275, 350)
        painter.setPen(yellow)
        painter.drawPoint(285, 350)
        painter.setPen(pink)
        painter.drawPoint(295, 350)
        ###################################340
        blue = QPen(QColor(178, 235, 244), 10, Qt.SolidLine)
        
        painter.setPen(yellow)
        painter.drawPoint(215, 340)
        painter.drawPoint(295, 340)
        
        painter.setPen(pink)
        painter.drawPoint(285, 340)
        painter.setPen(yellow)
        painter.drawPoint(275, 340)
        painter.setPen(pink)
        painter.drawPoint(265, 340)
        painter.setPen(yellow)
        painter.drawPoint(255, 340)
        painter.setPen(pink)
        painter.drawPoint(245, 340)
        painter.setPen(yellow)
        painter.drawPoint(235, 340)
        painter.setPen(pink)
        painter.drawPoint(225, 340)
        #####################################330
        painter.setPen(yellow)
        painter.drawPoint(205, 330)
        painter.drawPoint(305, 330)
        
        painter.setPen(pink)
        painter.drawPoint(215, 330)
        painter.drawPoint(295, 330)
        painter.drawPoint(255, 330)
        
        painter.setPen(yellow)
        painter.drawPoint(225, 330)
        painter.drawPoint(285, 330) 
        
        painter.setPen(pink)
        painter.drawPoint(235, 330)
        painter.drawPoint(275, 330)
        
        painter.setPen(yellow)
        painter.drawPoint(245, 330)
        painter.drawPoint(265, 330)
        #####################################320
        green = QPen(QColor(206, 242, 121), 10, Qt.SolidLine)
        painter.setPen(green)
        painter.drawPoint(205, 320)
        painter.drawPoint(305, 320)
        painter.drawPoint(215, 320)
        painter.drawPoint(295, 320)
        painter.drawPoint(255, 320)
        painter.drawPoint(225, 320)
        painter.drawPoint(285, 320) 
        painter.drawPoint(235, 320)
        painter.drawPoint(275, 320)
        painter.drawPoint(245, 320)
        painter.drawPoint(265, 320)
        ###########################################310
        painter.setPen(yellow)
        painter.drawPoint(205, 310)
        painter.drawPoint(305, 310)
        painter.drawPoint(215, 310)
        painter.drawPoint(295, 310)
        painter.drawPoint(255, 310)
        painter.drawPoint(225, 310)
        painter.drawPoint(285, 310) 
        painter.drawPoint(235, 310)
        painter.drawPoint(275, 310)
        painter.drawPoint(245, 310)
        painter.drawPoint(265, 310)
        ########################################300
        painter.setPen(blue)
        painter.drawPoint(205, 300)
        painter.drawPoint(305, 300)
        painter.drawPoint(215, 300)
        painter.drawPoint(295, 300)
        painter.drawPoint(255, 300)
        painter.drawPoint(225, 300)
        painter.drawPoint(285, 300) 
        painter.drawPoint(235, 300)
        painter.drawPoint(275, 300)
        painter.drawPoint(245, 300)
        painter.drawPoint(265, 300)
        ############################################290
        green = QPen(QColor(206, 242, 121), 10, Qt.SolidLine)
        painter.setPen(green)
        painter.drawPoint(205, 290)
        painter.drawPoint(305, 290)
        painter.drawPoint(215, 290)
        painter.drawPoint(295, 290)
        painter.drawPoint(255, 290)
        painter.drawPoint(225, 290)
        painter.drawPoint(285, 290) 
        painter.drawPoint(235, 290)
        painter.drawPoint(275, 290)
        painter.drawPoint(245, 290)
        painter.drawPoint(265, 290)
        ###############################################280
        painter.setPen(yellow)
        painter.drawPoint(205, 280)
        painter.drawPoint(305, 280)
        painter.drawPoint(215, 280)
        painter.drawPoint(295, 280)
        painter.drawPoint(255, 280)
        painter.drawPoint(225, 280)
        painter.drawPoint(285, 280) 
        painter.drawPoint(235, 280)
        painter.drawPoint(275, 280)
        painter.drawPoint(245, 280)
        painter.drawPoint(265, 280)
        ##############################################270
        painter.setPen(green)
        painter.drawPoint(205, 270)
        painter.drawPoint(305, 270)
        painter.drawPoint(215, 270)
        painter.drawPoint(295, 270)
        painter.drawPoint(255, 270)
        painter.drawPoint(225, 270)
        painter.drawPoint(285, 270) 
        painter.drawPoint(235, 270)
        painter.drawPoint(275, 270)
        painter.drawPoint(245, 270)
        painter.drawPoint(265, 270)
        #################################260
        painter.setPen(blue)
        painter.drawPoint(205, 260)
        painter.drawPoint(305, 260)
        painter.drawPoint(215, 260)
        painter.drawPoint(295, 260)
        painter.drawPoint(255, 260)
        painter.drawPoint(225, 260)
        painter.drawPoint(285, 260) 
        painter.drawPoint(235, 260)
        painter.drawPoint(275, 260)
        painter.drawPoint(245, 260)
        painter.drawPoint(265, 260)
        #################################250
        painter.setPen(green)
        painter.drawPoint(205, 250)
        painter.drawPoint(305, 250)
        painter.drawPoint(215, 250)
        painter.drawPoint(295, 250)
        painter.drawPoint(255, 250)
        painter.drawPoint(225, 250)
        painter.drawPoint(285, 250) 
        painter.drawPoint(235, 250)
        painter.drawPoint(275, 250)
        painter.drawPoint(245, 250)
        painter.drawPoint(265, 250)
        ####################################240
        painter.setPen(yellow)
        painter.drawPoint(205, 240)
        painter.drawPoint(305, 240)
        painter.drawPoint(215, 240)
        painter.drawPoint(295, 240)
        painter.drawPoint(255, 240)
        painter.drawPoint(225, 240)
        painter.drawPoint(285, 240) 
        painter.drawPoint(235, 240)
        painter.drawPoint(275, 240)
        painter.drawPoint(245, 240)
        painter.drawPoint(265, 240)
        ####################################230
        painter.setPen(green)
        painter.drawPoint(205, 230)
        painter.drawPoint(305, 230)
        painter.drawPoint(215, 230)
        painter.drawPoint(295, 230)
        painter.drawPoint(255, 230)
        painter.drawPoint(225, 230)
        painter.drawPoint(285, 230) 
        painter.drawPoint(235, 230)
        painter.drawPoint(275, 230)
        painter.drawPoint(245, 230)
        painter.drawPoint(265, 230)
        ###################################220
        painter.setPen(yellow)
        painter.drawPoint(205, 220)
        painter.drawPoint(305, 220)
        painter.drawPoint(215, 220)
        painter.drawPoint(295, 220)
        painter.drawPoint(255, 220)
        painter.drawPoint(225, 220)
        painter.drawPoint(285, 220) 
        painter.drawPoint(235, 220)
        painter.drawPoint(275, 220)
        painter.drawPoint(245, 220)
        painter.drawPoint(265, 220)               