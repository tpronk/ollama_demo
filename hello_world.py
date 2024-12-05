import ollama
prompt = 'Create a table with planets of the solar system, adding features like weight and distance from the sun'
response = ollama.chat(model='llama3.2', messages=[{ 'role': 'user', 'content': prompt }])
print(response['message']['content'])