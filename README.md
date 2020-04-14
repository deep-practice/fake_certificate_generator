# idcard generator
A simple code for generating idcard,academic research only

envioriment
====
```
pip install -r requirements.txt 
```
if no pip module found on your machine,you should install one first

usage
====

* generate idcard image
```
python gen_idcard.py
```
![image](https://github.com/deep-practice/idcard_generator/blob/master/res/idcard_front.jpg)  
*  generate vehicle license
```
python gen_vehicle_license.py
```
![image](https://github.com/deep-practice/fake_certificate_generator/blob/master/res/vl_front_res.png)   

*  generate driving license
```
python gen_driving_license.py
```
![image](https://github.com/deep-practice/fake_certificate_generator/blob/master/res/dl_front_res.png)  
*  generate image with given text
```
python gen_text_line.py
```
![image](https://github.com/deep-practice/idcard_generator/blob/master/res/line_res.png)  
if no error occurs,you can see the result in res dir
,otherwise you should change the line
```
_, contours, _= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
to
```
contours, _= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
