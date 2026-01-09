def hospital(patient, doctor, date):
    doctors = ["Dr. Smith", "Dr. John", "Dr. Emily"]

    if doctor in doctors:
        return (
            "Appointment booked successfully!\n"
            "Patient Name: " + patient + "\n"
            "Doctor: " + doctor + "\n"
            "Date: " + date
        )
    else:
        return "Doctor not available"


# Run program normally
if __name__ == "__main__":
    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date: ")

    result = hospital(patient, doctor, date)
    print(result)
