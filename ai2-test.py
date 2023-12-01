import os
import openai
openai.organization = "org-iVW********************s"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
def generate_prompt_response(prompt):
	response = openai.ChatCompletion.create(
	    	model="gpt-3.5-turbo",
		messages=[
        		{"role": "system", "content": "You are a helpful assistant."},
        		#{"role": "user", "content": "Who won the world series in 2020?"},
        		#{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
       			{"role": "user", "content": prompt}
		],
		#prompt=f'You are a helpful assistant.\nUser: {prompt}',
		max_tokens=200,
		n=1,
		stop=None,
        	temperature=0.8
	)
	return response['choices'][0]['message']['content']
#print (response)
#print (response['choices'][0]['message']['content'])
while True:
	user_input = input("User: ")
	response = generate_prompt_response(user_input)
	print("ChatGPT:", response)
