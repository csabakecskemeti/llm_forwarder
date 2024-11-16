# llm_forwarder/config.py

import importlib.util
import os

class Config:
    def __init__(self, config):
        self.server_address = config.get("server", {}).get("address", "127.0.0.1")
        self.server_port = config.get("server", {}).get("port", 5001)
        self.openai_base_url = config.get("openai", {}).get("base_url", "http://127.0.0.1:1234/v1")
        self.openai_api_key = config.get("openai", {}).get("api_key", "na")
        self.function_path = config.get("external_function", {}).get("path")
        self.function_name = config.get("external_function", {}).get("name", "dummy_rag")
        self.rag_function = self.load_external_function()

    def load_external_function(self):
        if not self.function_path:
            raise ValueError("External function path is not set in the config.")
        
        # Load the module from the specified path
        spec = importlib.util.spec_from_file_location("rag_module", self.function_path)
        rag_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rag_module)
        
        # Retrieve the function from the module
        return getattr(rag_module, self.function_name)

