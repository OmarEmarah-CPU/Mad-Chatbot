from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3


bot = ChatBot('MyBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///db.sqlite3',
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train("chatterbot.corpus.english")

engine = pyttsx3.init()

rate = engine.getProperty('rate')   
engine.setProperty('rate', 200)  

volume = engine.getProperty('volume')    
engine.setProperty('volume',1.0)    

voices = engine.getProperty('voices') 

while True: 
	request=input('you :') 
	if request == 'OK' or request == 'ok': 
		print('Bot: bye') 
		break
	else: 
		response=bot.get_response(request)
		print(response)
		engine.say(response)
		engine.runAndWait()

