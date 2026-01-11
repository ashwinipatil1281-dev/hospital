def hospital_details(pId, pname, doctor, date):
    result = (
        f"Patient ID: {pId}\n"
        f"Patient Name: {pname}\n"
        f"Doctor: {doctor}\n"
        f"Date: {date}"
    )
    return result


if __name__ == "__main__":
    print(hospital_details("H101", "Alice", "Dr. Smith", "10/10/2026"))
