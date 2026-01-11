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
