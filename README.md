# Application
This is a normal Python file that takes json config file.
JSON Parser
Overview
The JSON Parser is a Python application that reads, updates, and saves settings in a JSON configuration file. It ensures the JSON structure is valid before saving changes.

Clone the repository:
No additional libraries needed—just Python's built-in libraries.

Usage
Create a JSON configuration file: (e.g., config.json)

json
Copy code
{
    "setting1": "value1",
    "setting2": 2,
    "setting3": {
        "subsetting1": "subvalue1"
    }
}
Run the application:

bash
Copy code
python json_parser.py
Follow the prompts to update settings.

Operations
1. Load Configuration
The application reads the configuration from the specified JSON file.
2. Display Current Settings
Displays the current configuration in a readable format.
3. Update Setting
Prompts the user to specify which setting to update using dot notation (e.g., setting3.subsetting1).
Accepts new values for the specified setting.
4. Save Configuration
Validates the updated configuration and saves it back to the JSON file.
Example Output
When you run the application, you will see output like this:

sql
Copy code
Current configuration:
{
    "setting1": "value1",
    "setting2": 2,
    "setting3": {
        "subsetting1": "subvalue1"
    }
}

Enter the setting to update (e.g., setting3.subsetting1): setting3.subsetting1
Enter the new value: updated_value
Configuration saved successfully.
After updating, the config.json will look like this:

json
Copy code
{
    "setting1": "value1",
    "setting2": 2,
    "setting3": {
        "subsetting1": "updated_value"
    }
}
Error Handling
If there’s an issue (like a missing file or invalid JSON), the application will display an error message:

go
Copy code
An error occurred: Configuration file 'config.json' not found.
Contributing
Feel free to contribute! Open an issue or submit a pull request.
