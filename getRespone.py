"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key="AIzaSyCOelXolRJbpfoNyIZD3M7TQ9mR9R69fEg")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def getPrompt(text, type):
    prompt = ""
    if (type == "begin"):
        prompt = f"Hãy giúp tôi soạn thảo 1 email hoàn chỉnh từ nội dung sau: {text}."
    elif (type == "tomtat"):
        prompt = f"Hãy góp ý cho tôi cần sửa gì ở mail này {text}."
    elif (type == "E2V"):
        prompt = f"Hãy giúp tôi chuyển văn bản sau sang tiếng Việt: {text}.Hãy dịch và không thêm gì vào."
    elif (type == "V2E"):
        prompt = f"Hãy giúp tôi chuyển văn bản sau sang tiếng Anh: {text}.Hãy dịch và không thêm gì vào."
    return prompt

def getRes(text, type):
    prompt = getPrompt(text, type)
    response = model.generate_content(prompt)
    return response.text