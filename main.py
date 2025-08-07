import tldextract
import os
from collections import Counter
import time

# --- Kelas untuk pewarnaan terminal ---
class Warna:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m' # Kembali ke warna default
    BOLD = '\033[1m'

def tampilkan_sambutan():
    """Menampilkan splash screen / kata sambutan saat program pertama kali jalan."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    art = r"""
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗██╗  ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝╚██╗██╔╝
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    █████╗   ╚███╔╝ 
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝   ██╔██╗ 
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ███████╗██╔╝ ██╗
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═╝
    """
    print(f"{Warna.CYAN}{art}{Warna.RESET}")
    print(f"{Warna.BOLD}Selamat Datang di Domain Extractor v3.0{Warna.RESET}".center(70))
    print("Sebuah tool sederhana untuk ekstraksi & analisis domain.".center(70))
    
    # --- TAMBAHAN KREDIT DI SINI ---
    # Ganti @NAMA_USER_TELEGRAM dengan username Telegram kamu.
    telegram_user = "https://t.me/lantasss" 
    print(f"Dibuat oleh: {Warna.BOLD}{telegram_user}{Warna.RESET}".center(70))
    # --------------------------------
    
    time.sleep(2.5) # Jeda sedikit lebih lama agar kredit terbaca

def ekstrak_domain(nama_file_input, nama_file_output, filter_tld=None):
    """Fungsi inti untuk mengekstrak domain dan menampilkan laporan."""
    # ... (Fungsi ini tidak diubah, sama seperti sebelumnya) ...
    if filter_tld is None:
        filter_tld = []
    unique_full_domains = set()
    try:
        with open(nama_file_input, 'r', encoding='utf-8') as file_input:
            urls = file_input.readlines()
            print(f"\n{Warna.YELLOW}Memulai proses ekstraksi domain...{Warna.RESET}")
            for url in urls:
                bersih_url = url.strip()
                if not bersih_url: continue
                extracted = tldextract.extract(bersih_url)
                if filter_tld and extracted.suffix not in filter_tld:
                    continue
                domain_utama = extracted.top_domain_under_public_suffix
                if extracted.subdomain:
                    full_domain = f"{extracted.subdomain}.{domain_utama}"
                else:
                    full_domain = domain_utama
                if full_domain:
                    unique_full_domains.add(full_domain)
        with open(nama_file_output, 'w', encoding='utf-8') as file_output:
            for domain in sorted(list(unique_full_domains)):
                file_output.write(domain + '\n')
        print(f"{Warna.GREEN}✅ Selesai! {len(unique_full_domains)} domain unik berhasil diekstrak.{Warna.RESET}")
        print(f"Hasilnya disimpan di file '{Warna.BOLD}{nama_file_output}{Warna.RESET}'")
        if not unique_full_domains:
            print(f"\n{Warna.YELLOW}Tidak ada domain untuk dianalisis.{Warna.RESET}")
            return
        print("\n" + "="*45)
        print(f"    {Warna.BOLD}LAPORAN STATISTIK TLD DARI HASIL{Warna.RESET}")
        print("="*45)
        tld_counts = Counter(tldextract.extract(domain).suffix for domain in unique_full_domains)
        total_domains = len(unique_full_domains)
        for tld, count in tld_counts.most_common():
            percentage = (count / total_domains) * 100
            print(f"{Warna.CYAN}{tld:<15}{Warna.RESET} | {count:>5} domain | ({percentage:.2f}%)")
        print("="*45)
    except FileNotFoundError:
        print(f"\n{Warna.RED}❌ Error: File input '{nama_file_input}' tidak ditemukan!{Warna.RESET}")
    except Exception as e:
        print(f"\n{Warna.RED}❌ Terjadi error saat memproses file: {e}{Warna.RESET}")

def tampilkan_menu():
    """Tampilan menu dengan sentuhan warna."""
    border = "="*35
    title = "PROGRAM DOMAIN EXTRACTOR"
    print(f"\n{Warna.HEADER}{border}{Warna.RESET}")
    print(f"      {Warna.BOLD}{title}{Warna.RESET}")
    print(f"{Warna.HEADER}{border}{Warna.RESET}")
    print("Pilih Opsi:")
    print(f"{Warna.YELLOW}1.{Warna.RESET} Ekstrak Semua Domain")
    print(f"{Warna.YELLOW}2.{Warna.RESET} Ekstrak Domain dengan Filter TLD")
    print(f"{Warna.YELLOW}3.{Warna.RESET} Keluar")
    print(f"{Warna.HEADER}{border}{Warna.RESET}")

def dapatkan_path_file():
    """Fungsi untuk meminta nama file input dan output dari user."""
    input_file = input(f"{Warna.CYAN}Masukkan nama file input (cth: urls.txt): {Warna.RESET}")
    output_file = input(f"{Warna.CYAN}Simpan hasil dengan nama file apa? (cth: hasil.txt): {Warna.RESET}")
    return input_file, output_file

# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    tampilkan_sambutan()
    while True:
        tampilkan_menu()
        pilihan = input(f"{Warna.BOLD}Masukkan pilihan Anda (1/2/3): {Warna.RESET}")

        if pilihan == '1':
            print("\n--- Opsi 1: Ekstrak Semua Domain ---")
            input_f, output_f = dapatkan_path_file()
            ekstrak_domain(input_f, output_f)
            input(f"\n{Warna.YELLOW}Tekan Enter untuk kembali ke menu utama...{Warna.RESET}")

        elif pilihan == '2':
            print("\n--- Opsi 2: Ekstrak dengan Filter TLD ---")
            input_f, output_f = dapatkan_path_file()
            tld_input = input(f"{Warna.CYAN}Filter TLD tertentu? (pisahkan koma, cth: com,id): {Warna.RESET}")
            tld_filters = [tld.strip().lower() for tld in tld_input.split(',')] if tld_input else []
            ekstrak_domain(input_f, output_f, tld_filters)
            input(f"\n{Warna.YELLOW}Tekan Enter untuk kembali ke menu utama...{Warna.RESET}")

        elif pilihan == '3':
            print(f"\n{Warna.GREEN}Terima kasih telah menggunakan program ini. Sampai jumpa!{Warna.RESET}")
            break

        else:
            print(f"\n{Warna.RED}❌ Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.{Warna.RESET}")
            input(f"{Warna.YELLOW}Tekan Enter untuk mencoba lagi...{Warna.RESET}")