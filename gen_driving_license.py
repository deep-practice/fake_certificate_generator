# coding=utf-8
'''
code for generate driving license
'''
from PIL import Image,ImageFont,ImageDraw
from utils.driving_license_entity import DrivingLicense
import cv2
import numpy as np

def dl_front_generator(dl_info,name_ch_font,other_ch_font,alphabet_font,bk_img_path,save_path,photo):
    im = Image.open(bk_img_path)  # 加载模板
    draw = ImageDraw.Draw(im)
    draw.text((412, 125), dl_info.get_id_number(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((150, 180), dl_info.get_name(), fill=(49, 60, 80), font=name_ch_font)
    draw.text((570, 190), dl_info.get_gender(), fill=(49, 60, 80), font=other_ch_font)
    draw.text((800, 190), dl_info.get_nation(), fill=(49, 60, 80), font=other_ch_font)
    draw.text((173, 260), dl_info.get_addr(), fill=(49, 60, 80), font=other_ch_font)
    draw.text((429, 390), dl_info.get_birth_date(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((490, 465), dl_info.get_issue_date(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((520, 535), dl_info.get_class(), fill=(49, 60, 80), font=name_ch_font)
    draw.text((285, 620), dl_info.get_validate_from(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((620, 620), dl_info.get_validate_for(), fill=(49, 60, 80), font=alphabet_font)
    photo=photo.resize((224,358), Image.BILINEAR)
    im.paste(photo, box=(790, 330,790+photo.width,330+photo.height))
    im.save(save_path, quality=95)

if __name__ == '__main__':
    # Load font
    name_font_size = 45
    other_font_size = 32
    name_ch_font = ImageFont.truetype('resource/font/hei.ttf', name_font_size)  # 看不出上面的字体是啥，可根据需要自行切换
    other_ch_font = ImageFont.truetype('resource/font/hei.ttf', other_font_size)
    alphabet_font = ImageFont.truetype('resource/font/xsz_an_cu.ttf', other_font_size)
    bk_img_path = "resource/bkimg/dl_front_empty.jpg"
    save_path = "res/dl_front_res.png"
    dl_front_info = DrivingLicense(
        id_number="130428198812180013",
        name="张三",
        gender="男",
        nation="中国",
        addr="北京市石景山区",
        birth_date="1998-01-01",
        issue_date="2020-04-14",
        cls="C1",
        validate_from="2020-04-14",
        validate_for="2026-04-14"
    )
    photo = Image.open("resource/bkimg/photo.png")
    dl_front_generator(dl_front_info,name_ch_font,other_ch_font,alphabet_font,bk_img_path,save_path,photo)






