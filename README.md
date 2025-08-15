# 🎬 Movie Review Sentiment Analysis with IBM Granite

## 📌 Project Overview

Proyek ini bertujuan untuk melakukan analisis sentimen pada ulasan film, mengklasifikasikan review menjadi **Positive** atau **Negative**, serta mengekstrak insight dari dataset.
Pendekatan ini memanfaatkan **IBM Granite LLM** untuk _classification_, _summarization_, _keyword extraction_, dan pembuatan insight otomatis.
Dataset yang digunakan berimbang (50% positif, 50% negatif) sehingga cocok untuk pelatihan model machine learning tanpa bias signifikan.

## 📂 Raw Dataset

- **Sumber:** [Dataset IMDB Movie Review](https://ai.stanford.edu/~amaas/data/sentiment/)
- Jumlah data: **50.000 review** (25.000 positif, 25.000 negatif)

## 🔍 Research Questions

1. Berapa persentase review Positive dan Negative?
2. Kata-kata apa yang paling sering muncul di review Positive dan Negative?
3. Apakah review positif cenderung lebih panjang atau pendek dibanding review negatif?
4. Frasa dua kata (bigram) apa yang paling sering muncul pada masing-masing sentimen?

## 📊 Data Insights

1. **Distribusi Sentimen**

   - Seimbang 50:50 → 25.000 review positif & 25.000 review negatif.
   - Tidak ada dominasi satu sentimen, sehingga model tidak bias awal.

2. **Kata Dominan**

   - Kata umum seperti _movie_, _film_, _character_ muncul di kedua sentimen.
   - Pembeda utama ada di kata sifat (_good/great_ → positif, _bad/even_ → negatif).

3. **Panjang Review**

   - Positif lebih panjang (maks ≈ 2.500 kata) dibanding negatif (maks ≈ 1.500 kata).
   - Orang cenderung menulis lebih detail saat puas.

4. **Bigram Populer**

   - Positif: _great movie_, _well done_, _highly recommend_
   - Negatif: _waste time_, _poor acting_, _bad movie_

### 📌 AI-Generated Insights

1. **Positive Themes**

   - Akting memukau
   - Cerita unik dan engaging
   - Sinematografi kuat
   - Karakter memorable
   - Humor & skor musik bagus

2. **Negative Themes**

   - Akting buruk / overacting
   - Plot lemah atau membingungkan
   - Produksi rendah
   - Karakter stereotip
   - Humor ofensif atau tidak lucu

3. **Korelasi Panjang Review & Sentimen**

   - Tidak ada korelasi langsung, tapi review panjang biasanya lebih detail.

---

## 📌 Kesimpulan

- Kata sifat adalah indikator utama sentimen.
- Review positif umumnya lebih panjang → menandakan kepuasan memicu cerita detail.
- Fokus review positif pada _story_ dan _character_.

## 💡 Rekomendasi

**Untuk Produser Film:**

- Tingkatkan kualitas _story_ dan _character development_.
- Hindari elemen yang sering dikritik (pacing lambat, durasi berlebihan).

**Untuk Platform Review:**

- Gunakan AI untuk membuat _summary_ otomatis.
- Tambahkan _keyword tagging_ otomatis agar pembaca cepat memahami isi review.

---

## 🛠 Tools & Libraries

- **Python 3.10+**
- **Pandas** → Data processing
- **Matplotlib / Seaborn** → Visualisasi
- **NLTK / Scikit-learn** → Text processing & feature extraction
- **IBM Watsonx.ai & Granite LLM** → Sentiment classification, summarization, keyword extraction, AI insights
- **Google Colab** → Eksekusi notebook

---

## 🤖 Model Prediksi

- **IBM Granite-13b-instruct-v2** → Classification (Positive/Negative)
- **IBM Granite-13b-chat-v2** → Summarization & Keyword Extraction
- Evaluasi menggunakan **Accuracy, Precision, Recall, F1-score** terhadap data validasi.

---

## 📌 AI Support Explanation

AI digunakan di tahap:

1. **Sentiment Classification** → Granite mengklasifikasikan review ke positif atau negatif.
2. **Summarization** → Granite membuat ringkasan tiap review.
3. **Keyword Extraction** → Granite mengambil kata kunci penting dari review.
4. **Insight Generation** → Granite membuat insight otomatis dari pola data.

---

Kalau mau, aku bisa sekalian buatkan **versi README ini dalam format markdown siap commit ke GitHub**, plus menambahkan tabel _sentiment accuracy_ hasil evaluasi model.
Kamu mau aku lanjut buatkan versinya?
