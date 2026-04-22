from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
    QTextEdit,
    QHBoxLayout,
    QVBoxLayout,
    QInputDialog,
    QFileDialog,
    )
from PyQt5.QtGui import QPixmap
from processor import ImageProcessor
import os

# переменые
WORKDIR = None
image_processor = ImageProcessor()

#Интилизация
app = QApplication([])
main_window = QWidget()

#виджеты
select_photo_widget = QPushButton("папка")
func_left_widget = QPushButton("лево")
func_right_widget = QPushButton("право")
func_mirror_widget = QPushButton("зеркало")
func_gray_widget = QPushButton("ч/б")
func_sharpness_widget = QPushButton("резкость")

list_photo_widget = QListWidget()

photo_widget = QLabel("Картинка")

#слои
func_layout = QHBoxLayout()
files_layout = QVBoxLayout()
edit_photp_layout = QVBoxLayout()
main_layout = QHBoxLayout()

#заполнение слоёв
func_layout.addWidget(func_left_widget)
func_layout.addWidget(func_right_widget)
func_layout.addWidget(func_mirror_widget)
func_layout.addWidget(func_gray_widget)
func_layout.addWidget(func_sharpness_widget)

edit_photp_layout.addWidget(photo_widget)
edit_photp_layout.addLayout(func_layout)

files_layout.addWidget(select_photo_widget)
files_layout.addWidget(list_photo_widget)

main_layout.addLayout(files_layout)
main_layout.addLayout(edit_photp_layout)

main_window.setLayout(main_layout)

#функции
def file_filter(files, extensions):
    result = []
    for file_name in files:
        extent = file_name.split(".")[1] if len(file_name.split(".")) > 1 else None
        if extent in extensions:
            result.append(file_name)
    return result

def show_file_name_list():
    global WORKDIR
    WORKDIR = QFileDialog.getExistingDirectory()
    extensions = ["png", "jpg", "jpeg", "webp"]
    file_name = os.listdir(WORKDIR)
    file_name = file_filter(file_name, extensions)
    list_photo_widget.clear()
    list_photo_widget.addItems( file_name)

def select_and_show_image():
    if list_photo_widget.currentRow() >= 0:
        file_name = list_photo_widget.currentItem().text()
        image_processor.load_image(WORKDIR, file_name)
        image_path = os.path.join(WORKDIR, file_name)
        image_processor.show_image(image_path, photo_widget)

def event_flip():
    image_processor.do_flip(WORKDIR, photo_widget)

def event_left():
    image_processor.do_left(WORKDIR, photo_widget)

def event_right():
    image_processor.do_right(WORKDIR, photo_widget)

def event_gray():
    image_processor.do_gray(WORKDIR, photo_widget)

def event_Contrast():
    image_processor.do_Contrast(WORKDIR, photo_widget)
#Настройки виджетов
select_photo_widget.clicked.connect(show_file_name_list)
list_photo_widget.currentRowChanged.connect(select_and_show_image)
func_mirror_widget.clicked.connect(event_flip)
func_left_widget.clicked.connect(event_left)
func_right_widget.clicked.connect(event_right)
func_gray_widget.clicked.connect(event_gray)
func_sharpness_widget.clicked.connect(event_Contrast)
#класс управления фото


    
#запуск
main_window.show()
app.exec()
#конец