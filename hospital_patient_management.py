def search_by_disease(patients, search_disease):
    matching_patients = [patient["Name"] for patient in patients if patient["Disease"] == search_disease]
    return matching_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = input("Enter the disease to search: ")
result = search_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {result}")
