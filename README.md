This section is also designed for monitoring login activity and raising alerts when there is abnormal behavior, helping detect potential security risks.


Failed Login Attempts Analysis (Monitoring):
	1. Failed Attempts List: A list of failed login attempts is analyzed.
	2. Sorting: The list of failed login attempts is sorted in ascending order and displayed.
	3. Highest Failed Attempts: The script identifies and displays the highest number of failed login attempts.
	4. Categorization: Each failed attempt is categorized as "High", "Low", or "Moderate" based on predefined thresholds.
	5. Alert for High Attempts: If the highest failed login attempt exceeds a certain threshold, an alert is triggered, indicating further investigation is needed.
This section is designed for continuous monitoring of failed login attempts to detect unusual activity.

Login Attempts Analysis Function (Monitoring):
	1. Function Purpose: A function analyze_logins is created to analyze user login activity by comparing the current day's logins to the average daily logins.
	2. Inputs: The function takes the username, the number of logins for the current day, and the average logins per day.
	3. Error Handling: If the average logins per day is zero, an error message is displayed to avoid division by zero.
	4. Login Ratio Calculation: The ratio of current-day logins to average logins is calculated and displayed.
Alert for High Activity: If the login activity is significantly higher than usual (e.g., 3 times or more), an alert is triggered for investigation.![image]
