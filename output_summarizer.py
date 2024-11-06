import config
import google.generativeai as genai

genai.configure(api_key=config.LLM_API)

model = genai.GenerativeModel("gemini-pro")  # Choose the desired model

def op_summary(text):
	pre_prompt = "Summarize this data with proper sections."
	prompt = pre_prompt + text
	response = model.generate_content(prompt)
	return response.text
