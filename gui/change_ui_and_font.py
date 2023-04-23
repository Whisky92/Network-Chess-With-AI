from PyQt5.QtGui import QFont


def on_back_btn_pressed(widget):
    """
    The actions to be done in case the back button was pressed

    :param widget: the widget that stores the ui screens
    """

    current = widget.currentWidget()
    widget.setCurrentIndex(widget.currentIndex() - 1)
    widget.removeWidget(current)


def change_ui(screen, widget):
    """
    The actions to happen in case of ui screen change

    :param screen: the screen to change to
    :param widget: the widget that stores the ui screens
    """

    widget.addWidget(screen)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def resize(qwidget, buttons):
    """
    Determines text resizing in case the window size changes

    :param qwidget: the widget whose button texts are about to be resized
    :param buttons: the list of buttons to be resized
    """

    default_size = 9

    if qwidget.rect().width() // 40 > default_size:
        f = QFont('', qwidget.rect().width() // 40)
    else:
        f = QFont('', default_size)

    for btn in buttons:
        btn.setFont(f)