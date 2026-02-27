<div align="center">

# 🔄 VidLoop

### *Simple Video Upload & Share Platform with Loop Support*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <strong>Videolarını yükle, benzersiz link al, herkesle paylaş!</strong>
</p>

---

</div>

## ✨ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 📤 **Kolay Yükleme** | Sürükle-bırak veya dosya seçerek video yükle |
| 🔗 **Benzersiz Link** | Her video için otomatik paylaşım linki |
| 🔄 **Tekrar Seçenekleri** | Sonsuz döngü veya belirli sayıda tekrar |
| 📁 **Çoklu Format** | MP4, WebM, OGG, MOV desteği |
| 📦 **200 MB Limit** | Büyük dosya yükleme desteği |

---

## 🚀 Hızlı Kurulum

### 1. Repoyu Klonla
```bash
git clone https://github.com/KULLANICI_ADINIZ/vidloop.git
cd vidloop
```

### 2. Virtual Environment Oluştur

<details>
<summary>🪟 Windows</summary>

```bash
python -m venv .venv
.venv\Scripts\activate
```
</details>

<details>
<summary>🐧 Linux / 🍎 macOS</summary>

```bash
python3 -m venv .venv
source .venv/bin/activate
```
</details>

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 4. Çalıştır
```bash
python app.py
```

### 5. Tarayıcında Aç
```
🌐 http://127.0.0.1:5000
```

---

## 📖 Kullanım

```
1️⃣  Ana sayfada video dosyanı seç
2️⃣  "Yükle" butonuna tıkla
3️⃣  Oluşan linki kopyala ve paylaş!
```

### 🎛️ URL Parametreleri

| Parametre | Örnek | Açıklama |
|-----------|-------|----------|
| `loop` | `?loop=true` | Video sonsuz döngüde oynar |
| `repeats` | `?repeats=5` | Video 5 kez tekrar eder |

**Örnek kullanım:**
```
https://site.com/watch/abc123?loop=true
https://site.com/watch/abc123?repeats=3
```

---

## 📂 Proje Yapısı

```
vidloop/
├── 📄 app.py              # Ana Flask uygulaması
├── 📄 requirements.txt    # Python bağımlılıkları
├── 📁 templates/
│   ├── upload.html        # Yükleme sayfası
│   └── watch.html         # Video izleme sayfası
├── 📁 uploads/            # Yüklenen videolar
└── 📁 static/             # Statik dosyalar
```

---

## 🛠️ Gereksinimler

- **Python** 3.10 veya üzeri
- **Flask** 2.3.2
- **Werkzeug** 2.3.6

---

## 🤝 Katkıda Bulunma

1. Fork'la 🍴
2. Feature branch oluştur (`git checkout -b feature/awesome`)
3. Commit at (`git commit -m 'Add awesome feature'`)
4. Push et (`git push origin feature/awesome`)
5. Pull Request aç 🎉

---

## 📝 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.

---

<div align="center">

**Burak tarafından 💜 ile yapıldı

</div>
