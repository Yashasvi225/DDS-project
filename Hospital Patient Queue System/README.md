# 🏥 Hospital Patient Queue System

## 📌 Overview
A **command-line hospital triage** system that manages patient flow by prioritizing emergency (critical) 
patients over regular (non-urgent) ones. Designed as a Data Structures project using:

**Priority Queue → For emergency patients (higher priority first)
FIFO Queue → For regular patients (first-come, first-served)**
Wait Time Estimation → Based on queue length and average service time
Simulates real-world hospital triage logic with clear visual feedback.

---

## 🛠 Features
- Add emergency patients (highest priority)
- Add regular patients (normal queue)
- Serve the next patient (priority first)
- View all waiting patients
- Estimate wait time based on queue size
- Display triage level and arrival time
- Fully interactive menu with status updates

---

## 📂 Data Structures Used
  - **heapq** → Min-heap (priority queue)
  - **queue.Queue()** → FIFO processing
  - **Dynamic Serving Logic Priority first, then FIFO
 
---

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/your-username/hospital-patient-queue.git
cd hospital-patient-queue/src

# Run the program
python hospital_queue.py
