# Z-Ping - Tizim Monitoring Dasturi 🖥️

Z-Ping - bu Python dasturlash tilida yozilgan, tizim va tarmoq monitoringi uchun mo'ljallangan GUI dastur. Bu dastur orqali IP manzillarni tekshirish va tizim ma'lumotlarini kuzatish mumkin.

## Asosiy Xususiyatlari 🌟

- IP manzillarni tekshirish va ping yuborish
- Tizim ma'lumotlarini kuzatish:
  - Operatsion tizim ma'lumotlari
  - Foydalanuvchi nomi
  - Tarmoq tezligi
  - Tizim ishga tushgan vaqt
  - CPU ishlash ko'rsatkichlari
  - Operativ xotira holati
  - GPU ishlash ko'rsatkichlari
- Natijalarni jadval ko'rinishida ko'rsatish
- Natijalarni faylga saqlash imkoniyati

## O'rnatish 📥

1. Repositoriyani klonlash:

bash
git clone https://github.com/username/Z-ping.git
cd Z-ping

2. Kerakli kutubxonalarni o'rnatish:

bash
pip install -r requirements.txt
 
## Ishlatish 🚀

Dasturni ishga tushirish uchun:
 bash
python Z-ping.py

 
## Kerakli Kutubxonalar 📚

- tkinter
- subprocess
- socket
- platform
- getpass
- psutil
- GPUtil
- datetime

## Foydalanish Ko'rsatmalari 📖

1. IP manzilni to'rt qismga bo'lib kiriting
2. "Ping yuborish" tugmasini bosing
3. Natijalar jadvalda ko'rsatiladi
4. Natijalarni saqlash uchun "Natijalarni saqlash" tugmasini bosing
5. Jadvalni tozalash uchun "Jadvalni tozalash" tugmasini bosing

## Litsenziya 📝

Bu dastur [MIT](LICENSE) litsenziyasi ostida tarqatiladi.

## Muallif 👨‍💻

Dastur muallifi: [Ismingiz]
- GitHub: [@username]
- Telegram: [@username]

## Yordam Berish 🤝

Agar siz loyihaga hissa qo'shmoqchi bo'lsangiz:
1. Fork qiling
2. Yangi branch yarating (`git checkout -b feature/yangilik`)
3. O'zgarishlarni commit qiling (`git commit -am 'Yangi funksiya qo'shildi'`)
4. Branch'ni push qiling (`git push origin feature/yangilik`)
5. Pull Request yarating

## Muammolar va Takliflar 💡

Agar dasturda xatoliklar topsangiz yoki yangi g'oyalaringiz bo'lsa, (https://t.me/ZiyoTurakulov) bo'limida yangi muammo yarating.
 
 
 IP manzilga ping yuborish imkonini beradi. Keling, asosiy qismlarini ko'rib chiqamiz:
1. Kutubxonalar: Dastur tkinter, subprocess, socket, platform, getpass, psutil, GPUtil, va datetime kutubxonalaridan foydalanadi. Bu kutubxonalar foydalanuvchi interfeysi yaratish, tizim ma'lumotlarini olish, va tarmoq operatsiyalarini bajarish uchun ishlatiladi.
PingApp Klass: Bu klass tkinter asosida GUI yaratadi va asosiy funksiyalarni o'z ichiga oladi.
__init__ Metodi: Dastur oynasini yaratadi va create_widgets metodini chaqiradi.
create_widgets Metodi: Foydalanuvchi interfeysini yaratadi, jumladan IP manzil kiritish uchun maydonlar, ping tugmasi, natijalar jadvali, saqlash va tozalash tugmalari.
Ping Funksiyasi:
Foydalanuvchi kiritgan IP manzilni oladi va uni tekshiradi.
Agar IP manzil to'g'ri bo'lsa, tizim ma'lumotlarini (OS, foydalanuvchi, tarmoq tezligi, CPU, xotira, GPU) oladi va natijalarni jadvalga qo'shadi.
Agar xato yuz bersa, xato xabari ko'rsatiladi.
4. Qo'shimcha Funksiyalar:
validate_ip: IP manzilning to'g'riligini tekshiradi.
get_network_speed: Tarmoq tezligini aniqlaydi.
get_uptime: Tizimning ishga tushgan vaqtidan beri o'tgan vaqtni qaytaradi.
get_domain: IP manzilga mos domen nomini oladi.
get_gpu_usage: GPU ishlash ko'rsatkichlarini oladi.
save_to_file: Natijalarni faylga saqlaydi.
clear_results: Jadvaldagi natijalarni tozalaydi.
Asosiy Qism: Dastur tkinter oynasini ishga tushiradi va PingApp klassidan nusxa yaratadi.
Bu dastur foydalanuvchiga IP manzilni kiritish va unga ping yuborish orqali tarmoq va tizim ma'lumotlarini olish imkonini beradi. Natijalar jadvalda ko'rsatiladi va faylga saqlanishi mumkin.
