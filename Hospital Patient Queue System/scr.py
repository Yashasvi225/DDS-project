# hospital_queue.py
# Hospital Patient Queue System with Priority Queue and FIFO Queue

import heapq
import queue
import datetime


# -----------------------------
# 🏥 Main Hospital Queue System
# -----------------------------

class HospitalQueue:
    def __init__(self, avg_service_time=10):
        # Priority queue: (priority, timestamp, patient_name)
        # Emergency = priority 1, Regular = priority 2
        self.priority_queue = []  # Emergency patients (min-heap)
        self.regular_queue = queue.Queue()  # Regular patients (FIFO)
        self.avg_service_time = avg_service_time  # in minutes
        print("🏥 Welcome to the Hospital Patient Queue System!")

    def _get_timestamp(self):
        """Helper: Get current time as string."""
        return datetime.datetime.now().strftime("%H:%M")

    # -----------------------------
    # 1. Add Emergency Patient
    # -----------------------------
    def add_emergency_patient(self):
        name = input("\nEnter emergency patient name: ").strip()
        if not name:
            print("⚠️  Name cannot be empty.")
            return

        timestamp = self._get_timestamp()
        # Priority 1 = Emergency (higher priority)
        heapq.heappush(self.priority_queue, (1, timestamp, name))
        print(f"🚑 ✅ '{name}' added as **emergency** patient at {timestamp}.")

    # -----------------------------
    # 2. Add Regular Patient
    # -----------------------------
    def add_regular_patient(self):
        name = input("\nEnter regular patient name: ").strip()
        if not name:
            print("⚠️  Name cannot be empty.")
            return

        self.regular_queue.put(name)
        timestamp = self._get_timestamp()
        print(f"👤 ✅ '{name}' added to regular queue at {timestamp}.")

    # -----------------------------
    # 3. Serve Next Patient
    # -----------------------------
    def serve_patient(self):
        if not self.priority_queue and self.regular_queue.empty():
            print("\n🟢 No patients waiting.")
            return

        # Serve emergency patients first
        if self.priority_queue:
            priority, timestamp, name = heapq.heappop(self.priority_queue)
            print(f"\n🩺 Serving **EMERGENCY** patient: {name} (arrived at {timestamp})")
        else:
            name = self.regular_queue.get()
            timestamp = self._get_timestamp()
            print(f"\n🩺 Serving regular patient: {name}")

    # -----------------------------
    # 4. View Waiting Patients
    # -----------------------------
    def view_patients(self):
        print("\n" + "="*60)
        print("📋 CURRENTLY WAITING PATIENTS")
        print("="*60)

        # Show emergency patients
        if self.priority_queue:
            print("🚨 EMERGENCY PATIENTS (Priority):")
            # Heap doesn't support traversal, so we copy
            temp_heap = self.priority_queue[:]
            idx = 1
            while temp_heap:
                priority, timestamp, name = heapq.heappop(temp_heap)
                print(f"  {idx}. {name} [Arrived: {timestamp}]")
                idx += 1
        else:
            print("🟢 No emergency patients waiting.")

        # Show regular patients
        if not self.regular_queue.empty():
            print("\n🚶‍♂️ REGULAR PATIENTS (FIFO):")
            temp_list = []
            idx = 1
            while not self.regular_queue.empty():
                name = self.regular_queue.get()
                print(f"  {idx}. {name}")
                temp_list.append(name)
                idx += 1
            # Restore queue
            for name in temp_list:
                self.regular_queue.put(name)
        else:
            print("🟢 No regular patients waiting.")

        print("="*60)

    # -----------------------------
    # 5. Estimate Wait Time
    # -----------------------------
    def estimate_wait_time(self):
        emergency_count = len(self.priority_queue)
        regular_count = self.regular_queue.qsize()

        print("\n" + "-"*50)
        print("⏳ ESTIMATED WAIT TIME")
        print("-"*50)

        if emergency_count > 0:
            print(f"🚨 {emergency_count} emergency patient(s) ahead — you will be delayed.")
        
        # Only regular patients after emergencies
        my_position = regular_count + 1
        wait_time = my_position * self.avg_service_time
        print(f"👤 As a regular patient, estimated wait: ~{wait_time} minutes")
        print(f"   (Based on {regular_count} ahead + avg {self.avg_service_time} min per patient)")
        print("-"*50)

    # -----------------------------
    # Interactive Menu
    # -----------------------------
    def menu(self):
        while True:
            print("\n" + "═" * 50)
            print("🏥 HOSPITAL PATIENT QUEUE SYSTEM")
            print("═" * 50)
            print("1. 🚑 Add Emergency Patient")
            print("2. 👤 Add Regular Patient")
            print("3. 🩺 Serve Next Patient")
            print("4. 👀 View Waiting Patients")
            print("5. ⏳ Estimate Wait Time for New Regular Patient")
            print("6. 🚪 Exit")

            choice = input("\n👉 Choose an option (1-6): ").strip()

            if choice == '1':
                self.add_emergency_patient()
            elif choice == '2':
                self.add_regular_patient()
            elif choice == '3':
                self.serve_patient()
            elif choice == '4':
                self.view_patients()
            elif choice == '5':
                self.estimate_wait_time()
            elif choice == '6':
                print("👋 Thank you! The hospital queue system is now closed.")
                break
            else:
                print("❌ Invalid choice. Please select 1–6.")


# -----------------------------
# 🚀 Run the Program
# -----------------------------

if __name__ == "__main__":
    hospital = HospitalQueue(avg_service_time=10)  # 10 min per patient
    hospital.menu()
