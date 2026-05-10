# Transport Logistikasi Kalkulyatori

Yuk tashish narxini avtomatik hisoblaydigan Python dasturi.

---

## Vazifasi

Ushbu dastur logistika kompaniyalari va yuk jo'natuvchilar uchun mo'ljallangan bo'lib, masofa va yuk vazniga qarab tashish narxini tezda hisoblaydi. 10 tonnadan ortiq yuklar uchun avtomatik chegirma qo'llaniladi.

---

## Imkoniyatlar

- Masofa (km) va yuk vazni (tonna) asosida narx hisoblash
- Har bir tonna-kilometr uchun: **500 so'm**
- 10 tonnadan ortiq yuklarga **10% chegirma**
- Asosiy narx, chegirma miqdori va yakuniy narxni alohida ko'rsatish

---

## Ishlatish

### Talablar

- Python 3.x

### Ishga tushirish

```bash
python main.py
```

### Misol

```
=== Yuk Tashish Narxini Hisoblash ===
Masofani kiriting (km): 200
Yuk vaznini kiriting (tonna): 15

Masofa:         200 km
Yuk vazni:      15 tonna
Asosiy narx:    1,500,000 so'm
Chegirma:       -10% (-150,000 so'm)
Jami narx:      1,350,000 so'm
```

---

## Narx formulasi

```
Asosiy narx = Masofa × Vazn × 500
Chegirma    = Asosiy narx × 10%  (faqat vazn > 10 tonna bo'lsa)
Jami narx   = Asosiy narx − Chegirma
```

---

## Fayl tuzilmasi

```
logistika-loyiha/
├── main.py       # Asosiy dastur
└── README.md     # Loyiha haqida ma'lumot
```
