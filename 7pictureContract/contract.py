import os
from PIL import Image
import piexif

def compress_image(input_path, output_path, quality=60):
    # 打开图片
    img = Image.open(input_path)
    # 获取EXIF元数据
    exif_data = img.info.get('exif')
    # 压缩并保存图片，保留EXIF
    img.save(output_path, 'JPEG', quality=quality, optimize=True, exif=exif_data)

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(folder, filename)
            output_path = os.path.join(folder, filename.rsplit('.', 1)[0] + '_compressed.jpg')
            compress_image(input_path, output_path)
            print(f'Compressed: {filename} -> {output_path}')

if __name__ == '__main__':
    main()