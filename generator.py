def generate_test_cases(requirement):
    requirement = requirement.lower()

    test_cases = []

    if "login" in requirement:
        test_cases = [
            "Verify login with valid credentials - User logs in successfully",
            "Verify login with invalid password - Error message displayed",
            "Verify login with invalid username - Error message displayed",
            "Verify empty input fields - Validation message shown",
            "Verify account lock after multiple failed attempts - Account gets locked"
        ]

    elif "signup" in requirement:
        test_cases = [
            "Verify signup with valid details - Account created successfully",
            "Verify signup with existing email - Error message displayed",
            "Verify password strength validation - Weak password rejected",
            "Verify empty fields - Validation message shown",
            "Verify email format validation - Invalid email rejected"
        ]

    elif "payment" in requirement:
        test_cases = [
            "Verify payment with valid card - Payment successful",
            "Verify payment with invalid card - Transaction failed",
            "Verify expired card - Error message displayed",
            "Verify insufficient balance - Payment declined",
            "Verify empty payment fields - Validation message shown"
        ]

    else:
        test_cases = [
            "Verify functionality with valid input - Works as expected",
            "Verify invalid input handling - Error displayed",
            "Verify boundary values - Handled correctly",
            "Verify empty input - Validation triggered",
            "Verify system behavior under load - Stable performance"
        ]

    return "\n".join(test_cases)