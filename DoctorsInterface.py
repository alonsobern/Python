
import numpy as np
import pandas as pd
import os
from datetime import datetime
from Data.patient_data import patients
from prettytable import PrettyTable

def getPatientData(user_input):
    if user_input in patients:
        return patients.get(user_input)
    raise KeyError("Patient was not found!")

def getCount(patient, flag):
    number = len(patient.get(flag))
    return number

def getDetails(patient, flag):
    result = ""
    for detail in patient.get(flag):
        result = detail+"\n"+result
    return result

def getPatientBloodPressure(patient):
    result = ""
    bloodPressure = patient.get('blood_pressure_checks')
    bloodPressureDF = pd.DataFrame(bloodPressure, columns=['Systolic', 'Diastolic'])
    meanSystolic = np.mean(bloodPressureDF['Systolic'])
    meanDiastolic = np.mean(bloodPressureDF['Diastolic'])

    if meanSystolic > 125 and meanDiastolic > 85:
        result = "High\nSystolic > 125\nDiastolic > 85"
    elif (meanSystolic >= 115 and meanSystolic <= 125) and (meanDiastolic >= 75 and meanDiastolic <= 85):
        result = "Normal\n115 <= Systolic <= 125\n85 <= Diastolic<= 75"
    else:
        result = "Low"+"\nSystolic < 115\nnDiastolic < 75"
    
    return result

def getUpcomingAppointment(patient):
    if patient.get('next_appointment_date') != "No-Date":
        lastCheckup = datetime.strptime(patient.get('last_checkup_date'), "%Y-%m-%d")
        nextAppointment = datetime.strptime(patient.get('next_appointment_date'), "%Y-%m-%d")
        return str((nextAppointment - lastCheckup).days)+" days"
    else:
        return "Patient does not have an appointment\nArrange one for the next availables days"

def addMedication(patient, newMedication):
    tempNewMedication = list()
    if newMedication in patient['allergies']:
        return "\nThe patient is allergic to that medication. Please check the records."
    elif newMedication in patient['medications']:
        return "\nThe patient already has the medication in their records."
    else:
        for value in patient['medications']:
            tempNewMedication.append(value)
        tempNewMedication.append(newMedication)
        patient.update({'medications':tempNewMedication})
        return "\nThe new medication was added to their records."

def removeMedication(patient, medication):
    tempNewMedication = list()
    if medication in patient['medications']:
        for value in patient['medications']:
            tempNewMedication.append(value)
        tempNewMedication.remove(medication)
        patient.update({'medications':tempNewMedication})
        return "\nThe medication was removed from their records."
    else:
        return "The medication was not found! Please check the records."

def patientFormatTable(patientName, patientAge, patientGender, patientDiagnosis, 
                       patientNumberMedication=None, patientMedication=None, patientNumberAllergies=None, patientAllergies=None, 
                       patientBloodPressure=None, patientUpcomingAppointment=None, flag=None):
    
    general_information = ["Name", "Age", "Gender", "Diagnosis"]
    appointments = ["Upcoming Appointment"]
    blood_pressure = ["Blood Pressure"]
    medication = ["Number of Medication", "Medication"]
    allergies = ["Number of Allergies", "Allergies"]

    table = PrettyTable()
    if flag == 1:
        table.field_names = (general_information)
        table.add_row([patientName, patientAge, patientGender, patientDiagnosis])
    elif flag == 2:
        table.field_names = (general_information + appointments)
        table.add_row([patientName, patientAge, patientGender, patientDiagnosis, patientUpcomingAppointment])
    elif flag == 3:
        table.field_names = (general_information + blood_pressure)
        table.add_row([patientName, patientAge, patientGender, patientDiagnosis, patientBloodPressure])
    elif flag == 4:
        table.field_names = (general_information + medication)
        table.add_row([patientName, patientAge, patientGender, patientDiagnosis, patientNumberMedication, patientMedication])
    elif flag == 5:
        table.field_names = (general_information + allergies)
        table.add_row([patientName, patientAge, patientGender, patientDiagnosis, patientNumberAllergies, patientAllergies])
    return table

print("\nDoctors Interface\n")
global user_input 
user_input = input("Enter the Patient ID: ").upper()

try:
    menu = list()
    menu.append("1. Check General Information")
    menu.append("2. Check Appointments")
    menu.append("3. Check Blood Pressure")
    menu.append("4. Check Medication")
    menu.append("5. Check Allergies")
    menu.append("6. Add Medication")
    menu.append("7. Remove Medication")
    menu.append("8. Change the patient")
    menu.append("9. Exit")

    while True:

        for entry in range(len(menu)):
            print (menu[entry])

        patient = getPatientData(user_input)
        patientName = patient.get('name')
        patientAge = patient.get('age')
        patientGender = patient.get('gender')
        patientDiagnosis = patient.get('diagnosis')

        selection=int(input("Please Select: "))

        if selection == 1: 

            print("\nGeneral Information\n")
            print(patientFormatTable(patientName,patientAge,
                             patientGender,patientDiagnosis, flag=1))
            
        elif selection == 2:

            patientUpcomingAppointment = getUpcomingAppointment(patient)
            print("\nAppointments\n")
            print(patientFormatTable(patientName,patientAge,
                             patientGender,patientDiagnosis, patientUpcomingAppointment=patientUpcomingAppointment, flag=2))
            
        elif selection == 3:

            patientBloodPressure = getPatientBloodPressure(patient)
            print(patientFormatTable(patientName,patientAge,
                             patientGender,patientDiagnosis, patientBloodPressure=patientBloodPressure, flag=3))
            
        elif selection == 4:

            patientNumberMedication = getCount(patient, "medications")
            patientMedication = getDetails(patient, "medications")
            print("\nMedications\n")
            print(patientFormatTable(patientName,patientAge,
                             patientGender,patientDiagnosis, patientNumberMedication=patientNumberMedication, patientMedication=patientMedication, flag=4))
            
        elif selection == 5:

            patientNumberAllergies = getCount(patient, "allergies")
            patientAllergies = getDetails(patient, "allergies")
            print("\nAllergies\n")
            print(patientFormatTable(patientName,patientAge,
                             patientGender,patientDiagnosis, patientNumberAllergies=patientNumberAllergies, patientAllergies=patientAllergies, flag=5))
            
        elif selection == 6:

            flag = True
            answer = input("Do you want to add a medication?\nPress (Y) to proceed or (C) to cancel the action: ").upper()
            while flag:
                if answer[0] == "Y":
                    answerMedication = input("Register the new medication: ").capitalize()
                    print(addMedication(patient, answerMedication))
                    patientNumberMedication = getCount(patient, "medications")
                    patientMedication = getDetails(patient, "medications")
                    print("\nMedications\n")
                    print(patientFormatTable(patientName,patientAge,
                                patientGender,patientDiagnosis, patientNumberMedication=patientNumberMedication, patientMedication=patientMedication, flag=4))
                    flag = False
                elif answer[0] == "C":
                    print("\n")
                    flag = False
                else:
                    answer = input("Do you want to add a medication?\nPress (Y) to proceed or (C) to cancel and return to the menu: ").upper()

        elif selection == 7:

            flag = True
            answer = input("Do you want to remove a medication?.\nPress (Y) to proceed or (C) to cancel the action: ").upper()
            while flag:
                if answer[0] == "Y":
                    answerMedication = input("Enter the medication: ").capitalize()
                    print(removeMedication(patient, answerMedication))
                    patientNumberMedication = getCount(patient, "medications")
                    patientMedication = getDetails(patient, "medications")
                    print(patientFormatTable(patientName,patientAge,
                                patientGender,patientDiagnosis, patientNumberMedication=patientNumberMedication, patientMedication=patientMedication, flag=4))
                    flag = False
                elif answer[0] == "C":
                    print("\n")
                    flag = False
                else:
                    answer = input("Do you want to remove a medication?.\nPress (Y) to proceed or (C) to cancel the action: ").upper()
        
        elif selection == 8:
            os.system('cls')
            user_input = input("Enter the Patient ID: ").upper()
            print("\n")

        elif selection == 9:
            break

        else: 
            print ("Unknown Option Selected!")
        
        if selection != 8:
            backMenu = input("Return to the menu (M) or Exit (E): ").upper()
            flag = True
            while flag:
                if backMenu[0] == "M":
                    flag = False
                    os.system('cls')
                elif backMenu[0] == "E":
                    exit(True)
                else:
                    backMenu = input("Return to the menu (M) or Exit (E): ").upper()

except Exception as err:
    print("Handling Errors:", err)