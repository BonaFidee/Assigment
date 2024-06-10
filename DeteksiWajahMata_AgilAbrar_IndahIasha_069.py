import cv2

# Muat model Haar Cascade untuk deteksi wajah dan mata
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Fungsi untuk mendeteksi wajah dan mata
def deteksi_wajah_dan_mata(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Gambar persegi panjang di sekitar wajah yang terdeteksi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            # Gambar persegi panjang di sekitar mata yang terdeteksi
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return frame

# Deteksi mata dan wajah dari webcam
def detektor_wajah_dan_mata_webcam():
    video_capture = cv2.VideoCapture(0)
    while True:
        # Ambil frame-by-frame dari webcam
        ret, frame = video_capture.read()
        
        # Deteksi wajah dan mata
        canvas = deteksi_wajah_dan_mata(frame)
        
        # Tampilkan hasil dalam jendela
        cv2.imshow('Detektor Wajah dan Mata', canvas)
        
        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Rilis capture dan tutup jendela
    video_capture.release()
    cv2.destroyAllWindows()

# Jalankan deteksi mata dan wajah dari webcam
detektor_wajah_dan_mata_webcam()
