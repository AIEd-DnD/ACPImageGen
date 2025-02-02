import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model="dall-e-2",
    prompt="A cute grey cat wearing round orange glasses",
    n=1,
    size="1024x1024", #options are 256x256, 512x512, 1024x1024
    )

print(response) #click on the url that appear in the terminal output to see the image. Next update will automaticall open the image in browser.