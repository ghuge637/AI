

!pip install expert
from experta import *

# Define the Knowledge Engine
class MedicalDiagnosis(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        yield Fact(action='diagnose')
    
    @Rule(Fact(action='diagnose'),
          Fact(fever=True),
          Fact(cough=True),
          Fact(fatigue=True))
    def flu(self):
        print("✅ Diagnosis: You might have the flu.")
    
    @Rule(Fact(action='diagnose'),
          Fact(fever=True),
          Fact(sore_throat=True),
          Fact(runny_nose=True))
    def cold(self):
        print("✅ Diagnosis: You might have a common cold.")
        
    @Rule(Fact(action='diagnose'),
          Fact(nausea=True),
          Fact(diarrhea=True))
    def stomach_infection(self):
        print("✅ Diagnosis: You might have a stomach infection.")
        
    @Rule(Fact(action='diagnose'),
          Fact(headache=True),
          Fact(fever=False))
    def migraine(self):
        print("✅ Diagnosis: You might have a migraine.")
    
    @Rule(Fact(action='diagnose'),
          NOT(Fact(flu=True)),
          NOT(Fact(cold=True)),
          NOT(Fact(stomach_infection=True)),
          NOT(Fact(migraine=True)))
    def unknown(self):
        print("⚠️ Diagnosis: Unable to determine. Please consult a doctor.")

# Get user input
def get_symptom_input():
    symptoms = {
        'fever': input("Do you have a fever? (yes/no): ").lower() == 'yes',
        'cough': input("Do you have a cough? (yes/no): ").lower() == 'yes',
        'sore_throat': input("Do you have a sore throat? (yes/no): ").lower() == 'yes',
        'runny_nose': input("Do you have a runny nose? (yes/no): ").lower() == 'yes',
        'headache': input("Do you have a headache? (yes/no): ").lower() == 'yes',
        'fatigue': input("Are you experiencing fatigue? (yes/no): ").lower() == 'yes',
        'nausea': input("Do you feel nauseous? (yes/no): ").lower() == 'yes',
        'diarrhea': input("Do you have diarrhea? (yes/no): ").lower() == 'yes'
    }
    return symptoms

# Run the system
def run_expert_system():
    symptoms = get_symptom_input()
    engine = MedicalDiagnosis()
    engine.reset()
    for symptom, value in symptoms.items():
        engine.declare(Fact(**{symptom: value}))
    engine.run()

# Start the diagnosis
run_expert_system()
