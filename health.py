import hashlib
import json
import time

class HealthcareBlockchain:

    def __init__(self):
        self.records = []

    def generate_hash(self, record):
        data = json.dumps(record, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    def add_record(self, patient_id, name, age, disease):
        record = {
            "Patient ID": patient_id,
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Time": time.ctime()
        }

        record_hash = self.generate_hash(record)

        self.records.append({
            "record": record,
            "hash": record_hash
        })

        print("Healthcare Record Added Successfully!")
        print("Record Hash:", record_hash)

    def display_records(self):
        if not self.records:
            print("No Records Found!")
            return

        for item in self.records:
            print("\nPatient Details:")
            for key, value in item["record"].items():
                print(key, ":", value)

            print("Record Hash:", item["hash"])

    def verify_records(self):
        for item in self.records:
            new_hash = self.generate_hash(item["record"])

            if new_hash != item["hash"]:
                print("Record Integrity Failed!")
                return

        print("All Healthcare Records Verified!")


hospital = HealthcareBlockchain()

while True:
    print("\n--- HEALTHCARE RECORD SYSTEM ---")
    print("1. Add Patient Record")
    print("2. Display Records")
    print("3. Verify Records")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        patient_id = input("Patient ID: ")
        name = input("Patient Name: ")
        age = input("Patient Age: ")
        disease = input("Disease: ")

        hospital.add_record(
            patient_id, name, age, disease
        )

    elif choice == "2":
        hospital.display_records()

    elif choice == "3":
        hospital.verify_records()

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")
