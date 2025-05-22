import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

number_of_images = 3

response = client.images.generate(
    model="gpt-image-1",
    prompt="A cute siamese cat chasing an orange ball. The style should be illustrated.",
    n=number_of_images,
    quality="low", #options are low, medium, high
    size="1024x1024", #options are 1024x1024, 1024x1536, 1536x1024
    )

for i in range(number_of_images):
    image_base64 = response.data[i].b64_json
    with open(f"Image Generations/CuteCat_low_illustrated_test_{i+1}.png", "wb") as f:
        image_bytes = base64.b64decode(image_base64)
        f.write(image_bytes)
    print(f"Image {i+1} saved as CuteCat_low_illustrated_test_{i+1}.png")

#print(response) #click on the url that appear in the terminal output to see the image. Next update will automaticall open the image in browser.