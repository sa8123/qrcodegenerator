# This python code generates the qrcode which contains the information present in the data variable. 
from PIL import Image, ImageDraw
import qrcode


data = "Random data"
img = qrcode.make(data)
img.save("random.png")