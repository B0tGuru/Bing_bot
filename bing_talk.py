from bingchat import BingChat

chat = BingChat()

chat.set_prompt("hello there, who are you.")

#chat.upload_image("example.jpg") 

response = chat.submit()

print(response)