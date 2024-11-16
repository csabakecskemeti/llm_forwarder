# llm_forwarder/server.py

from flask import Flask, request, jsonify
from openai import OpenAI
from .config import Config

class LLMForwarder:
    def __init__(self, config):
        self.config = Config(config)
        self.client = OpenAI(
            base_url=self.config.openai_base_url,
            api_key=self.config.openai_api_key,
        )
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/v1/chat/completions', methods=['POST'])
        def handle_chat_completion():
            data = request.json
            # Apply the external RAG function
            if self.config.rag_function:
                data['messages'] = self.config.rag_function(data['messages'])
            
            # Call the local model with the updated data
            response = self.client.chat.completions.create(**data)
            response_dict = response.to_dict()
            return jsonify(response_dict)

    def run(self):
        self.app.run(debug=True, host=self.config.server_address, port=self.config.server_port)

