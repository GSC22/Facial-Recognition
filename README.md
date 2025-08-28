👁️ Facial Recognition Web App

A real-time **facial recognition and threat detection system** built with **Python, Flask, OpenCV, and DeepFace**.  
The app captures live video from a webcam, verifies detected faces against registered users stored in the `guest/` folder, and automatically saves unknown faces in the `threats/` folder for monitoring and security purposes.  

This project demonstrates the power of **AI + Web Development** by combining machine learning for face recognition with a simple web interface for accessibility.

---

## ✨ Key Features

- 🎥 **Real-time Face Detection**  
  Uses **OpenCV** to capture and process live video from the webcam.

- ✅ **Face Verification with DeepFace**  
  Matches detected faces with known images stored in the `guest/` directory.

- 🚨 **Threat Logging**  
  Automatically saves images of unrecognized faces into the `threats/` directory for later review.

- 🌐 **Web-based Interface**  
  Built with **Flask** and styled using **Tailwind CSS** for a responsive and minimal UI.

- 📂 **Organized Data Storage**  
  Separate folders for `guest` (authorized users) and `threats` (unrecognized users).

---

## 🛠️ Tech Stack

- **Python 3**  
- **Flask** – lightweight web framework for the backend  
- **DeepFace** – facial recognition and deep learning model  
- **OpenCV** – image/video processing and real-time capture  
- **HTML + Tailwind CSS** – frontend interface
