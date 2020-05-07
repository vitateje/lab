from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.portuguese")

#bot.set_trainer(ListTrainer)
#bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')