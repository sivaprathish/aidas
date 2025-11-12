import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyC9_6L3sUL6vjgVkAyGLx3eUHM8lX0U2iY")

# Create model
model = genai.GenerativeModel('gemini-2.5-pro')

# Your question
question = input("Enter your programming question: ")

# Create prompt
prompt = f"Generate Python code for: {question}. Return only the code."

# Generate codebfs code 
response = model.generate_content(prompt)

# Print result
print("\nGenerated Code:")
print(response.text)
