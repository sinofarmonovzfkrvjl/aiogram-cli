# aiogram-cli version - 1.0.7

bu aiogram uchun cli (command line tool)

siz bu cli yordamida loyihalarni osonlik bilan kam vaqt ichida yasay olasiz, handler, funksiyalarni qisqa vaqt ishida qo'shaolasiz

# O'RNATISH

1. repositoriyni clone qiling
```
git clone https://github.com/sinofarmonovzfkrvjl/aiogram-cli.git
```

2. setup.py fayli joylashgan joydan terminal oching
```
pip install .
```

3. Siz aiogram-cli ni ornatdizgiz, endi kodni o'chirib tashlashingiz mumkin

# ISHLATISH
loyiha yaratish
```
aiogram-cli init <path>
```
```path``` parametrini o'rniga loyixangiz nomini yozing yoki nuqta qo'yisangiz ham bo'ladi

loyihani template bilan yaratish
```
aiogram-cli init --with-template
```
```--with-template``` bilan siz loyihani template bilan yaratishingiz mumkin

men yasagan template sodda va u handlerlar keyboardlar statelarni a middlewareni o'z ichiga oladi va database yo'q (hozircha)

loyihani ishga tushiish
```
aiogram-cli run <file_name.py>
```
savol: nega ```python file_name.py``` qilib ishga tushirsak ham bo'ladiku?
javob: bu ```python file_name.py```chunki bu reload qilaoladi yani qaysidir faylga qaysidir kod yozilsa yoki qaysidir kod o'chirib tashlansa, bu o'zgarishni payqaydi loyihani qayta ishga tushirib yuboradi va har safar loyihani qo'lda to'xtatib yana qo'lda ishga tushirmasligingizni oldini oladi 

loyahaga majburiy obuna qo'shish, buning uchun siz ```aiogram-cli``` buyrug'idan keyin ```add force-follow-to-channel``` buyrig'ini yozishingiz kerak bo'ladi
```
aiogram-cli add force-follow-to-channel
```
majburiy obuna kodi handlers papkasini ichidagi users papkasini ichidagi start.py fayliga qo'shilari

loyihaga admin handler qo'shish, yani admin panel
```
aiogram-cli add admin-handler <path>
```
buni qo'shganingizdan keyin siz ```.env``` fayliga kirib ADMIN_ID ni berishungiz kerak bo'ladi

loyihaga telefon raqamni qabul qiluvchi handler qo'shish buning uchun siz ```add phone-number-handler``` dan foydalishingiz kerak bo'ladi
```
aiogram-cli add phone-number-handler
```

Loyihaga joylashuvni qabul qiluvchi handler qo'shish
```
aiogram-cli add location-handler
```

# hozircha faqat shu