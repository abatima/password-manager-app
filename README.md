# 🔐 Password Manager

## <img width="454" height="428" alt="image" src="https://github.com/user-attachments/assets/baf7d1f0-0d13-41e1-9dea-47070e003110" />


A desktop security utility designed to generate, store, and retrieve account credentials. This version upgrades the storage engine to **JSON**, enabling structured data management and an efficient search feature for localized credential lookups.

## 🕹️ How It Works
The application manages a digital vault using a dictionary-style data structure:
* **Credential Entry**: Securely input website, email, and password details.
* **Smart Generation**: Create high-entropy passwords that are automatically copied to the clipboard.
* **Persistent Storage**: Saves data in a structured `passwords.json` format, allowing for better data integrity.
* **Instant Search**: Look up any previously saved website to retrieve associated emails and passwords via a dedicated interface.

## ✨ Key Features
* **JSON Data Management**: Implements the `json` library to read, update, and write user data, replacing standard flat-file storage for better scalability.
* **Error-Resistant Logic**: Uses `try-except-else` blocks to handle missing files or non-existent entries gracefully without crashing the UI.
* **Integrated Search Engine**: A dedicated search algorithm that fetches data by key (Website name) and displays it via interactive popups.
* **Automatic Clipboard Integration**: Leverages `pyperclip` to ensure generated passwords are ready for immediate use.
* **Enhanced UI Layout**: A refined Tkinter grid system with `columnspan` and `sticky` attributes to ensure a tight, professional user interface.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **GUI Framework**: Tkinter
* **Data Format**: JSON (JavaScript Object Notation)
* **Packages**: `pyperclip`, `json`, `random`

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* `pyperclip` package: `pip install pyperclip`
* `logo.png` image asset.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/abatima/password-manager.git](https://github.com/abatima/password-manager.git)

```

2. Navigate to the project folder:
```bash
cd password-manager

```


3. Run the application:
```bash
python main.py

```



## 🎮 Controls

* **Search**: Retrieves and displays saved details for a specific website.
* **Generate**: Creates a randomized password and copies it to the clipboard.
* **Add**: Validates input and updates the `passwords.json` vault.

---

*Developed by [abatima](https://github.com/abatima)

```
