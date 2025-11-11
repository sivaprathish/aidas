import google.generativeai as genai
genai.configure(api_key="AIzaSyAFtPzArLvp377CsuAD1u-lBeKlYPuCYkg")
model = genai.GenerativeModel('gemini-2.5-pro')
question = input("Enter your programming question: ")
prompt = f"Generate Python code for: {question}. Return only the code, with no comments or explanations."
response = model.generate_content(prompt)
print("\nGenerated Code:")
print(response.text)

