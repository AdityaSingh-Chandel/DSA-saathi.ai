import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key = os.getenv("Gemini_API_Key")
)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_approach(problem_statement):
    prompt = f"""
    Role: You are an expert in Data Structures and Algorithms (DSA).
    Your Task: Understand the problem statement,analyze it, tell about the pattern and how to solve this and similar problems. Keep your response concise and clear. Do not generate unnecesary code or explanations. Focus on the approach and the steps to solve the problem.

    Problem Statement:
    {problem_statement}
    """

    response = model.generate_content(prompt)

    return response.text