import openai
from flask import Flask, jsonify, request

class ChatGPTBotAPI:
    def __init__(self, openai_api_key):
        self.api_key = openai_api_key
        self.prompts = {}
    
    # Initialize the OpenAI API with your credentials
    def initialize_gpt3(self):
        openai.api_key = self.api_key

    def create_prompt(self, prompt):
        #Storing prompt
        prompt_index = len(self.prompts)
        self.prompts[prompt_index] = prompt
        return prompt_index

    def get_response(self, prompt_index):
        #Interacting with Chatgpt
        if prompt_index not in self.prompts:
            return "Prompt not found."
        prompt = self.prompts[prompt_index]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def update_prompt(self, prompt_index, new_prompt):
        # updating propmt index
        if prompt_index not in self.prompts:
            return "Prompt not found."
        self.prompts[prompt_index] = new_prompt
        return "Prompt updated successfully."

    def delete_prompt(self, prompt_index):
        # Deleteing index
        if prompt_index not in self.prompts:
            return "Prompt not found."
        del self.prompts[prompt_index]
        return "Prompt deleted successfully."

app = Flask(__name__)
openai_api_key = 'ADD_YOUR_SECRET_KEY'
bot_api = ChatGPTBotAPI(openai_api_key)
bot_api.initialize_gpt3()

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"message": "Invalid request. 'prompt' parameter is missing."}), 400

    prompt_index = bot_api.create_prompt(prompt)
    return jsonify({"prompt_index": prompt_index}), 201

@app.route('/get_response/<int:prompt_index>', methods=['GET'])
def get_response(prompt_index):
    response = bot_api.get_response(prompt_index)
    return jsonify({"response": response}), 200

@app.route('/update_prompt/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    data = request.get_json()
    new_prompt = data.get('new_prompt')
    if not new_prompt:
        return jsonify({"message": "Invalid request. 'new_prompt' parameter is missing."}), 400

    result = bot_api.update_prompt(prompt_index, new_prompt)
    return jsonify({"message": result}), 200

@app.route('/delete_prompt/<int:prompt_index>', methods=['DELETE'])
def delete_prompt(prompt_index):
    result = bot_api.delete_prompt(prompt_index)
    return jsonify({"message": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
