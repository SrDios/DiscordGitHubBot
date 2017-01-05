import discord
import asyncio
from commit import Commit
from github import Github

# First create a Github instance:
g = Github("user", "password")

def checkCommits():
    commitlist = []
    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)
        print(repo.id)
        print(repo.updated_at)
        for commit in repo.get_commits():
            commit = Commit(commit.commit.sha,commit.commit.message,commit.html_url);
            '''print(commit.commit.sha)'''
            '''print(commit.commit.message)'''
            commitlist.append(commit)
            '''print(commit)'''
        commitlist.reverse()
        '''for commit in commitlist:
            print(commit)'''
    return commitlist



client = discord.Client()
botkey = 'GsOxNzI1NDEwNjkXXTk3MjQ5.CrdAWw.c3wqsyXLlu2jzxx_xS7Hvx0XxHk'
channelnumber = 100707500019139000
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    for channel in client.get_all_channels():
        '''print(channel.id)'''
        '''print(channel.name)'''
        if (channel.name == "commits"):
            devchannel = channel
    setsha = set()
    nosha = True

    if message.content.startswith('!check'):
        commitlist = checkCommits()
        counter = 0
        '''devchannel = client.get_channel(channelnumber)'''
        tmp = await client.send_message(devchannel, 'Checking commits...')
        '''Sacamos los últimos mensajes y los concatenamos en una string.'''
        async for log in client.logs_from(devchannel, limit=100):
            if("SHA: " in log.content):
                nosha = False
                shaindex = log.content.index('SHA: ')
                setsha.add(log.content[shaindex+5:])

        for commit in commitlist:
            if (setsha.add(commit.getSha())):
                print("No está en la lista ergo lo publicamos")
                counter += 1
                await client.send_message(devchannel, str(commit))
            else:
                print("Ya está en la lista, no hacemos nada.")

        '''for sha in setsha:'''

        if(nosha):
            print("First Time!")
            for commit in commitlist:
                await client.send_message(devchannel, str(commit))


        await client.edit_message(tmp, 'Tenemos {} commits nuevos.'.format(counter))
        if(counter == 0):
            for repo in g.get_user().get_repos():
                updated = repo.updated_at

            await client.edit_message(tmp, 'No se encontraron nuevos commits, último commít fue en: {}'.format(updated))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(botkey)

