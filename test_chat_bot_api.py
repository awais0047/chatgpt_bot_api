import requests

BASE_URL = "http://localhost:5000"

def create_prompt(prompt):
    response = requests.post(f"{BASE_URL}/create_prompt", json={"prompt": prompt})
    return response.json()

def get_response(prompt_index):
    response = requests.get(f"{BASE_URL}/get_response/{prompt_index}")
    return response.json()

def update_prompt(prompt_index, new_prompt):
    response = requests.put(f"{BASE_URL}/update_prompt/{prompt_index}", json={"new_prompt": new_prompt})
    return response.json()

def delete_prompt(prompt_index):
    response = requests.delete(f"{BASE_URL}/delete_prompt/{prompt_index}")
    return response.json()

if __name__ == '__main__':
    # Initialize the prompt with the API
    prompt_index = create_prompt("what is jwt tell me in short.")['prompt_index']
    print(prompt_index)

    # Get response for the prompt
    response = get_response(prompt_index)
    print("Response for prompt:", response['response'])

    # Update the prompt
    update_result = update_prompt(prompt_index, "what is decorator.")
    print("Update result:", update_result['message'])

    # Get response for the updated prompt
    response = get_response(prompt_index)
    print("Response for updated prompt:", response['response'])

    # Delete the prompt
    delete_result = delete_prompt(prompt_index)
    print("Delete result:", delete_result['message'])
