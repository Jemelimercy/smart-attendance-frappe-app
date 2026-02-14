# 🏢 Warehouse AI Attendance & Monitoring System
### *Integrating Computer Vision with Enterprise ERP via Frappe Framework*

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Frappe Framework](https://img.shields.io/badge/Framework-Frappe-orange?logo=frappe&logoColor=white)](https://frappeframework.com/)
[![MediaPipe](https://img.shields.io/badge/AI-MediaPipe-00C7B7?logo=google&logoColor=white)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/Vision-OpenCV-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)

## 📝 Project Overview
This project is a real-time attendance and security monitoring system designed for warehouse environments. It bridges the gap between high-speed **Computer Vision (AI)** and structured **Enterprise Resource Planning (ERP)** data management. 

The system uses a camera feed to detect employees, calculates a confidence score, and instantly pushes a log to a custom **Frappe DocType** via REST API, providing an automated, paperless audit trail.

## ⚙️ Technical Stack
* **Language**: Python 3.11
* **Computer Vision**: MediaPipe (Face Detection) & OpenCV
* **Backend**: Frappe Framework (MariaDB)
* **Authentication**: Token-based API Keys via `.env`

## 🚀 Key Features
* **Real-time Logging**: Automatically creates `Warehouse Attendance` records with zero manual entry.
* **Intelligent Dashboards**: Includes "Detections Today" number cards and "Employee Breakdown" pie charts.
* **Professional Naming**: Implements custom naming logic (`AI-LOG-{#####}`) for enterprise-grade record keeping.
* **Data Integrity**: Uses server-side Datetime filtering for accurate "Today" activity reporting.

## 🏗️ System Architecture
1. **Edge Device**: Python 3.11 script captures video frames via OpenCV.
2. **AI Processing**: MediaPipe identifies faces and generates confidence scores.
3. **API Bridge**: Script sends a POST request with `employee_name`, `confidence`, and `time`.
4. **Cloud ERP**: Frappe validates the token, stores the log, and updates the Dashboard.



## 🛠️ Setup & Installation

### 1. Frappe Setup
* Create a DocType named `Warehouse Attendance`.
* Add fields: `employee_name` (Data), `confidence` (Float), and `time` (Datetime).
* Set Naming Rule to **Expression**: `format:AI-LOG-{#####}`.

### 2. Python Client Setup
```bash
git clone [https://github.com/](https://github.com/)[YourUsername]/warehouse-ai-attendance.git
cd warehouse-ai-attendance
pip install -r requirements.txt

### 3.Environment Configuration
Create a .env file to store your credentials:
Code snippet
API_KEY=your_frappe_api_key
API_SECRET=your_frappe_api_secret
SITE_URL=http://your-site-url

📊 Dashboard Preview
The system populates a visual dashboard where managers can track:

Total Detections: High-level throughput metrics.

Employee Bar Chart: Breakdown of presence by individual.

Activity Heatmap: Peak detection times throughout the day.