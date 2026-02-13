# 🔐 Password Manager

## <img width="455" height="426" alt="image" src="https://github.com/user-attachments/assets/c1ef1dee-463b-413f-bd9a-ec1bfcfa4940" />


A robust desktop application designed to generate, manage, and store account credentials locally. This project focuses on UI layout precision using the Tkinter grid system and implements cross-platform clipboard integration for a seamless user experience.

## 🕹️ How It Works
The application serves as a centralized hub for managing digital credentials:
* **Credential Entry**: Users input website names and usernames/emails into a structured form.
* **Password Generation**: A specialized algorithm creates randomized, high-entropy strings.
* **Validation & Confirmation**: The system validates inputs to ensure no empty fields are saved and provides a verification popup before final storage.
* **Local Storage**: Data is appended to a local `passwords.txt` file for persistent access.

## ✨ Key Features
* **Automated Password Engine**: Generates secure passwords by shuffling a randomized mix of letters, numbers, and symbols.
* **Integrated Clipboard Support**: Utilizes the `pyperclip` library to automatically copy generated passwords to the user's clipboard for immediate use.
* **Grid-Based UI Design**: Implements a clean, multi-column layout with fixed-width entry fields and column-spanning buttons for a professional aesthetic.
* **Input Validation**: Features multiline conditional logic to prevent the storage of incomplete or empty data entries.
* **Event-Driven Popups**: Uses the `messagebox` module to provide real-time feedback and user confirmations.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **Library**: Tkinter (Standard GUI Library)
* **Packages**: `pyperclip` (Clipboard management)
* **Logic**: Procedural event handling and file I/O operations.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* `pyperclip` package: `pip install pyperclip`
* `logo.png` asset file in the project directory.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abatima/password-manager.git

```

2. Navigate to the directory:
```bash
cd password-manager

```


3. Run the application:
```bash
python main.py

```



## 🎮 Controls

* **Generate Button**: Creates a new secure password and copies it to the clipboard.
* **Add Button**: Validates inputs, asks for confirmation, and saves the credentials to `passwords.txt`.

---

*Developed by [abatima](https://github.com/abatima)

```
