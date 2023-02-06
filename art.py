print ('hello')
print("안녕하세요 청표범입니다")
pip install pillow
from PIL import Image

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize



