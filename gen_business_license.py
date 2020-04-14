# coding=utf-8
'''
code for generate vehicle license
'''
from PIL import Image,ImageFont,ImageDraw
from utils.bussiness_license_entity import BusinessLicense

def bl_generator(bl_info,ch_font,scope_font,bk_img_path,save_path):
    im = Image.open(bk_img_path)  # 加载模板
    draw = ImageDraw.Draw(im)
    draw.text((1560, 1320), bl_info.get_uscc(), fill=(0, 0, 0), font=ch_font)
    draw.text((744, 1455), bl_info.get_corp_name(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 1550), bl_info.get_corp_type(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 1645), bl_info.get_addr(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 1740), bl_info.get_legal_rep(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 1835), bl_info.get_regist_capital(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 1930), bl_info.get_establish_date(), fill=(49, 60, 80), font=ch_font)
    draw.text((744, 2025), bl_info.get_business_term(), fill=(49, 60, 80), font=ch_font)
    start = 0
    loc = 2120
    business_scope = bl_info.get_business_scope()
    while start + 28 < len(business_scope):
        draw.text((744, loc), business_scope[start:start + 28], fill=(49, 60, 80), font=scope_font)
        start += 28
        loc += 60
    draw.text((744, loc), business_scope[start:], fill=(49, 60, 80), font=scope_font)
    year,month,day = bl_info.get_issue_date().split("-")
    draw.text((1543, 3040), year, fill=(49, 60, 80), font=ch_font)
    draw.text((1773, 3040), month, fill=(49, 60, 80), font=ch_font)
    draw.text((1962, 3040), day, fill=(49, 60, 80), font=ch_font)
    im.save(save_path, quality=95)

if __name__ == '__main__':
    # Load font
    font_size = 43
    ch_font = ImageFont.truetype('resource/font/simsun.ttf', font_size)  # 看不出上面的字体是啥，可根据需要自行切换
    scope_font = ImageFont.truetype('resource/font/simsun.ttf', 35)
    bk_img_path = "resource/bkimg/bl_empty.jpg"
    save_path = "res/bl_res.jpg"
    bl_info = BusinessLicense(
        corp_name="上海丙叮科技技术有限公司",
        corp_type="有限责任公司(自然人投资或控股)",
        uscc="91310101MA1K31K168",
        regist_number=None,
        addr="中国(上海)南京北路211号海瑞大厦302室",
        legal_rep=" 洗良辰",
        regist_capital="人民币1757.8130万元整",
        establish_date="2015年11月19日",
        validate_for="2045年11月18日",
        business_scope="体育用品、化妆品的销售，商务信息咨询，从事网络科技领域，计算机科技专业领域内的技术开发"
                       +"，技术转让，技术咨询,技术服务，计算机系统服务、设计、制作、代理、发布各类广告，体育赛事"
                       +"的策划，电子商务，电信业务，从事货物及技术的进出口业务。",
        issue_date="2018-12-20"
    )
    bl_generator(bl_info,ch_font,scope_font,bk_img_path,save_path)






