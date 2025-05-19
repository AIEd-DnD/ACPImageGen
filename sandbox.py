import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model="gpt-image-1",
    prompt="A cute grey cat wearing round orange glasses",
    n=1,
    quality="medium", #options are low, medium, high
    size="1024x1024", #options are 1024x1024, 1024x1536, 1536x1024
    )

image_base64 = response.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("Image Generations/Test1.png", "wb") as f:
    f.write(image_bytes)

print(response) #click on the url that appear in the terminal output to see the image. Next update will automaticall open the image in browser.