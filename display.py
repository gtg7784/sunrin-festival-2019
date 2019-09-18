import sys
import cv2
import datetime
import glob
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui
import PyQt5.QtCore as cr

class first(pq.QWidget):
    def __init__(self):
        super().__init__()
        self.setUi()
        self.setWindowTitle('당신의 스타일은?')
        self.resize(400,280)
    def setUi(self):
        btn_move=pq.QPushButton('사진 찍기',self)
        btn_move.clicked.connect(self.pic)
        btn_move.resize(100,50)
        btn_move.move(140,100)

    def pic(self):
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        while True:
            ret, frame = capture.read()
            if ret == True:
                cv2.imshow('frm', frame)
            else:
                print('카메라 연결 실패')
                break

            key = cv2.waitKey(1)

            if key == ord('q'):
                break
            elif key == ord('s'):
                name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
                path = glob.glob('./', 'data', 'test', name)
                cv2.imwrite(path, frame)
                print(path, 'saved')

        capture.release()
        cv2.destroyAllWindows()

if __name__=='__main__':
    app=pq.QApplication(sys.argv)
    ex=first()
    ex.show()
    app.exec_()