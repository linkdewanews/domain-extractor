# 🚀 Domain Extractor & Analyzer

![Versi Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Lisensi](https://img.shields.io/badge/License-MIT-green.svg)

Sebuah tool CLI (Command-Line Interface) sederhana namun powerful yang ditulis dengan Python untuk mengekstrak, menganalisis, dan mengelola daftar domain dari sekumpulan URL.

![Demo Program](https://i.imgur.com/uR1k3aY.gif)
*(Saran: Ganti link gambar di atas dengan link GIF demo program buatanmu sendiri)*

---

## ✨ Fitur Unggulan

-   **🎨 Tampilan Menu Interaktif:** Antarmuka yang ramah pengguna dengan menu berbasis pilihan dan pewarnaan cerdas untuk keterbacaan maksimal.
-   ** extractor:** Ekstrak domain lengkap (termasuk subdomain) dari file berisi ribuan URL.
-   **
-   **📊 Laporan Statistik Otomatis:** Setiap selesai mengekstrak, program akan otomatis menampilkan laporan statistik TLD dari domain yang berhasil diekstrak.
-   **🗑️ Pembersihan Duplikat:** Hasil ekstraksi dijamin unik, karena duplikat domain akan otomatis dibersihkan.
-   **💾 Simpan ke File:** Simpan hasil ekstraksi yang bersih ke dalam file `.txt` dengan nama kustom.
-   **👋 Layar Sambutan:** Dilengkapi dengan *splash screen* keren saat pertama kali dijalankan.

---

## ⚙️ Instalasi

Untuk menjalankan tool ini, pastikan kamu sudah menginstal **Python 3.7** atau versi yang lebih baru.

1.  **Clone repository ini ke komputermu:**
    ```bash
    git clone [https://github.com/linkdewanews/domain-extractor.git](https://github.com/linkdewanews/domain-extractor.git)
    ```

2.  **Masuk ke direktori proyek:**
    ```bash
    cd domain-extractor
    ```

3.  **Instal semua modul yang dibutuhkan:**
    Perintah ini akan membaca file `requirements.txt` dan menginstal `tldextract`.
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Cara Penggunaan

Setelah instalasi selesai, jalankan program dengan perintah berikut di terminal:

```bash
python main.py