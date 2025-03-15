import cv2
import mediapipe as mp
import pyautogui
import time

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Inisialisasi webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Tidak dapat membuka webcam.")
    exit()

# Variabel untuk mencegah input berulang
last_action = "idle"
action_cooldown = 0.2  # Cooldown dalam detik
last_action_time = time.time()

def detect_hand_gestures(landmarks):
    thumb_tip = landmarks[4]    # Ibu jari
    index_tip = landmarks[8]    # Telunjuk
    middle_tip = landmarks[12]  # Jari tengah
    ring_tip = landmarks[16]    # Jari manis
    pinky_tip = landmarks[20]   # Kelingking
    wrist = landmarks[0]        # Pergelangan
    
    # Tangan terbuka penuh (lompat)
    if (thumb_tip.y < wrist.y and 
        index_tip.y < wrist.y and 
        middle_tip.y < wrist.y and 
        ring_tip.y < wrist.y and 
        pinky_tip.y < wrist.y):
        return "jump"
    
    # Tangan ke bawah (tunduk)
    elif (index_tip.y > wrist.y and 
          middle_tip.y > wrist.y and 
          ring_tip.y > wrist.y):
        return "duck"
    
    # Hanya telunjuk terbuka (kiri)
    elif (index_tip.y < wrist.y and 
          middle_tip.y > wrist.y and 
          ring_tip.y > wrist.y):
        return "left"
    
    # Hanya jari tengah terbuka (kanan)
    elif (middle_tip.y < wrist.y and 
          index_tip.y > wrist.y and 
          ring_tip.y > wrist.y):
        return "right"
    
    return "idle"

# Loop utama
print("Program berjalan. Tekan 'q' untuk keluar.")
while True:
    success, img = cap.read()
    if not success:
        print("Error: Gagal membaca frame dari webcam.")
        break
    
    # Konversi ke RGB untuk MediaPipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Deteksi gesture
    action = "idle"
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            action = detect_hand_gestures(hand_landmarks.landmark)
    
    # Tampilkan aksi di webcam
    cv2.putText(img, f"Action: {action}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Terjemahkan ke input keyboard dengan cooldown
    current_time = time.time()
    if action != last_action and (current_time - last_action_time) > action_cooldown:
        if action == "jump":
            pyautogui.press("space")  # Lompat
            print("Lompat")
        elif action == "duck":
            pyautogui.keyDown("down")  # Tunduk
            time.sleep(0.3)  # Durasi tunduk
            pyautogui.keyUp("down")
            print("Tunduk")
        elif action == "left":
            pyautogui.press("left")  # Kiri
            print("Kiri")
        elif action == "right":
            pyautogui.press("right")  # Kanan
            print("Kanan")
        
        last_action = action
        last_action_time = current_time

    # Tampilkan webcam
    cv2.imshow("Hand Control - Subway Surfers", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("Program selesai.")