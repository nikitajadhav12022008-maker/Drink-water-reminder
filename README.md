## 💧 Drink Water Reminder:

A simple Python project that reminds the user to drink water at regular time intervals using desktop notifications.
This is a beginner-friendly project created using Python and the Plyer library.

---

## 📌 Project Description:

Many people forget to drink enough water while studying or working on the computer.
This program runs in the background and sends a notification at fixed intervals to remind the user to drink water and stay hydrated.

---

## 🎯 Features:

- Sends desktop notifications at regular intervals
- Lightweight and easy to run
- Beginner-friendly Python project
- Customizable reminder time
- Works on Windows, Linux, and macOS (with supported notification systems)

---

## 🛠 Technologies Used:

- Python
- Plyer (for system notifications)
- Time module (for scheduling reminders)

---

## 📂 Project Structure:

- Drink-Water-Reminder/
- ├── water_reminder.py
- └── README.md

---

### ⚙️ Installation and Setup:

- Step 1: Install Python

Download and install Python from:
https://www.python.org/downloads/

While installing, make sure to check:

Add Python to PATH

---

- Step 2: Install Required Library

Open Command Prompt or Terminal and run:

pip install plyer

---

## ▶️ How to Run the Program:

1. Open Command Prompt or Terminal.
2. Navigate to the project folder.
3. Run the following command:
```bash
python  water_reminder.py

The program will start and send water reminder notifications at regular intervals.

---

## 🧠 How It Works:

- The program uses the plyer notification module to show desktop alerts.
- A loop keeps the program running.
- The "time.sleep()" function pauses the program for a fixed interval before sending the next reminder.

---

### ⏱ Changing the Reminder Time:

You can change the reminder interval inside the code:
interval = 3600
Examples:
    Time   | Value
15 minutes| 900
30 minutes| 1800
45 minutes| 2700
   1 hour  | 3600

---

## 🚀 Future Improvements:

- You can enhance this project by adding:
- Graphical User Interface (GUI)
- Start/Stop buttons
- Sound alert
- Daily water intake tracker
- Custom reminder intervals
- Mobile app version

---

## 👩‍💻 Author:
Nikita Jadhav
IT Student | Beginner Python Developer

----

📜 License:
This project is open-source and free to use for learning purposes....
