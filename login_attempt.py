# FAILED LOGIN ATTEMPTS ANALYSIS
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Sort and display failed login attempts in ascending order
print("Sorted failed login attempts:", sorted(failed_login_list))

# Get and display the highest failed login attempt count
highest_failed_attempts = max(failed_login_list)
print("Highest number of failed login attempts:", highest_failed_attempts, "\n")

# Define thresholds to categorize "High" and "Low" login attempts
high_threshold = 264
low_threshold = 90

# Analyze each failed login attempt and categorize as "High" or "Low"
print("Failed login attempt categorization:")
print(" ")
for attempt in failed_login_list:
    if attempt >= high_threshold:
        print(f"{attempt} - High failed login attempt")
    elif attempt <= low_threshold:
        print(f"{attempt} - Low failed login attempt")
    else:
        print(f"{attempt} - Moderate failed login attempt")


# Conditional alert if there are "High" failed login attempts
# If the highest number of failed attempts exceeds the high_threshold, an alert is displayed
if highest_failed_attempts >= high_threshold:
    print(f"\nAlert: There is one  High failed login attempt of failed login attempts, further investigation needed! [{highest_failed_attempts}]\n")
    print("\n")
else:
    # If no attempt exceeds the high threshold, a normal message is displayed
    print("\nFailed login attempts are within normal ranges.")


######################################################

# ANALYZE LOGIN ATTEMPTS FUNCTION
def analyze_logins(username, current_day_logins, average_day_logins):
    """
    Analyzes login activity and returns the ratio of current-day logins to average logins.
    
    Parameters:
        username (str): The username being analyzed.
        current_day_logins (int): Number of logins on the current day.
        average_day_logins (int): Average number of logins per day.

    Returns:
        float: The ratio of current-day logins to average logins.
    """
    
    # Display the login activity for the user
    print(f"Current day login total for {username} is {current_day_logins}")
    print(f"Average logins per day for {username} is {average_day_logins}")
    
    # Avoid division by zero (assuming all users have logged in at least once)
    if average_day_logins == 0:
        print("Error: Cannot divide by zero! Ensure users have a valid login history.")
        return None
    
    # Calculate the ratio of current day logins to average logins
    login_ratio = current_day_logins / average_day_logins
    print(f"{username} logged in {login_ratio:.2f} times as much as they do on an average day.\n")

    return login_ratio  # Return the computed ratio for further analysis

# Call the function and store the login analysis result
login_analysis = analyze_logins("ejones", 9, 3)

# Check if login activity is significantly higher than normal
if login_analysis and login_analysis >= 3:
    print("🚨 Alert! This account has more login activity than normal and it need to be investigated .\n")  # Security warning if login rate is abnormal
