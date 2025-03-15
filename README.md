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
2. git clone https://github.com/DrkTriad/SubwayCameraControl.git.git
cd subway_hand_control
