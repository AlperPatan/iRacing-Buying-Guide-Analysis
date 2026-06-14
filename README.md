# 🏎️ iRacing Track Popularity & Cost Optimization Analyzer

📊 **A Data-Driven Guide to Smart Purchasing in iRacing**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data_Analysis-Pandas-emerald.svg?style=for-the-badge)
![iRating Otority](https://img.shields.io/badge/Driver_Authority-4.6K_iRating-orange.svg?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open_Source-❤️-red.svg?style=for-the-badge)

---

## 📌 Project Overview
Buying tracks in iRacing can get expensive quickly. This project uses automated data analysis to scrape, clean, and evaluate historical season calendars. By tracking how frequently each track appears across the most popular series (GT3, Porsche Cup, IMSA, etc.), this script generates a mathematically optimized **Top 10 "Must-Have" Tracks** list to help drivers get the highest possible return on investment (ROI).

🎥 **Watch the full breakdown and cinematic analysis on YouTube:** [iRacing'e Başlarken Almanız Gereken Altın Liste! (Top 10 + Bonus) 🚀](https://youtu.be/nMIAMZpj_Xo)

---

## 🚀 Key Features
- **Automated Data Processing:** Cleans and parses schedule datasets via Python (`dataset.py` & `analysis.py`).
- **Frequency Matrix:** Ranks tracks based on actual usage counts across high-population official series.
- **Cost Optimization Logic:** Factors in official iRacing volume discounts (3-piece %10, 6-piece %15) to build ideal shopping carts.
- **Strategic Insights:** Distinguishes between base content, legendary endurance tracks (Spa 24h, Daytona 24h, Sebring 12h), and "Honorable Mentions" like the Nürburgring Nordschleife complex.

---

## 🛠️ Architecture & Tech Stack
- **Language:** Python 3.9+
- **Data Wrangling:** Pandas, NumPy
- **Storage/Formats:** CSV / JSON Data Structures
- **Environment Management:** Python Virtual Environments (`venv`)

---

## 📦 File Structure
```text
├── dataset/               # Raw and processed schedule data
├── analysis.py            # Main data analysis and ranking algorithm
├── dataset.py             # Data loader and preprocessing script
├── .gitignore             # Keeps the repository clean
└── README.md              # You are here!
```
---

## 🤝 Need Extra tenths? Let's Connect!
Are you trying to master these tracks but still finding yourself off the pace?
As a 4.6K iRating driver and content creator, I don't just analyze data—I push the limits on the tarmac.

YouTube Channel: [@MaxPatan](https://youtube.com/@MaxPatan)

Coaching & Inquiries: Drop a comment on the YouTube video or open an issue here to join our upcoming Turkish Track Guide & Coaching Series!

Disclaimer: This project is an independent analytical tool and is not officially affiliated with iRacing.com.
