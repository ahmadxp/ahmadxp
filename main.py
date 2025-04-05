import os
import time
from datetime import datetime

# Konfigurasi
REPO_PATH = "/path/to/your/repository"  # Ganti dengan path repo lokal Anda
COMMIT_MESSAGE = "Scheduled daily commit at 15:00"
FILE_TO_MODIFY = "stamp.txt"  # File yang akan dimodifikasi untuk commit

def perform_commit():
    # Pindah ke direktori repo
    os.chdir(REPO_PATH)
    
    # Modifikasi file (tambahkan timestamp)
    with open(FILE_TO_MODIFY, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Daily commit at {timestamp}\n")
    
    # Git commands
    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')
    os.system("git push origin main")  # Ganti 'main' dengan branch Anda jika berbeda
    
    print(f"Committed at {timestamp} - Daily commit")

def main():
    print("Starting daily auto-commit script (15:00 only)...")
    
    while True:
        now = datetime.now()
        
        # Cek jika sekarang jam 15:00
        if now.hour == 15 and now.minute == 0:
            perform_commit()
            # Tunggu 1 menit untuk menghindari multiple commits di jam yang sama
            time.sleep(60)
        
        # Cek setiap 30 detik untuk efisiensi
        time.sleep(30)

if __name__ == "__main__":
    main()
