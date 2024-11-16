from setuptools import setup, find_packages

setup(
    name="llm-forwarder",
    version="0.1.0",
    author="Csaba Kecskemeti",
    description="A configurable forwarder for OpenAI-compatible LLM requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/csabakecskemeti/llm_forwarder",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0",
        "openai",
        # Add any other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

