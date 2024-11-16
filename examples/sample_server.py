from llm_forwarder import LLMForwarder
from example_config import config

# Initialize and run the server with the provided configuration
server = LLMForwarder(config)
server.run()

