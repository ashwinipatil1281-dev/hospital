def hospital_details(patient, doctor, date):
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


if __name__ == "__main__":
    try:
        patient = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter appointment date: ")

        result = hospital(patient, doctor, date)
        print(result)
    except EOFError:
        # This prevents Jenkins/pytest from crashing when no input is available
        print("Interactive input not available in this environment.")
