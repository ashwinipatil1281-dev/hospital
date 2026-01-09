from hospital import hospital


def test_hospital_success():
    output = hospital("Alice", "Dr. Smith", "10/10/2026")
    assert output == (
        "Appointment booked successfully!\n"
        "Patient Name: Alice\n"
        "Doctor: Dr. Smith\n"
        "Date: 10/10/2026"
    )


def test_hospital_failure():
    output = hospital("Bob", "Dr. Unknown", "12/10/2026")
    assert output == "Doctor not available"
