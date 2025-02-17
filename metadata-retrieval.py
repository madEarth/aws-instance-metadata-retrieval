import requests
import json

def get_token():
    response = requests.put(
        "http://169.254.169.254/latest/api/token",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "600"}
    )
    response.raise_for_status()
    return response.text

def list_available_metadata(token):
    response = requests.get(
        "http://169.254.169.254/latest/meta-data/",
        headers={"X-aws-ec2-metadata-token": token}
    )
    response.raise_for_status()
    return response.text.splitlines()

def get_instance_metadata(keys, token):
    baseurl = "http://169.254.169.254/latest/meta-data/"
    headers={"X-aws-ec2-metadata-token": token}
    metadata = {}

    if keys.lower() in ["all", "list"]:
        available_keys = list_available_metadata(token)
        if keys.lower() == "list":
            print("Available metadata keys:\n" + "\n".join(available_keys))
            keys = input("Enter metadata key(s) you want to retrieve (comma or space-separated): ").strip()
        else:
            keys = " ".join(available_keys)
    
    key_list = [key.strip() for key in keys.replace(",", " ").split() if key.strip()]

    for key in key_list:
        response = requests.get(baseurl + key, headers=headers)
        metadata[key] = response.text if response.status_code == 200 else f"Error: Unable to retrieve '{key}', please check metadata key name"

    return json.dumps(metadata, indent=4)

if __name__ == "__main__":
    print("**AWS instance matadata retrieval tool**")
    try:
        token = get_token()
        user_input = input("Enter one or more metadata keys (comma or space-separated), 'all' to retrieve everything, or 'list' to see available keys: ").strip()
        print(get_instance_metadata(user_input, token))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
