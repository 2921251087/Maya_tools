
import sys
import _44a6428a69494567aed2941f480fe31f
_44a6428a69494567aed2941f480fe31f.main = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/30 17:44\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
import json
import datetime
from functools import partial
import _44a6428a69494567aed2941f480fe31f.config as config, _44a6428a69494567aed2941f480fe31f.config as _
reload(config)
from _44a6428a69494567aed2941f480fe31f.config import *
if DEBUG:
    import _44a6428a69494567aed2941f480fe31f.CPMel_Form as CPMel_Form, _44a6428a69494567aed2941f480fe31f.CPMel_Form as _
    reload(CPMel_Form)
    import _44a6428a69494567aed2941f480fe31f.plugins as plugins, _44a6428a69494567aed2941f480fe31f.plugins as _
    reload(plugins)
    import _44a6428a69494567aed2941f480fe31f.setup as setup, _44a6428a69494567aed2941f480fe31f.setup as _
    reload(setup)
    import _44a6428a69494567aed2941f480fe31f.update as update, _44a6428a69494567aed2941f480fe31f.update as _
    reload(update)
from _44a6428a69494567aed2941f480fe31f.CPMel.ui import *
from _44a6428a69494567aed2941f480fe31f.CPMel.tool import *
from _44a6428a69494567aed2941f480fe31f.plugins import plugins
import _44a6428a69494567aed2941f480fe31f.update as update, _44a6428a69494567aed2941f480fe31f.update as _

class HeadPixButton(QPushButton, ):

    def __init__(self, parent=None):
        super(HeadPixButton, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        pix = QPixmap(HEAD_IMG)
        head_label.setPixmap(pix)
        self._main_layout.addWidget(head_label)
        self.setFixedSize(pix.size())
        self.clicked.connect((lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com'))))

    def paintEvent(self, event):
        pass

class Head(QWidget, ):

    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.setFixedHeight(36)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = HeadPixButton()
        self._main_layout.addWidget(head_label)
        v_label = QLabel(((((START_TIME + u'-') + str(datetime.datetime.now().year)) + u' Version ') + u'{:.1f}'.format(Version)))
        self._main_layout.addWidget(v_label)
        self._main_layout.addStretch(0)

class _Body(QWidget, ):

    def __init__(self, parent=None):
        super(_Body, self).__init__(parent)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(2)
        pix = QPixmap((IMAGES + u'/button.png'))
        for i in plugins:
            try:
                i.init()
                name = i.name()
            except Exception as ex:
                print ex
            else:
                label = QLabel(self)
                label.setPixmap(pix)
                label.setFixedSize(QSize(20, 20))
                bn = QPushButton(name)
                bn.clicked.connect(undoBlock(i.doit))
                h_layout = QHBoxLayout()
                h_layout.addWidget(label)
                h_layout.addWidget(bn)
                self._main_layout.addLayout(h_layout)
        self._main_layout.addStretch(0)

class UpdateThread(QThread, ):
    sinOut = Signal(str)

    def __init__(self, parent=None):
        super(UpdateThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        info = update.updateinfo()
        self.sinOut.emit(info)

class Body(QWidget, ):

    def __init__(self, parent=None):
        super(Body, self).__init__(parent)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(0)
        self._body = _Body(self)
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(self._body)
        self._main_layout.addWidget(scrollArea)

class Footer(QWidget, ):

    def __init__(self, parent=None):
        super(Footer, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(0)
        self._news = QLabel()
        self._news.setText(u'loading...')
        self._main_layout.addWidget(self._news)
        self._update_thread = UpdateThread()
        self._update_thread.sinOut.connect(self._updateVersion)
        self._update_thread.start()
        self.update_bn = QPushButton(u'\u66f4\u65b0')
        self.update_bn.clicked.connect((lambda *args: update.update()))
        self._main_layout.addWidget(self.update_bn)
        self.update_bn.close()

    def _updateVersion(self, data):
        data = json.loads(data)
        if (int((Version * 10)) < int((data.get(u'version', (-1)) * 10))):
            self._news.setText((u'\u5b58\u5728\u65b0\u7684\u7248\u672c : ' + str(data.get(u'version', (-1)))))
            self.update_bn.show()
            return
        self._news.setText(u'\u5df2\u7ecf\u662f\u6700\u65b0\u7684\u7248\u672c\u4e86!')
        return

class MainWindow(CPQWidget, ):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(Title)
        icon = QIcon((IMAGES + u'/icon.png'))
        self.setWindowIcon(icon)
        with open((ASSETS + u'/qss.qss'), 'r') as f:
            self.setStyleSheet(f.read())
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(5)
        self._head = Head(self)
        self._body = Body(self)
        self._footer = Footer(self)
        self._main_layout.addWidget(self._head)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._body)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._footer)
        self.setMinimumHeight(400)

    def closeEvent(self, *args, **kwargs):
        deleteWidget(self)
win = None

def main():
    global win
    if (not (win is None)):
        win.close()
    win = MainWindow()
    win.show()
