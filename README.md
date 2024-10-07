# 📇 ID Card Data Extraction App - OCR-rex

![React](https://img.shields.io/badge/frontend-React-blue) ![Flask](https://img.shields.io/badge/backend-Flask-red) ![License](https://img.shields.io/badge/license-MIT-green)

This web application enables users to upload an image of an ID card and extract personal data like name, address, date of birth, and ID card number using Optical Character Recognition (OCR) technologies. The app leverages **React** for the frontend and **Flask** for the backend.

---

## 🚀 Features

- **ID Card Upload:** Users can upload images of ID cards for processing.
- **OCR Data Extraction:** Extracts personal details such as:
  - Full Name
  - Address
  - Date of Birth
  - ID Number
- **Tech Stack:**
  - Frontend: **React**
  - Backend: **Flask**
  - OCR: **PaddlePaddle**
  - Database: **SQLite** (configurable)

---

## 📸 Screenshots

Here’s what the app looks like:

![App Screenshot](/screenshot.png)

---

## 🛠 Technologies

| **Frontend** | **Backend** | **OCR**        | **Database** |
|--------------|-------------|----------------|--------------|
| React        | Flask       | PaddlePaddle   | SQLite       |
| HTML5/CSS3   | Python      | | MySQL (opt)  |
| JavaScript   | REST API    | | PostgreSQL (opt)|

---

## 📋 Requirements

To run this project, you need:

- **Python 3.8+** (for Flask)
- **Node.js** (for React)
- **pipenv** or **pip** for package management
- **OCR Engines** (PaddlePaddle)
  
Check `requirements.txt` for Python dependencies.

---

## ⚙️ Installation

### Backend (Flask)

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nahlibee/OCR-rex.git
    cd OCR-rex/backend
    ```

2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask server:**
    ```bash
    python main.py
    ```
   The server will be available at `http://localhost:5000`.

### Frontend (React)

1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```

2. **Install the dependencies:**
    ```bash
    npm install
    ```

3. **Run the React development server:**
    ```bash
    npm run dev
    ```
   Access the frontend at the given port.

---
## 📖 Usage

### Launch the Application:

1. Open the frontend at the given port.
2. The backend will run at `http://localhost:5000`.

### Upload an ID Card:

- Select an ID card front and back image.
- Click "Upload" to send the image for processing.

### View Extracted Data:

- The app will display the extracted data (name, address, date of birth, ID number).