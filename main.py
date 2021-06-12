# -*- coding: utf-8 -*-
# @Date    : 2021-06-12 17:41:21
# @Author  : Nora Yao(norayao0817@gmail.com)
# @Link    :
# @Version : Python3.7

import sys
from PyQt6




translator = Translator(service_urls=[
      'translate.google.cn',])# 如果可以上外网，还可添加 'translate.google.com' 等
trans = translator.translate('Hello World', src='en', dest='zh-cn')
# 原文
print(trans.origin)
# 译文
print(trans.text)

if __name__ == '__main__':
      app = QApplication(sys.argv)
      w = QWidget()
      w.resize(400, 200)
      # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
      w.move(300, 300)
      # 设置窗口的标题
      w.setWindowTitle('Simple')
      # 显示在屏幕上
      w.show()


      sys.exit(app.exec_())
class MyWindow(QMainWindow, Ui_MWin):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    clipboard = QApplication.clipboard()
    clipboard.dataChanged.connect(w.onClipboradChanged)
    sys.exit(app.exec_())