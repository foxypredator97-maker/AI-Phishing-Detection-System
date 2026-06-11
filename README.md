# 🛡️ AI-Powered Phishing Detection & Website Trust Analyzer

## Live Demo

https://ai-phishing-detection-system-q7aa.onrender.com
An AI-powered cybersecurity web application that detects potentially malicious websites by analyzing URL characteristics using Machine Learning and cybersecurity heuristics.

## 🚀 Project Overview

Phishing attacks are one of the most common cyber threats used to steal user credentials, financial information, and personal data.

This project uses:

* Machine Learning (Random Forest Classifier)
* URL Feature Engineering
* Trust Score Analysis
* Risk Level Assessment
* Flask Web Framework

to determine whether a website is potentially legitimate or suspicious.

---

## 🎯 Features

✅ AI-Based Phishing Detection

✅ URL Feature Extraction

✅ Trust Score Calculation (0-100)

✅ Risk Level Classification

✅ Interactive Cybersecurity Dashboard

✅ Real-Time URL Analysis

✅ Flask-Based Web Application

✅ Bootstrap 5 User Interface

---

## 🧠 Machine Learning Model

### Algorithm Used

* Random Forest Classifier

### Model Performance

* Accuracy: **91.57%**

### Training Pipeline

Dataset → Feature Engineering → Model Training → Prediction Engine

---

## 🔍 URL Features Analyzed

The system evaluates multiple URL characteristics including:

| Feature             | Description                                  |
| ------------------- | -------------------------------------------- |
| URL Length          | Length of URL                                |
| HTTPS Usage         | Checks secure protocol                       |
| Dot Count           | Number of dots in URL                        |
| Hyphen Count        | Number of hyphens                            |
| Suspicious Keywords | login, verify, secure, bank, account, update |
| @ Symbol Detection  | Presence of @ symbol                         |
| Path Length         | URL path complexity                          |
| Domain Structure    | URL validity analysis                        |

---

## 📊 Risk Assessment

The application assigns a Trust Score and Risk Level:

### Trust Score

* 85 – 100 → Safe
* 60 – 84 → Suspicious
* Below 60 → Phishing Risk

### Risk Levels

🟢 LOW

🟡 MEDIUM

🔴 HIGH

---

## 🖥️ Dashboard Preview

### Features Displayed

* URL Analysis
* AI Prediction
* Trust Score
* Risk Level
* Final Security Verdict
* Security Assessment Summary

---

## 🏗️ Project Structure

```text
AI-Phishing-Detection-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── dataset/
│   └── phishing_url_dataset.csv
│
├── model/
│   └── phishing_model.pkl
│
├── static/
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── feature_extractor.py
│   ├── trust_score.py
│   └── url_checker.py
│
├── train_model.py
├── predict.py
└── predict_url.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Phishing-Detection-System.git
cd AI-Phishing-Detection-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🌐 Access Application

Open:

```text
http://127.0.0.1:5000
```

---

## 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Backend

* Flask

### Frontend

* HTML
* CSS
* Bootstrap 5

### Version Control

* Git
* GitHub

---

## 🔒 Cybersecurity Concepts Used

* Phishing Detection
* URL Analysis
* Threat Classification
* Risk Assessment
* Feature Engineering
* Security Heuristics

---

## 📈 Future Improvements

* WHOIS Domain Age Analysis
* VirusTotal Integration
* Google Safe Browsing API
* SSL Certificate Validation
* Website Screenshot Analysis
* Deep Learning Models
* Browser Extension Version

---

## 👨‍💻 Author

**Anshul Garg**

B.Tech CSE (Cyber Security)

DIT University

Founder – SHAGAA FASHION

---

## ⭐ Project Goal

The objective of this project is to demonstrate the practical application of Machine Learning and Cybersecurity concepts for detecting phishing websites and helping users assess website trustworthiness before visiting potentially malicious links.
