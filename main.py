from generator import generate_test_cases
from formatter import format_output

def save_to_file(content):
    with open("test_cases.txt", "w") as f:
        f.write(content)

if __name__ == "__main__":
    requirement = input("Enter requirement: ")

    raw_output = generate_test_cases(requirement)
    formatted_output = format_output(raw_output)

    print("\nGenerated Test Cases:\n")
    print(formatted_output)

    save_to_file(formatted_output)
    print("\nTest cases saved to test_cases.txt ✅")