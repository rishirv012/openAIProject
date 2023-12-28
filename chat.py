import openai

# Set up the OpenAI API client
openai.api_key = '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'

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Who won the 2018 super bowl?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
