import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VN BROWSER")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.setCentralWidget(self.browser)

        self.create_navigation_bar()
        self.create_navigation_actions()

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

    def create_navigation_bar(self):
        self.navigation_bar = self.addToolBar("Navigation")
        self.navigation_bar.setMovable(False)

        self.back_button = QAction("Back", self)
        self.back_button.triggered.connect(self.browser.back)
        self.navigation_bar.addAction(self.back_button)

        self.forward_button = QAction("Forward", self)
        self.forward_button.triggered.connect(self.browser.forward)
        self.navigation_bar.addAction(self.forward_button)

        self.reload_button = QAction("Reload", self)
        self.reload_button.triggered.connect(self.browser.reload)
        self.navigation_bar.addAction(self.reload_button)

        self.home_button = QAction( "Home", self)
        self.home_button.triggered.connect(self.navigate_home)
        self.navigation_bar.addAction(self.home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navigation_bar.addWidget(self.url_bar)

    def create_navigation_actions(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        new_tab_action = QAction("New Tab", self)
        file_menu.addAction(new_tab_action)

        new_window_action = QAction("New Window", self)
        file_menu.addAction(new_window_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")

        about_action = QAction("About", self)
        help_menu.addAction(about_action)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
