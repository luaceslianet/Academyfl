
import re
 
def extract_patient_info(text):
    # Define regex patterns to extract relevant data
    patterns = {
        'patient_name': r'Patient:\s+(.*)',
        'patient_id': r'Patient ID:\s+(\d+)',
        'admission_date': r'Admission Date:\s+(\d{4}-\d{2}-\d{2})',
        'discharge_date': r'Discharge Date:\s+(\d{4}-\d{2}-\d{2})',
        'diagnosis': r'Diagnosis:\s+(.*)'
    }
   
    extracted_data = {}
   
    # Iterate over each pattern and extract corresponding data
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_data[key] = match.group(1)
   
    return extracted_data
 
# Example text string
sample_text = """
Patient: John Doe
Patient ID: 12345
Admission Date: 2024-05-01
Discharge Date: 2024-05-10
Diagnosis: Hypertension
"""
 
# Extract information using the defined function
extracted_info = extract_patient_info(sample_text)
 
# Print extracted data
print("Extracted Patient Information:")
for key, value in extracted_info.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
 