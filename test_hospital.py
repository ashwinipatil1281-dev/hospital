# test_hospital.py
from hospital import hospital_details


def test_hospital_success():
    output = hospital_details("Alice", "Dr. Smith", "10/10/2026")
    expected = (
        "Appointment booked successfully!\n"
        "Patient Name: Alice\n"
        "Doctor: Dr. Smith\n"
        "Date: 10/10/2026"
    )
    assert output == expected
    print(" Success case passed")


def test_hospital_details_failure():
    output = hospital_details("Bob", "Dr. Unknown", "12/10/2026")
    assert output == "Doctor not available"
    print("Failure case passed")


if __name__ == "__main__":
    test_hospital_details_success()
    test_hospital_failure()
    print("All tests passed!")
