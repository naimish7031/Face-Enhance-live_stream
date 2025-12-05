import cv2
import numpy as np

# Haar cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam (auto-detect)
for i in range(3):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        print(f"✅ Camera working at index {i}")
        break

if not cap.isOpened():
    print("❌ Camera not found")
    exit()


def enhance_face(face):
    # 1️⃣ Strong skin smoothing
    smooth = cv2.bilateralFilter(face, 15, 120, 120)

    # 2️⃣ Very high glow effect
    glow = cv2.GaussianBlur(smooth, (0, 0), 15)  # High blur for strong glow
    glow = cv2.addWeighted(smooth, 1.4, glow, -0.4, 0)

    # 3️⃣ Strong brightness + contrast
    bright = cv2.convertScaleAbs(glow, alpha=1.25, beta=25)

    # 4️⃣ Dark red overlay
    red_overlay = np.zeros_like(bright, dtype=np.uint8)
    red_overlay[:, :, 2] = 80  # Red channel
    red_overlay[:, :, 1] = 0   # Green channel
    red_overlay[:, :, 0] = 0   # Blue channel
    final = cv2.addWeighted(bright, 0.85, red_overlay, 0.15, 0)

    # 5️⃣ Blend with original face for natural texture
    final = cv2.addWeighted(final, 0.65, face, 0.35, 0)
    return final


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        # ✅ Bigger padding → full face coverage
        pad_w = int(0.40 * w)
        pad_h = int(0.35 * h)

        x1 = max(0, x - pad_w)
        y1 = max(0, y - pad_h)
        x2 = min(frame.shape[1], x + w + pad_w)
        y2 = min(frame.shape[0], y + h + pad_h)

        face_roi = frame[y1:y2, x1:x2]

        enhanced = enhance_face(face_roi)

        frame[y1:y2, x1:x2] = enhanced

    cv2.imshow("Face Enhancement with High Glow & Dark Red", frame)

    if cv2.waitKey(1) == 13:  # Enter to exit
        break

cap.release()
cv2.destroyAllWindows()
