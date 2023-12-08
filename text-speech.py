import os
import openai
from openai import OpenAI
openai.organization="org-iV********************ws"
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

#from openai import OpenAI
def data(recv):
    response = client.audio.speech.create(
   	 model="tts-1",
   	 voice="nova",
   	 input=recv,
   	 #input="Hello world! This is a streaming test.",
    )
    return response.stream_to_file("output.mp3")


while True:
    print ("Type 'exit' to close prompt!")
    user_input=input("User: ")
    if user_input == 'exit':
   	 print('Thank You.')
   	 break
    response=data(user_input)
    print("ChatGPT: ",response)
