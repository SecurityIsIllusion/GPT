import os
import openai
import webbrowser
openai.organization="org-iV********************ws"
openai.api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI

client = OpenAI()

def image_prompt(PROMPT):
	response=client.images.generate(
		model= "dall-e-3",
		prompt=PROMPT,
		quality="hd",
		n=1,
		#size="1024x1024",
		size="1792x1024",
		#size=#1024x1792",
	)
	return(response.data[0].url)

#PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
#PROMPT = "A monkey with Ice Cream"
#PROMPT = "Sunny Leone Bollywood with Monkey"

#openai.api_key = os.getenv("OPENAI_API_KEY")

#response = openai.Image.create(
#    prompt=PROMPT,
#    n=1,
#    size="256x256",
#)

#print(response["data"][0]["url"])

while True:
	print ("Type 'exit' to close prompt!")
	user_input=input("User: ")
	if user_input == 'exit':
		print('Thank You.')
		break
	response=image_prompt(user_input)
	webbrowser.open(response)
	#print("ChatGPT: ",response)
