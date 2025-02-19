from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement


bot = ChatBot('MyBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///db.sqlite3',
        logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train("chatterbot.corpus.english")


while True: 
	request=input('you :') 
	if request == 'OK' or request == 'ok': 
		print('Bot: bye') 
		break
	else: 
		response=bot.get_response(request) 
		print('Bot:', response) 

