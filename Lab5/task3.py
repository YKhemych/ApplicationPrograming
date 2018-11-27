import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image, ImageEnhance


def show_image():
    image = mpimg.imread('photo.jpg')
    plt.imshow(image)
    plt.show()


def channel():
    image = mpimg.imread('photo.jpg')
    i_red, i_blue, i_green = image.copy(), image.copy(), image.copy()
    i_red[:,:, 1], i_red[:, :, 2] = 0, 0
    plt.imshow(i_red)
    plt.show()
    i_blue[:, :, 0], i_blue[:, :, 1] = 0, 0
    plt.imshow(i_blue)
    plt.show()
    i_green[:, :, 0], i_green[:, :, 2] = 0, 0
    plt.imshow(i_green)
    plt.show()

def contrast():
    img =  Image.open('photo.jpg')
    img1 = img.copy()
    img = ImageEnhance.Contrast(img).enhance(0.1)
    plt.imshow(img)
    plt.show()
    img1 = ImageEnhance.Contrast(img1).enhance(50.0)
    plt.imshow(img1)
    plt.show()

def gray_image():
    rgb = mpimg.imread('photo.jpg')
    gray = np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    plt.show()




if __name__ == "__main__":
    show_image()
    contrast()
    channel()
    gray_image()
