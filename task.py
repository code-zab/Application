import json
import os

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

def save_config(file_path, config):
    try:
        json_string = json.dumps(config, indent=4)
        json.loads(json_string) 
        
        with open(file_path, 'w') as file:
            file.write(json_string)
        print("Configuration saved successfully.")
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error saving configuration: {e}")

def update_setting(config, path, value):
    keys = path.split('.')
    d = config
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value

def main():
    config_file = 'config.json'
    
    try:
        config = load_config(config_file)
        print("Current configuration:", json.dumps(config, indent = 4))

        #User input for updates
        setting_path = input("Enter the setting to update (eg., settings.theme):")
        new_value = input("Enter the new value: ")

        #Update the configuration
        update_setting(config, setting_path, new_value)
        
        #Save the updated configuration
        save_config(config_file, config)

    except Exception as e:
        print(f"An error occurre: {e}")

if __name__ == "__main__":
    main()
