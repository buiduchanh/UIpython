import io
from PIL import Image
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QBuffer

img = QImage("/home/buiduchanh/WorkSpace/demo_jestson/test/T0_018/TO_016_0205932.jpg")

buffer = QBuffer()
buffer.open(QBuffer.ReadWrite)
img.save(buffer, "PNG")
pil_im = Image.open(io.BytesIO(buffer.data()))
print(buffer)
pil_im.show()