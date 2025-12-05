Real-Time Face Enhancement Filter (Python + OpenCV)

This project enhances the face in real-time during webcam streaming using Python and OpenCV.
It applies a natural-looking beauty filter similar to those used in video calling apps (Google Meet, Zoom, Instagram filters, etc.).

  Features

 Real-time face detection (Haar Cascade)

 High-level skin smoothing (bilateral filter)

 Very high glow effect for bright skin

 Brightness & contrast enhancement

 Dark red tint effect (light makeup / lips enhancement)

 Full face coverage (pads used for better detection area)

 Fast processing (30 FPS depending on system)

 How It Works

Webcam stream run hota hai

Haar cascade face detector se face locate hota hai

Face region ko extract karke enhance kiya jata hai using:

Bilateral smoothing

Gaussian glow

Brightness boost

Red tint overlay

Enhanced face dubara frame me place kar diya jata hai

Final output real-time display hota hai

🛠️ Tech Stack

Python 3.8+

OpenCV

NumPy

Haar Cascade Classifier (frontal face detection)

 Installation
pip install opencv-python
pip install numpy




▶ Run the Project
python Blur.py

 Output Preview

Real-time smooth skin

Brightened & enhanced face

Dark-red lip / tint effect

Better & clean video call appearance

 Project Structure
Face-Enhancement-Filter/
│-- Blur.py
│-- README.md
│-- haarcascade_frontalface_default.xml (auto from cv2)

 Use Cases

Video calls (Google Meet / Zoom)

Live streaming appearance enhancement

Interview video quality improvement

Face beautification filters for apps

 Contribution

Pull requests are welcome.
For major changes, please open an issue first.

 License

This project is for educational and internship demonstration purposes.



 Demo Video
Click the link below to watch the live demonstration of the project:

[Watch Project Demo]( Demo Video
Click the link below to watch the live demonstration of the project:

  [Watch Project Demo]https://1drv.ms/v/c/EBB02A64894EEB74/Ea2s9i_aAZdJi2ZlZq9fB1ABCbdy9oHkk8nBbIcEqvESZg?e=hMaSfo