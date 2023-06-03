import openai
import config

openai.api_key = config.GPT_API

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages={
        "role": "system",
        "content": "Hello"
    }
)
print(response)













# # Модель 
# completion = openai.Completion.create(engine=engine, 
#                                       prompt=prompt, 
#                                       max_tokens=1000)
# # message = completion.choices[0].text
# print(completion) 