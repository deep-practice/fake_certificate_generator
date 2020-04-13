# coding=utf-8
'''
code for generate vehicle license
'''
from PIL import Image,ImageFont,ImageDraw
from utils.vehicle_license_entity import VehicleLicense

def vl_front_generator(vl_info,ch_font,alphabet_font,font_size,bk_img_path,save_path):
    im = Image.open(bk_img_path)  # 加载模板
    draw = ImageDraw.Draw(im)
    draw.text((225, 170), vl_info.get_plate_number()[0], fill=(49, 60, 80), font=ch_font)
    draw.text((255, 170), vl_info.get_plate_number()[1:], fill=(49, 60, 80), font=alphabet_font)
    draw.text((600, 170), vl_info.get_vtype(), fill=(49, 60, 80), font=ch_font)
    draw.text((225, 230), vl_info.get_owner(), fill=(49, 60, 80), font=ch_font)
    draw.text((225, 300), vl_info.get_addr(), fill=(49, 60, 80), font=ch_font)
    draw.text((225, 360), vl_info.get_use_chara(), fill=(49, 60, 80), font=ch_font)
    draw.text((510, 360), vl_info.get_model_ch(), fill=(49, 60, 80), font=ch_font)
    draw.text((510 + len(vl_info.get_model_ch()) * font_size, 360), vl_info.get_model_num(), fill=(49, 60, 80),
              font=alphabet_font)
    draw.text((475, 430), vl_info.get_vin(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((460, 490), vl_info.get_engine_num(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((420, 560), vl_info.get_reg_date(), fill=(49, 60, 80), font=alphabet_font)
    draw.text((730, 560), vl_info.get_issue_date(), fill=(49, 60, 80), font=alphabet_font)
    im.save(save_path, quality=95)

if __name__ == '__main__':
    # Load font
    font_size = 30
    ch_font = ImageFont.truetype('resource/font/xingshi_ch.ttf', font_size)  # 看不出上面的字体是啥，可根据需要自行切换
    alphabet_font = ImageFont.truetype('resource/font/xsz_an_xi.ttf', font_size)
    bk_img_path = "resource/bkimg/vl_front.png"
    save_path = "res/vl_front_res.png"
    vl_front_info = VehicleLicense(
        plate_number="京A88888",
        vtype="小型轿车",
        owner="张三",
        addr="北京市石景山区",
        use_chara="非营运",
        model_ch="大众汽车牌",
        model_num="SVW6474DFD",
        vin="SSVUDDTT2J2022558",
        engine_num="111533",
        reg_date="2020-04-13",
        issue_date="2020-04-14"
    )
    vl_front_generator(vl_front_info,ch_font,alphabet_font,font_size,bk_img_path,save_path)






