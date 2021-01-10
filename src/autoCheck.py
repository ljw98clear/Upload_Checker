import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

import toon
import dataHandler


class MyApp(QWidget):

    def __init__(self, data):
        super().__init__()
        self.initUI(data)

    def initUI(self, data):
        label1 = QLabel(data["result"], self)
        label1.setAlignment(Qt.AlignCenter)

        table = QTableWidget(self)
        columnCnt = sum(data["toonCnt"])
        table.resize(150,columnCnt*30)
        table.setColumnCount(3)
        table.setRowCount(columnCnt)

        cnt = 0
        for site, names in data["detail"].items():
            for name, state in names.items():
                table.setItem(cnt, 0, QTableWidgetItem(site))
                table.setItem(cnt, 1, QTableWidgetItem(name))
                table.setItem(cnt, 2, QTableWidgetItem(state))
                cnt += 1

        font1 = label1.font()
        font1.setPointSize(20)

        label1.setFont(font1)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(table)

        self.setLayout(layout)

        self.setWindowTitle('만화 업로드 확인')
        self.setGeometry(300, 300, 350, columnCnt*30+80)
        self.show()


if __name__ == '__main__':
    data = dataHandler.getData()
    result = {"result": "업로드 없음", "detail": {}}
    #result = {"result": "없로드 없음", "detail": {"마나토끼":{"원피스":"업로드확인", "진격의 거인": "업로드 안됨", "진격의 거인2": "업로드 안됨", "진격의 거인3": "찾을 수 없음"}}}
    toonInst = []
    toonCnt = 0

    detail = result["detail"]
    for site, names in data.items():
        detail[site] = {}
        for name in names:
            isUpload = toon.toon(site,name).checkUpload()
            toonCnt += 1
            if isUpload == 0:
                detail[site][name] = "최신 업로드 확인"
                result["result"] = "업로드 존재"
            elif isUpload == 1:
                detail[site][name] = "-"
            else:
                detail[site][name] = "X"
    result["toonCnt"] = [1, 2, 1]
    app = QApplication(sys.argv)
    ex = MyApp(result)
    sys.exit(app.exec_())