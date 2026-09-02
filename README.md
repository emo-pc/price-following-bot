# 🛒 Amazon Price Tracker & Notifier Bot

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg)
![Selenium](https://img.shields.io/badge/Selenium-Scraping-43B02A.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg)

This project is an end-to-end web scraping and automation application that automatically tracks the current prices of products on Amazon. It features a user-friendly web dashboard and sends instant email notifications when a product reaches your desired target price.

---

## 🚀 Step-by-Step Installation & Execution Guide

Follow the steps below to run the application smoothly on your local machine.

### 1. Clone the Repository
First, clone the project from GitHub and navigate into the project directory:
```bash
git clone [https://github.com/YOUR_USERNAME/amazon-price-tracker.git](https://github.com/YOUR_USERNAME/amazon-price-tracker.git)
cd amazon-price-tracker
```

### 2. Set Up a Virtual Environment
To prevent library conflicts with other projects on your computer, create an isolated virtual environment (macOS / Linux):
```bash
python3 -m venv venv
source venv/bin/activate
```
*(Windows users should use `venv\Scripts\activate` to activate the environment.)*

### 3. Install Required Libraries
While your virtual environment is active (you should see `(venv)` in the terminal prompt), install all necessary dependencies:
```bash
pip install streamlit selenium webdriver-manager beautifulsoup4 pandas schedule requests
```

### 4. Email Notification Settings
To allow the bot to send you emails when a price drops, open the `check_prices.py` file and update the following variables:
```python
EMAIL_ADRESIM = "your.email@gmail.com"
EMAIL_SIFREM = "your_16_digit_app_password" 
```
> **⚠️ Security Note:** Do **not** use your personal Gmail password. Go to your Google Account settings (Security > 2-Step Verification > App Passwords), generate a specific 16-digit "App Password" for this bot, and paste it here.

---

## 💻 Usage (Dual Terminal System)

The web interface and the background checking bot run simultaneously. To run both, open **two separate terminal tabs** in your project folder and activate the virtual environment (`source venv/bin/activate`) in both.

### 1️⃣ Starting the Web Interface
In the first terminal, run the following command to launch the Streamlit dashboard:
```bash
streamlit run app.py
```
A browser window will automatically open. From there, you can add the Amazon product URL and set your target price.

### 2️⃣ Starting the Automation Bot
In the second terminal, start the background bot that monitors prices and sends emails:
```bash
python3 check_prices.py
```
As long as this terminal remains open, the system will periodically check Amazon and immediately email you when your price target is reached.

---

## ✨ Core Features

* **User-Friendly Web Panel:** A modern, minimal dashboard built with Streamlit.
* **Advanced Web Scraping:** A robust scraping engine using Selenium and BeautifulSoup to bypass standard bot protections.
* **Local Database (SQLite):** Securely stores all tracked products, URLs, and price data.
* **Scheduled Tasks:** Utilizes the `schedule` library for a completely automated loop without human intervention.

## 📂 Project Architecture

```text
📦 amazon-price-tracker
 ┣ 📜 app.py               # Main file to launch the web interface
 ┣ 📜 scraper.py           # Selenium-based web scraping engine
 ┣ 📜 database.py          # SQLite database operations
 ┣ 📜 check_prices.py      # Background bot for price checking & alerts
 ┣ 📜 tracker.db           # Database file for stored products (Auto-generated)
 ┗ 📜 README.md            # Project documentation
```
