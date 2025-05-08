from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)