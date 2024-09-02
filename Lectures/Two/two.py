import google.generativeai as genai


api_key = "AIzaSyDMhYAHLqk1AjmMUQ0Eby5ycLlNDM92x10"

genai.configure(api_key=api_key)

# text_prompt = "A cat playing with a ball of yarn"
# image = client.generate_image(text_prompt)
# image.save("generated_image.jpg")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)