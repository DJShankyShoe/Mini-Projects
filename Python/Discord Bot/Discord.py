import discord
import json
from discord.ext import commands, tasks 
from discord.utils import get
import youtube_dl
import os
from datetime import timedelta, datetime
import time
from youtube_search import YoutubeSearch
import shutil
import asyncio
#import lavalink
from discord import Embed

client = commands.Bot(command_prefix = ".")
client.remove_command("help")

song_no = 1
@client.event
async def on_ready():
    global playlist123, song_no, check_value, playlist_check, position, queue_playlist, current_song, song_list_play, add_check
    #global store1
    playlist123 = ""
    song_no = 1
    check_value = True 
    playlist_check = False
    position = 0
    queue_playlist = [False, ""]
    current_song = 0
    song_list_play = []
    add_check = False
    
    ###
    #store1 = lavalink.Client(client.user.id)
    #store2 = store1.add_node("localhost", 12345, "Legendary_Trash", "na", "music-node")
    #store3 = client.add_listener(store1.voice_update_handler, "on_socket_response")
    ###
    base.start()    
    await client.change_presence(status = discord.Status.online, activity = discord.Game(". help"))
    print("Bot is ready.")

@client.command()
async def help(ctx):
    embed = discord.Embed(title = "Commands", colour = discord.Color.orange())
    embed.add_field(name = ".trash", value = "Clears messages and channels", inline = False)
    embed.add_field(name = ".playlist", value = "Display playlists", inline = False)
    embed.add_field(name = ".play", value = "Plays music", inline = False)
    await ctx.channel.send(content = None, embed = embed)  

#trash
#########################################################################################################################
#########################################################################################################################
reset = 0
@tasks.loop(seconds = 35)
async def base():
    global channel_lists, warn_time, reset
    
    #id_lists is used in clear_chats and warning
    channel_lists = ["general", "gambling-den", "for-memelords", "uno-pundehs", "math-bot-spam", "slave-dj"]
    
    time = datetime.now()
    
    #edit time to clear chat here
    hour_time = 22
    minute_time = 30
    warn_time = 5
    #in minutes
    #edit time to clear chat here
    
    trash_time = time.replace(hour= hour_time, minute= minute_time, second=0, microsecond=0)
    trash_time2 = time.replace(hour= hour_time, minute= minute_time + 1, second=0, microsecond=0)
    
    warning_time = trash_time - timedelta(minutes = warn_time)
    warning_time2 = trash_time2 - timedelta(minutes = warn_time)
    
    if time >= warning_time and time <= warning_time2 and reset == 0: 
        await warning()
        reset += 1
    
    if time >= trash_time and time <= trash_time2: 
        await clear_chats()
        reset = 0

async def warning():
    for name in client.get_all_channels():
        if str(name) in channel_lists:
            await name.send("Clearing chat in " + str(warn_time) + " minutes")


async def clear_chats():
    for name in client.get_all_channels():
        if str(name) in channel_lists:
            await name.purge(limit = 9999999999)
    

@client.command()
async def trash(ctx, amount = None, *, x = None):
    if amount == "clear" and x == None:
        amount = 9999999998
    try:
        if x != None:
            #forces to bring up an error
            die += 1
        amount = int(amount) + 1
        await ctx.channel.purge(limit = amount)
        
    except:
        embed = discord.Embed(title = None, description = None)
        embed.add_field(name = ".trash [number]", value = "Clears the number of messages", inline = False)
        embed.add_field(name = ".trash clear", value = "Clears the enitre messages in channel", )
        await ctx.channel.send(content = None, embed = embed)

#playlist
#########################################################################################################################
#########################################################################################################################
@client.event
async def on_guild_join(guild):
    
    with open("data.json", "r") as data:
        prefix = json.load(data)
        
    prefix[str(guild.id)] = {"playlist" : None, "trash" : None}
    
    with open("data.json", "w") as data:
        json.dump(prefix, data, indent=4) 
    
    location = "MP3/" + str(guild.id)
    os.mkdir(location)
    os.mkdir(location + "/playlist/")
    os.mkdir(location + "/music/")

@client.event
async def on_guild_remove(guild):
    
    with open("data.json", "r") as data:
        prefix = json.load(data)
        
    prefix.pop(str(guild.id))
    
    with open("data.json", "w") as data:
        json.dump(prefix, data, indent=4) 
    
    location = "MP3/" + str(guild.id)
    shutil.rmtree(location)


temp_loop1 = ""
temp_loop2 = ""
@tasks.loop(seconds = 5)
async def message_music():
    global temp_loop1, temp_loop2
    location = locationX
    
    try:
        if location.find("playlist") >= 0:
            if temp_loop1 != cu_song:
                embed = Embed(colour = discord.Color.blue())
                embed.add_field(name = "Now Playing", value = cu_song)
                #embed.description = "Now Playing: " + cu_song
                await temp0.channel.send(embed=embed, delete_after = 180)
            
                temp_loop1 = cu_song
                #print("part 1")
            
        else:
            if temp_loop2 != song_list_play[0]:
                embed = Embed(colour = discord.Color.blue())
                embed.add_field(name = "Now Playing", value = song_list_play[0])
                #embed.description = "Now Playing: " + song_list_play[0]
                await temp0.channel.send(embed=embed, delete_after = 180)
                
                temp_loop2 = song_list_play[0]
            #print("part 2")
            
    except Exception as error:
        #print(error)
        pass
        
    #print(playlist_check)




def music(location):
    global check_value, playlist_check, position, queue_playlist, temp0, current_song, song_list_play
    global temp0, current_song, cu_song, file0, locationX
    check_value = False
    ctx = temp0
    file0 = ""
    
    try:
        
        def function():
            global playlist_check, position
            
            if not playlist_check:
                os.remove("./" + location + file0)
                del song_list_play[0]
                
            else:
                position += 1
            music(location)
        
        
        filetype1 =  os.listdir(location)
        for num in range(len(filetype1)):
            filetype1[num] = filetype1[num].replace(".mp3", "")
        filetype1.sort(key = int)        
        file0 =  filetype1[position] + ".mp3"
        
        voice = get(client.voice_clients, guild = ctx.guild)
        voice.play(discord.FFmpegPCMAudio(location + file0), after=lambda e: function())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.40          
        
        
        if location.find("playlist") >= 0:
            
            with open("data.json", "r") as data:
                prefix = json.load(data)
            list_name = location.replace("./MP3/" + str(ctx.guild.id) + "/playlist/", "").replace("/", "")
            cu_song = prefix[str(temp0.guild.id)]["playlist"][list_name][current_song]        
        
        current_song += 1
        locationX = location
        
        print("playing song")
        
    except IndexError:
    #except Exception as error:
        #print(error)
        
        check_value = True
        playlist_check = False
        position = 0
        
        if len(os.listdir("./MP3/" + str(ctx.message.guild.id) + "/music/")) != 0:
            music("./MP3/" + str(ctx.message.guild.id) + "/music/")
        
        if queue_playlist[0]:
            playlist_check = True
            print(playlist_check )
            current_song = 0
            music("./MP3/" + str(ctx.message.guild.id) + "/playlist/" + queue_playlist[-1] + "/")
            queue_playlist = [False, ""]            


async def download(query, location):
    global song_no, song_list_play, add_check
    
    ctx = temp0
    
    result = []
    x = 0
    while result == [] and x != 100:
        result = YoutubeSearch(query, max_results=1).to_dict()
        try:
            url = 'https://www.youtube.com' + result[0]["link"]
        except:
            x += 1
    
    voice = get(client.voice_clients, guild = ctx.guild)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        #"quiet" : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
       
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now")
        embed = Embed()
        if playlist_check:
            embed.description = "Adding playlist.\nPlease don't use any commands during this period. It will crash the bot :("
        else:
            embed.description = "Downloading Audio.\nPlease don't use any commands during this period. It will crash the bot :("
        await ctx.channel.send(embed=embed, delete_after = 0.5)
        
        ydl.download([url])
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            
            if playlist_check:
                filetype = os.listdir(location)
                if filetype != []:
                    for num in range(len(filetype)):
                        filetype[num] = filetype[num].replace(".mp3", "")
                    filetype.sort(key = int)
                    num = int(filetype[-1]) + 1
                else:
                    num = 1
                os.rename(file, str(num) + ".mp3")
                
            else:
                os.rename(file, str(song_no) + ".mp3")
                song_no += 1
                
            #print("renamed song")    
    
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            shutil.move(file, location) 
            #print("moved file")  
            
    song_name = result[0]["title"]
    
    if not playlist_check:
        song_list_play.append(song_name)    
    
    if not add_check:
        if check_value:
            embed = Embed()
            embed.description = "You can proceed to use any commands now :)"
            await ctx.channel.send(embed=embed, delete_after = 10)
            music(location) 
                
        else:
            embed = Embed()
            embed.description = "Queued Song: " + song_name
            await ctx.channel.send(embed=embed)





@client.command()
async def add(ctx, name = None, *, song = None):
    global playlist_check, temp0, add_check
    
    if name == "music":
        ctx.message.send("The attribute \"music\" is reserved. Try other playlist name instead")
    else:
        temp0 = ctx   
        add_check = True
        
        if name == None or song == None:
            await playlist_help(ctx)
            
        else:        
            with open("data.json", "r") as data:
                prefix = json.load(data)         
                
            location = "MP3/" + str(ctx.message.guild.id) + "/playlist/" + name + "/"
            if not os.path.isdir(location):
                os.mkdir(location)
            
            try:
                if song in prefix[str(ctx.guild.id)]["playlist"][name]:
                    await ctx.channel.send("\"" + song + "\" already exists in playlist: " +  name)
                    
                else:
                    temp = prefix[str(ctx.guild.id)]["playlist"][name]
                    temp.append(song)
                    prefix[str(ctx.guild.id)]["playlist"][name] = temp
                    
                    ####################################################
                    if playlist_check:
                        print("adding song")
                        await download(song, location)
                    else:
                        playlist_check = True
                        print("adding song")
                        await download(song, location)
                        playlist_check = False
                    ####################################################
                    
                    embed = discord.Embed(title = None, description = None)
                    embed.add_field(name = "New data added", value = "Playlist: " + name + "\nData: " + song)            
                    await ctx.channel.send(content = None, embed = embed) 
                   
            except Exception as error:
                print(error)
                
                if prefix[str(ctx.guild.id)]["playlist"] == None:
                    prefix[str(ctx.guild.id)]["playlist"] = {name:[song]}            
                else:
                    prefix[str(ctx.guild.id)]["playlist"][name] = [song]
                
                
                ####################################################
                if playlist_check:
                    print("adding song1")
                    await download(song, location)
                else:
                    playlist_check = True
                    print("adding song1")
                    await download(song, location)
                    playlist_check = False
                ####################################################            
                
                
                embed = discord.Embed(title = None, description = None)
                embed.add_field(name = "New data added", value = "Playlist: " + name + "\nData: " + song)        
                await ctx.channel.send(content = None, embed = embed) 
                
            with open("data.json", "w") as data:
                json.dump(prefix, data, indent=4)
        

@client.command()
async def delete(ctx, name = None, *, song = None):
    
    global playlist123
    
    with open("data.json", "r") as data:
        prefix = json.load(data)      
        
    location = "MP3/" + str(ctx.message.guild.id) + "/playlist/" + name + "/"
    
    if (name != None or name == "yes") and song == None:
        if name in prefix[str(ctx.guild.id)]["playlist"].keys() or name == "yes":
            
            if name != "yes":
                playlist123 = name
            
                embed = discord.Embed(title = None, description = None)
                embed.add_field(name = "Warning", value = "Are you sure you want to delete Playlist: \"" + name + "\"\nTo continue key in .delete yes")            
                await ctx.channel.send(content = None, embed = embed)

            if name == "yes" and song == None:
                try:
                    del prefix[str(ctx.guild.id)]["playlist"][playlist123]
                    with open("data.json", "w") as data:
                        json.dump(prefix, data, indent=4)
                    
                    shutil.rmtree("MP3/" + str(ctx.message.guild.id) + "/playlist/" + playlist123 + "/")
                    
                    await ctx.channel.send("Successfully deleted")
                except Exception as error:
                    print(error)
                    await ctx.channel.send("Invalid Command")
                    
                playlist123 = ""
        else:
            await ctx.channel.send("Playlist: " + name + " does not exist")
            
    elif name != None and song != None:
        if name in prefix[str(ctx.guild.id)]["playlist"].keys():
            if song in prefix[str(ctx.guild.id)]["playlist"][name]:
                
                x = 0
                for data0 in prefix[str(ctx.guild.id)]["playlist"][name]:
                    if song == data0:
                        number = x
                        break
                    x += 1
                
                x = 0
                filetype2 = os.listdir(location)
                
                for num in range(len(filetype2)):
                    filetype2[num] = filetype2[num].replace(".mp3", "")
                filetype2.sort(key = int)                 
                
                for types in filetype2:
                    if number == x:
                        os.remove(location + types + ".mp3")
                        break
                    x += 1
                
                prefix[str(ctx.guild.id)]["playlist"][name].remove(song)
                with open("data.json", "w") as data:
                    json.dump(prefix, data, indent=4)                
                
                embed = discord.Embed(title = None, description = None)
                embed.add_field(name = "Deleted", value = "\"" + song + "\" has been deleted from Playlist: " + name)            
                await ctx.channel.send(content = None, embed = embed)
                
            else:
                await ctx.channel.send("Data: \"" + song + "\" does not exist in Playlist: " + name)
        else:
            await ctx.channel.send("Playlist: \"" + name + "\" does not exist")        
                
        
    else:
        await playlist_help(ctx)
    
    
@client.command()
async def playlist(ctx, message = None, *, help = None):
    
    with open("data.json", "r") as data:
        prefix = json.load(data)    
    
    if message == "all" and help == None:
        if prefix[str(ctx.guild.id)]["playlist"] != None and prefix[str(ctx.guild.id)]["playlist"] != {}:
            
            title = ""
            output = ""
            for playlist in prefix[str(ctx.guild.id)]["playlist"].keys():
                title = "Playlist: " + playlist
                if len(prefix[str(ctx.guild.id)]["playlist"][playlist]) == 0:
                    output = "<<No Data>>"
                else:
                    tempx = 0
                    tx = []
                    tpx = 0
                    for data in prefix[str(ctx.guild.id)]["playlist"][playlist]:
                        output += "- " + data + "\n"
                        tempx += 1
                        
                        if tempx == 32 and tpx == 0:
                            embed = discord.Embed(title = None, description = None)
                            embed.add_field(name = title, value = output, inline = False)
                            await ctx.channel.send(content = None, embed = embed)
                            output = "" 
                            tempx = 0
                            tpx += 1
                            
                        elif tempx == 32 and tpx > 0:
                            #print(output)
                            embed = discord.Embed(title = None, description = None)
                            embed.add_field(name = "|", value = output, inline = False)
                            await ctx.channel.send(content = None, embed = embed)
                            output = ""
                            tempx = 0
                    
                    if tempx < 32 and tpx == 0:
                        embed = discord.Embed(title = None, description = None)
                        embed.add_field(name = title, value = output, inline = False)
                        await ctx.channel.send(content = None, embed = embed)
                        
                    elif tempx < 32 and tpx > 0:
                        embed = discord.Embed(title = None, description = None)
                        embed.add_field(name = "|", value = output, inline = False)
                        await ctx.channel.send(content = None, embed = embed) 
                        
                    output = ""
                    tempx  = 0
                    tpx = 0
            
        else:
            await ctx.channel.send("You have an empty playlist")
    
    else:
        await playlist_help(ctx)

async def playlist_help(ctx):
    
    embed = discord.Embed(title = None, description = None)
    embed.add_field(name = ".add [List Name] [Song/data]", value = "Stores data in a playlist", inline = False)
    embed.add_field(name = ".delete [List Name]", value = "Deletes entire playlist", inline = False)
    embed.add_field(name = ".delete [List Name] [Song/data]", value = "Deletes data in playlist", inline = False)
    embed.add_field(name = ".playlist all ", value = "Displays created playlists and data")
    await ctx.channel.send(content = None, embed = embed)    

#voice
#########################################################################################################################
#########################################################################################################################
#@client.command()
#async def play(ctx):
    #channel = ctx.author.voice.channel
    #await channel.connect()

#@client.command()
#async def leave(ctx):
    #await ctx.voice_client.disconnect()
    
#@client.command()
#async def join(ctx):
    #global voice
    
    ###### lavalink
    ##global player
    ##player = store1.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
    ######
    
    #channel = ctx.message.author.voice.channel
    #voice = get(client.voice_clients, guild = ctx.guild)
    
    #if voice and voice.is_connected():
        #await voice.move_to(channel)
    #else:
        #voice = await channel.connect()    
        #print("The bot has connected to " + str(channel))

@client.command()
async def leave(ctx):
    global check_value, playlist_check, position, queue_playlist, song_list_play
    
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    
    location = "MP3/" + str(ctx.message.guild.id) + "/music/"
    
    if voice and voice.is_connected():
        await voice.disconnect()
        
        check_value = True
        playlist_check = False
        position = 0
        queue_playlist = [False, ""]
        message_music.stop() 
        song_list_play = []
        
        try:
            for file in os.listdir(location):
                os.remove(location + file) 
        except:
            x1 = 0
            for file in os.listdir(location):
                if x1 != 0:
                    os.remove(location + file)
                x1 += 1
        
        print("The bot has left " + str(channel))
    else:
        print("Bot not in channel")
    
    try:
        check_value = True
        playlist_check = False
        position = 0
        queue_playlist = [False, ""]
        message_music.stop() 
        song_list_play = []
        
        try:
            for file in os.listdir(location):
                os.remove(location + file) 
        except:
            x1 = 0
            for file in os.listdir(location):
                if x1 != 0:
                    os.remove(location + file)
                x1 += 1
    except:
        pass
                
                

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if voice and voice.is_connected():
        voice.pause()
    else:
        print("Bot not in voice channel")

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if voice and voice.is_connected():
        voice.resume()
    else:
        print("Bot not in voice channel")

@client.command()
async def skip(ctx):
    voice = get(client.voice_clients, guild = ctx.guild)
    
    if voice and voice.is_connected():
        voice.stop()
    else:
        print("Bot not in voice channel")

    

@client.command()
async def play(ctx, prefix = None, *, query = None):
    global temp0, playlist_check, check_value, queue_playlist, add_check
    
    if (prefix == None and query == None) or (prefix == "-p" and query == None):
        
        embed = discord.Embed(title = None, description = None)
        embed.add_field(name = ".play [song name]", value = "Plays a song.\nWARNING: Song length cannot exceed 1 hour", inline = False)
        embed.add_field(name = ".play -p [playlist name]", value = "Plays the specified playlist", inline = False )
        embed.add_field(name = ".pause", value = "Pauses the song", inline = False )
        embed.add_field(name = ".resume", value = "Resume playing the song", inline = False )
        embed.add_field(name = ".skip", value = "Skips current song", inline = False )
        embed.add_field(name = ".leave", value = "Bot leaves the voice Channel", inline = False )
        await ctx.channel.send(content = None, embed = embed)
        
    else:
        
        location = "MP3/" + str(ctx.message.guild.id) + "/music/"
        temp0 = ctx 
        
        try:
            channel = ctx.message.author.voice.channel
            voice = get(client.voice_clients, guild = ctx.guild)
            
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()    
                print("The bot has connected to " + str(channel))
            
            
            if prefix != "-p":
            
                if query == None:
                    query = ""
                await download(prefix + " " + query, location)
                add_check = False
            
            else:            
                with open("data.json", "r") as data:
                    prefix = json.load(data) 
                    
                if query in prefix[str(ctx.guild.id)]["playlist"].keys():
                    #print("pass1")
                    if not playlist_check and not queue_playlist[0]:
                        #print("pass2")
                        if check_value:
                            #print("pass3")
                            playlist_check = True
                            music("MP3/" + str(ctx.message.guild.id) + "/playlist/" + query + "/")
                            embed = Embed()
                            embed.description = "Playing Playlist: " + query                        
                        else:
                            #print("pass4")
                            queue_playlist[0] = True
                            queue_playlist[-1] = query
                            embed = Embed()
                            embed.description = "Queued to play Playlist: \"" + query + "\" after finishing non-playlist songs"
                            
                        await ctx.channel.send(embed = embed)
                    else:
                        await ctx.channel.send("Already playing/queued a playlist")
                else:
                    await ctx.channel.send("Playlist: " + query + " does not exist")
                
            try:
                message_music.start()
            except:
                pass
                
            
        except Exception as error:
            print(error)
            await ctx.channel.send("You need to be connected to a voice channel first/An error has occured, please try again")
            
        


################################################################################
        
       
        #try:
            #player = store1.player_manager.get(ctx.guild.id)
            #query = f'ytsearch:{query}'
            #results = await player.node.get_tracks(query)
            #tracks = results['tracks'][0:10]
            #i = 0
            #query_result = ''
            #for track in tracks:
                #i = i + 1
                #query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'
            #embed = Embed()
            #embed.description = query_result
        
            #await ctx.channel.send(embed=embed)
        
            #def check(m):
                #return m.author.id == ctx.author.id
        
            #response = await client.wait_for('message', check=check)
            #track = tracks[int(response.content)-1]
        
            #player.add(requester=ctx.author.id, track=track)
            #if not player.is_playing:
                #await player.play()
                #print("playing")
    
        #except Exception as error:
            #print(error)
        
        
client.run("x")
