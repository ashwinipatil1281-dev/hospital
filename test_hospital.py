from hospital import hospital_details

def test_hospital_details():
    expected_output = (
        "Patient ID: H101\n"
        "Patient Name: Alice\n"
        "Doctor: Dr. Smith\n"
        "Date: 10/10/2026"
    )
    assert hospital_details("H101", "Alice", "Dr. Smith", "10/10/2026") == expected_output
    print("✅ Hospital details test passed")


if __name__ == "__main__":
    try:
        # User input mode
        pId = input("Enter patient ID: ")
        pname = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter appointment date: ")

        result = hospital_details(pId, pname, doctor, date)
        print("\n--- User Output ---")
        print(result)

    except EOFError:
        # Jenkins or pytest fallback
        print("No interactive input available, running tests instead...\n")
        test_hospital_details()
        print("🎉 All tests passed!")
