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
1. loyiha yaratish
```
aiogram-cli init <path>
```
```path``` parametrini o'rniga loyixangiz nomini yozing yoki nuqta qo'yisangiz ham bo'ladi

2. loyihani template bilan yaratish
```
aiogram-cli init --with-template
```
```--with-template``` bilan siz loyihani template bilan yaratishingiz mumkin

men yasagan template sodda va u handlerlar keyboardlar va statelarni o'z ichiga oladi va database yo'q (hozircha)

3. loyahaga majburiy obuna qo'shish, buning uchun siz ```aiogram-cli``` buyrug'idan keyin ```add force-follow-to-channel``` buyrig'ini yozishingiz kerak bo'ladi
```
aiogram-cli add force-follow-to-channel
```
majburiy obuna kodi handlers papkasini ichidagi users papkasini ichidagi start.py fayliga qo'shilari

4. loyihaga admin handler qo'shish
```
aiogram-cli add admin-handler <path>
```
buni qo'shganingizdan keyin siz ```.env``` fayliga kirib ADMIN_ID ni berishungiz kerak bo'ladi
# hozircha faqat shu