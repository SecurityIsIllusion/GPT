import os
import openai
openai.organization="org-iV*********************ws"
openai.api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI
client = OpenAI()

def mod(PROMPT):
	response = client.moderations.create(
		input=PROMPT
	)
#	return response.results[0]
	return (response.results[0].flagged)


while True:
	print ("Type 'exit' to close prompt!")
	user_input=input("User: ")
	# user_input = "i want to kill pakistan"
	if user_input == 'exit':
		print('Thank You.')
		break
	response=mod(user_input)
	print("ChatGPT: ",response)

