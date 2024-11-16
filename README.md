# LLMForwarder

`LLMForwarder` is a Python package for forwarding chat requests to a locally hosted model API (such as OpenAI-compatible models). It allows users to configure the server address, port, and OpenAI API details, as well as customize request handling through an external function. This package is ideal for injecting custom context or pre-processing user messages before forwarding to the model API.

## Features

- Configurable server address and port
- Flexible OpenAI API integration
- Customizable prompt-handling function, allowing easy injection of context or prompt modifications
- Easy setup and usage for OpenAI-compatible models

## Installation

To install `LLMForwarder`, use pip:

```bash
pip install llm-forwarder

