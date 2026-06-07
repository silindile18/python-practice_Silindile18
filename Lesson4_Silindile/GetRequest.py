import requests
import json

def get_groups():
    response = requests.get('https://www.ndosiautomation.co.za/APIDEV/groups')
    return response.json()

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data["data"], json_file, indent=4)

def search_group(filename):
    # Read the JSON file
    with open(filename, 'r') as json_file:
        groups = json.load(json_file)

    # Ask user for a group name
    group_name = input("Enter group name to search for: ")

    # Search for the group
    for group in groups:
        if group["Name"].lower() == group_name.lower():
            print(f"SUCCESS: Group '{group_name}' found with ID {group['Id']}")
            return

    print(f"ERROR: Group '{group_name}' was not found.")

# Get data from API
groups_data = get_groups()

# Save data to file
save_to_json(groups_data, 'groups.json')

# Search for a group
search_group('groups.json')