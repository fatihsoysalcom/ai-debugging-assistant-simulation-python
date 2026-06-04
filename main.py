import traceback

def process_user_data(user_id, name, age_str):
    """
    Simulates a function that processes user data.
    Can raise errors due to invalid input.
    """
    try:
        if not name:
            raise ValueError("Name cannot be empty.")
        
        # Attempt to convert age_str to int, potential ValueError
        age = int(age_str)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
            
        print(f"User {user_id}: {name}, Age: {age} processed successfully.")
        return {"user_id": user_id, "name": name, "age": age}
    except ValueError as e:
        # Re-raise to be caught by the main loop for AI analysis
        raise ValueError(f"Data validation error for user {user_id}: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred for user {user_id}: {e}")

def ai_debugger_assistant(error_message, stack_trace):
    """
    Simulates an AI assistant analyzing an error message and stack trace
    to provide debugging suggestions based on simple rules.
    """
    suggestions = []

    # --- AI-like analysis based on error message patterns ---
    if "ValueError: invalid literal for int()" in error_message or "ValueError: could not convert string to int" in error_message:
        suggestions.append("AI Suggestion: The 'age' field likely contains non-numeric characters. Check input validation for age.")
        suggestions.append("AI Action: Verify the `age_str` parameter before calling `int()`. Consider using `str.isdigit()` or a more robust parsing method.")
    elif "ValueError: Name cannot be empty" in error_message:
        suggestions.append("AI Suggestion: The 'name' field is empty. Ensure name input is not blank.")
        suggestions.append("AI Action: Add a check for empty name strings at the input stage.")
    elif "ValueError: Age must be between 0 and 120" in error_message:
        suggestions.append("AI Suggestion: The 'age' value is out of the expected range (0-120).")
        suggestions.append("AI Action: Implement stricter range validation for the 'age' field.")
    elif "ZeroDivisionError" in error_message:
        suggestions.append("AI Suggestion: A division by zero error occurred. Check denominators before division.")
        suggestions.append("AI Action: Add a conditional check to prevent division by zero.")
    elif "KeyError" in error_message:
        suggestions.append("AI Suggestion: A dictionary key was not found. Verify dictionary keys or use `.get()` with a default value.")
        suggestions.append("AI Action: Inspect the dictionary access point in the stack trace.")
    else:
        suggestions.append("AI Suggestion: This seems like a general error. Review the full stack trace for context.")
        suggestions.append("AI Action: Consider logging more context variables around the error point.")

    # --- AI-like analysis based on stack trace context (simplified) ---
    if "process_user_data" in stack_trace:
        suggestions.append("AI Context: The error originated within the `process_user_data` function.")
    
    if not suggestions:
        return "AI Assistant: No specific suggestions, but the error message is: " + error_message.splitlines()[0]
    
    return "\n".join(suggestions)

def main():
    user_data_list = [
        (1, "Alice", "30"),
        (2, "Bob", "twenty-five"), # Intentional bug: non-numeric age
        (3, "Charlie", "150"),     # Intentional bug: age out of range
        (4, "", "45"),             # Intentional bug: empty name
        (5, "David", "28")
    ]

    print("--- Simulating AI-Powered Debugging Workflow ---")
    print("Processing user data and using AI to assist with errors.\n")

    for user_id, name, age_str in user_data_list:
        print(f"Attempting to process user {user_id} (Name: '{name}', Age: '{age_str}')...")
        try:
            process_user_data(user_id, name, age_str)
        except Exception as e:
            error_message = str(e)
            full_stack_trace = traceback.format_exc() # Capture the full stack trace

            print(f"ERROR detected for user {user_id}: {error_message}")
            print("\n--- AI Debugging Assistant Analysis ---")
            # This is the core of the AI-powered debugging simulation:
            # The 'AI' analyzes the error and stack trace to provide insights.
            ai_suggestion = ai_debugger_assistant(error_message, full_stack_trace)
            print(ai_suggestion)
            print("---------------------------------------\n")
        print("-" * 30)
    print("\n--- Simulation Complete ---")

if __name__ == "__main__":
    main()
