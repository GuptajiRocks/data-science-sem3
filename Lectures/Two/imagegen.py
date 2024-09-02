from openai import OpenAI
client = OpenAI(api_key="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")

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url