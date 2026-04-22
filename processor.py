from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
import os
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = "Modified/"

    def load_image(self, _dir, filename):

        self.filename = filename
        image_path = os.path.join(_dir, filename)
        self.image = Image.open(image_path)
    
    def show_image(self, path, photo_widget):
        pixmapimage = QPixmap(path)
        width, height = photo_widget.width(), photo_widget.height()
        scaled_image = pixmapimage.scaled(width, height, Qt.KeepAspectRatio)
        photo_widget.setPixmap(scaled_image)
        photo_widget.setVisible(True)

    def save_image(self, _dir):
        path = os.path.join(_dir, self.save_dir)
        if not((os.path.exists(path)) or os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)
    
    def do_flip(self, _dir, widget):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image(_dir)
        image_path = os.path.join(_dir, self.save_dir, self.filename)
        self.show_image(image_path, widget)

    def do_left(self, _dir, widget):
        self.image = self.image.rotate(-90)
        self.save_image(_dir)
        image_path = os.path.join(_dir, self.save_dir, self.filename)
        self.show_image(image_path, widget)

    def do_right(self, _dir, widget):
        self.image = self.image.rotate(90)
        self.save_image(_dir)
        image_path = os.path.join(_dir, self.save_dir, self.filename)
        self.show_image(image_path, widget)
        
    def do_gray(self, _dir, widget):
        self.image = ImageOps.grayscale(self.image)
        self.save_image(_dir)
        image_path = os.path.join(_dir, self.save_dir, self.filename)
        self.show_image(image_path, widget)        

    def do_Contrast(self, _dir, widget):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image(_dir)
        image_path = os.path.join(_dir, self.save_dir, self.filename)
        self.show_image(image_path, widget)      