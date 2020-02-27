import aiml # version: python-aiml 0.9.3

bot = aiml.Kernel()
bot.learn("dialogue.xml")

print(bot.respond("inicio"))

while True:
    print("> ", end='')
    i = input()
    response = bot.respond(i)
    print(response)
    if response == "Obrigado pela preferencia, volte sempre.":
        break