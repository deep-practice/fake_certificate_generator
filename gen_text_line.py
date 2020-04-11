# coding=utf-8
from PIL import Image,ImageFont,ImageDraw

def create_an_image(bground_path, width, height):
    bground = Image.open(bground_path)
    bground = bground.resize((width, height),Image.ANTIALIAS)
    return bground

"""
A simple method for generating text image with given background
    :param dst_w: The result image width
    :param dst_h: The result image height
    :param bk_img_path: The background image path
    :param text:The text you want to write
    :param start_point:Where to begin
    :param font:Text font
    :param save_path:
"""
def gen_chinese_text_line_with_bkimg(dst_w,dst_h,bk_img_path,text,start_point,font,save_path):
    im = create_an_image(bk_img_path, dst_w, dst_h)
    draw = ImageDraw.Draw(im)
    draw.text(start_point, text, fill=(0, 0, 0), font=font)
    im.save(save_path, quality=95)


if __name__ == '__main__':
    #Load font
    other_font = ImageFont.truetype('resource/font/hei.ttf', 19)
    bk_img_path = "resource/bkimg/paper1.png"
    text = "Hello world,你好,世界"
    start_point = (5,5)
    save_path = "res/line_res.png"
    gen_chinese_text_line_with_bkimg(280,32,bk_img_path,text,start_point,other_font,save_path)




