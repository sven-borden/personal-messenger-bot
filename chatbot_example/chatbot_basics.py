from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create ChatBot with specific storage adapter and logic adapter
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train the bot with an entry
trainer = ListTrainer(bot)
trainer.train([
    'Hi',
    'Hello',
    'I need your assistance regarding my order',
    'Please, Provide me with your order id',
    'I have a complaint.',
    'Please elaborate, your concern',
    'How long it will take to receive an order ?',
    'An order takes 3-5 Business days to get delivered.',
    'Okay Thanks',
    'No Problem! Have a Good Day!'
])

# Dummy Testing
response = bot.get_response('I have a complaint.')
print(f'Dummy Test {response}')

# Proper testing
while True:
    request = input()
    if request == 'exit':
        break
    response = bot.get_response(request)
    print(response)
