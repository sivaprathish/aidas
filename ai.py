import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyAFtPzArLvp377CsuAD1u-lBeKlYPuCYkg")

# Create model
model = genai.GenerativeModel('gemini-2.5-pro')

# Your question
question = input("Enter your programming question: ")

# Create prompt (simple code, no comments or explanations)
prompt = f"Generate Python code for: {question}. Return only the code, with no comments or explanations."

# Generate code
response = model.generate_content(prompt)

# Print result
print("\nGenerated Code:")
print(response.text)
