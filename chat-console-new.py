import os
import openai
openai.organization="org-iV********************ws"
openai.api_key=os.getenv("OPENAI_API_KEY")
#openai.Model.list()
from openai import OpenAI
client = OpenAI()
def generate_prompt_response(prompt):
	response=client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": prompt}],
		max_tokens=200,
		n=1,
		stop=None,
		temperature=0.8
	)
	#return response['choices'][0]['message']['content']
	return (response.choices[0].message.content)
while True:
	print ("Type 'exit' to close prompt!")
	user_input=input("User: ")
	if user_input == 'exit':
		print ('Thank You.')
		break
	response=generate_prompt_response(user_input)
	#print ("Type 'exit' to close prompt!")
	print("ChatGPT: ",response)
