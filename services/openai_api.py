from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_text(prompt):
    r = client.chat.completions.create(
        model="gpt-4.2-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content

def generate_image(prompt):
    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )
    return img.data[0].url
    