# Subway surfers Hand control

## Deskripsi
Proyek ini adalah aplikasi berbasis Python yang memungkinkan Anda mengontrol game *Subway Surfers* menggunakan gerakan tangan. Dengan memanfaatkan webcam, proyek ini mendeteksi gestur tangan melalui library MediaPipe dan menerjemahkannya menjadi input keyboard untuk menggerakkan karakter di game.

Proyek ini dikembangkan sebagai bagian dari eksplorasi teknologi computer vision dan interaksi manusia-komputer (HCI). Cocok untuk Anda yang ingin mencoba pengalaman bermain game dengan cara baru yang inovatif!

## Fitur
- *Kontrol Berbasis Gestur*:
  - Tangan terbuka penuh: Lompat (Space).
  - Tangan menunjuk ke bawah: Tunduk (Tombol Bawah).
  - Hanya telunjuk terbuka: Bergerak ke kiri (Tombol Kiri).
  - Hanya jari tengah terbuka: Bergerak ke kanan (Tombol Kanan).
- Mendeteksi gerakan tangan secara real-time menggunakan webcam.
- Kompatibel dengan emulator Android seperti BlueStacks untuk menjalankan Subway Surfers.

## Prasyarat
Sebelum menjalankan proyek ini, pastikan Anda memiliki:
- *Python 3.10* (versi yang kompatibel dengan MediaPipe).
- Emulator Android seperti *BlueStacks* dengan game *Subway Surfers* terinstall.
- Webcam untuk mendeteksi gestur tangan.
- Library Python berikut:
  - opencv-python
  - mediapipe
  - pyautogui

## Cara Instalasi
1. *Clone Repository*:
2. git clone https://github.com/DrkTriad/SubwayCameraControl.git
cd subway_hand_control

2. *Instal Python dan Library*:
Pastikan Python 3.10 terinstall, lalu jalankan:

pip install opencv-python mediapipe pyautogui

3. *Jalankan Emulator*:
- Buka BlueStacks (atau emulator lain) dan jalankan Subway Surfers.
- Pastikan emulator menerima input keyboard dengan mengklik jendela game.

4. *Jalankan Program*:

python subway_hand_control.py

## Cara Menggunakan
1. Pastikan webcam Anda aktif.
2. Jalankan program subway_hand_control.py.
3. Hadapkan tangan Anda ke webcam untuk mengontrol game:
- Tangan terbuka: Lompat.
- Tangan ke bawah: Tunduk.
- Hanya telunjuk: Ke kiri.
- Hanya jari tengah: Ke kanan.
4. Tekan tombol q di jendela webcam untuk keluar dari program.

## Troubleshooting
- *Webcam Tidak Terdeteksi*: Ganti cv2.VideoCapture(0) ke cv2.VideoCapture(1) jika Anda memiliki lebih dari satu kamera.
- *Input Tidak Berfungsi*: Pastikan jendela emulator aktif (klik di dalamnya sebelum menjalankan program).
- *Gestur Tidak Akurat*: Sesuaikan pencahayaan atau jarak tangan dari webcam.

## Teknologi yang Digunakan
- *Python*: Bahasa pemrograman utama.
- *MediaPipe*: Untuk deteksi gestur tangan.
- *OpenCV*: Untuk pengolahan video dari webcam.
- *PyAutoGUI*: Untuk mensimulasikan input keyboard.
- *BlueStacks*: Emulator untuk menjalankan Subway Surfers.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini:
1. Fork repository ini.
2. Buat branch baru (git checkout -b fitur-baru).
3. Commit perubahan Anda (git commit -m "Menambahkan fitur X").
4. Push ke branch (git push origin fitur-baru).
5. Buat Pull Request.


## Kontak
Jika ada pertanyaan atau saran, hubungi saya di gilangafs02@gmail.com atau buka issue di repository ini.
