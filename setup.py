# setup.py

from setuptools import setup, find_packages

setup(
    name="llm_forwarder",
    version="0.1.1",
    description="LLM Forwarder with configurable external function",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.0",
        "openai>=0.27.0"
    ],
    entry_points={
        'console_scripts': [
            'llm-forwarder=llm_forwarder.server:main'
        ],
    },
)

