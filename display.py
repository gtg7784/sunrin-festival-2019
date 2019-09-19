import sys
import cv2
import datetime
import glob
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui
import PyQt5.QtCore as cr
import numpy as np
from tensorflow import keras
import os

class first(pq.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('당신의 스타일은?')
        self.resize(400,280)
        self.setUi()
    def setUi(self):

        self.label=pq.QLabel('당신의 스타일은?!?!',self)
        self.label.move(15,100)
        self.label.setAlignment(cr.Qt.AlignHCenter)
        self.label.resize(400,200)
        font=self.label.font()
        font.setPointSize(20)
        font.setBold(True)
        font.setFamily('NanumSquare')
        self.label.setFont(font)
        btn_move=pq.QPushButton('사진 찍기',self)
        btn_move.clicked.connect(self.pic)
        btn_font=btn_move.font()
        btn_font.setFamily('NanumSquare')
        btn_move.setFont(btn_font)

        btn_move.resize(100,50)
        btn_move.move(140,200)

    def pic(self):
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        while True:
            ret, frame = capture.read()
            if ret == True:
                cv2.imshow('farme', frame)
            else:
                print('카메라 연결 실패')
                break

            key = cv2.waitKey(1)

            if key == ord('q'):
                capture.release()
                cv2.destroyAllWindows()
                return

            elif key == ord('s'):

                break

        capture.release()
        cv2.destroyAllWindows()
        print(frame.shape)
        model=keras.models.load_model('model.h5')
        print('로딩성공')
        data = frame / 255.0
        img=cv2.resize(data,(48,48))
        img=img.reshape(1,48,48,3)
        pre=model.predict(img)
        pre=pre.reshape(-1)
        max=np.argmax(pre)

        if int(max) == 0:
            kind='amekaji'
            print(kind)
            self.label.setText('당신의 스타일은:'+kind)
            name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
            path = os.path.join('./', 'data/train/',kind, name)
            cv2.imwrite(path, frame)
            print(path, 'saved')
        elif int(max) == 1:
            kind='casual'
            print(kind)
            self.label.setText('당신의 스타일은:'+kind)
            name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
            path = os.path.join('./', 'data/train/', kind, name)
            cv2.imwrite(path, frame)
            print(path, 'saved')
        elif int(max) == 2:
            kind = 'dandy'
            print(kind)
            self.label.setText('당신의 스타일은:'+kind)
            name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
            path = os.path.join('./', 'data/train/', kind, name)
            cv2.imwrite(path, frame)
            print(path, 'saved')
        elif int(max) == 3:
            kind = 'street'
            print(kind)
            self.label.setText('당신의 스타일은:'+kind)
            name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
            path = os.path.join('./', 'data/train/', kind, name)
            cv2.imwrite(path, frame)
            print(path, 'saved')

if __name__=='__main__':
    app=pq.QApplication(sys.argv)
    ex=first()
    ex.show()
    app.exec_()
    print('정싱종료')