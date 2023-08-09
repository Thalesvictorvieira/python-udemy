import time
import discord





# Crie uma instância do bot
bot = discord.Client()

# Evento que é acionado quando o bot estiver pronto e conectado ao Discord
@bot.event
async def on_ready():
    print(f'{bot.user} está conectado ao Discord!')

# Evento que é acionado quando uma mensagem é enviada para o servidor
@bot.event
async def on_message(message):
    # Verifique se a mensagem foi enviada por um bot para evitar loops infinitos
    if message.author.bot:
        return

    # Verifique se a mensagem começa com um comando específico (por exemplo, !executar)
    if message.content.startswith('!executar'):
        # Obtenha o conteúdo da mensagem após o comando
        command = message.content[len('!executar'):].strip()

        try:
            # Execute o comando usando a função "exec" do Python (use com cautela!)
            exec(command)
            await message.channel.send("Comando executado com sucesso!")
        except Exception as e:
            await message.channel.send(f"Ocorreu um erro: {e}")

# Conecte o bot ao Discord usando o token
bot.run('MTEzNzc5NDcwNzk5NzYxMDAzNg.G5raji.eHMUnDJPBEKOG2mS6TIldB99b_RLxtl4Oa-ucM')
