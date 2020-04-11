from PIL import ImageFont
from utils.idcard_entity import *
from utils.idcard_generator import *
name_font = ImageFont.truetype('resource/font/hei.ttf', 72)
other_font = ImageFont.truetype('resource/font/hei.ttf', 60)
bdate_font = ImageFont.truetype('resource/font/fzhei.ttf', 60)
id_font = ImageFont.truetype('resource/font/ocrb10bt.ttf', 72)

random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
areaCode = "500101"
id = generate_id(areaCode, random_sex)
provinceName="重庆市"
cityName = "万州区"
addr = "重庆市万州区园丁路41号"
name = "张三"
nation = "土家"
idcard = IDCard(name,nation,addr,id,provinceName,cityName)
idcard_empty_path = "resource/bkimg/idcard_empty.png"
idcard_photo_path = "resource/bkimg/idcard_avatar.png"
bk_path = "resource/bkimg/black.jpg"
idcard_save_dir = "res/"
generator(idcard, name_font, other_font, bdate_font, id_font,idcard_empty_path,
          idcard_photo_path,idcard_save_dir,bk_path)