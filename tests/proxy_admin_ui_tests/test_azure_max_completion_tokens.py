import os
import sys
import pytest
from unittest.mock import patch, MagicMock
import json

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath("../.."))
import litellm
from litellm.llms.azure.chat.gpt_transformation import AzureOpenAIConfig

API_KEY = "XXX"

@pytest.mark.asyncio
async def test_azure_max_completion_tokens_mapping():
    os.environ["AZURE_API_KEY"] = API_KEY
    response = litellm.completion(
        model="azure/gpt-4o",
        api_base="https://XXX.openai.azure.com/",
        api_version="2024-08-01-preview",
        api_key=API_KEY, 
        messages=[{"role": "user", "content": "hi"}],
        max_completion_tokens=100,
        # max_tokens=100,
    )

    print("response=", response)

    # Check that max_completion_tokens was mapped to max_tokens
    data = response._hidden_params
    assert 1 == 2
    assert response.choices[0].message.content is not None
