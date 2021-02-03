from keep_alive import keep_alive
import random
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ie.hi'):
        await message.channel.send('fuck you')
        return
      
    if message.content.startswith('ie.i love you'):
        await message.channel.send('no <3')
        return

    if message.content.startswith('ie.beans'):
        await message.channel.send('how many beans are in my jar bro? no decimals because im stupid. if you dont say a number i wont play anymore')
        num = random.randint(0,100)
        correct = False
        msg = await client.wait_for("message")
        while correct == False:
            if msg.content == str(num):
                await message.channel.send('oh ok thats right')
                correct = True
                return
            elif (msg.content == 'i give up') or (msg.content == 'give up') or (msg.content == 'idk'):
                await message.channel.send('the answer is...')
                await message.channel.send(num)
                correct = True
                return
            elif int(msg.content) > 100: 
                await message.channel.send('fuckin slow down its under 100')
                msg = await client.wait_for("message")
            elif int(msg.content) > num:
                await message.channel.send('too high bitch')
                msg = await client.wait_for("message")
            elif int(msg.content) < num:
                await message.channel.send('too low')
                msg = await client.wait_for("message")
            else:
                await message.channel.send('you can give up or say idk bc ur still wrong')
                msg = await client.wait_for("message")
        return 

    if message.content.startswith('ie.help'):
        embed = discord.Embed(color=0x00ff00)
        embed.title = 'Available Commands' 
        embed.description = """
        **1. ie.i love you** - you can see for yourself lmfao
        **2. ie.hi** - again, see for yourself
        **3. ie.callout [map]** - callouts for any valid map
        **4. ie.maplist [map pool]** - Low Ink (LI) and SOS map pool generator
        **5. ie.dance [message]** - convert any message into terrible dancing letters 
        """
        await message.channel.send(embed=embed)
        return

    if message.content.startswith('ie.dance'):
        msg = message.content.split(' ', 1)
        conv_msg = msg[1]
        new_msg = ''
        let_dict = {'A': '<a:dance_A:770117754085703680>', 'a': '<a:dance_A:770117754085703680>', 'B': '<a:dance_B:770117819252604939>', 'b': '<a:dance_B:770117819252604939>', 'C': '<a:dance_C:770117845581299734>', 'c': '<a:dance_C:770117845581299734>', 'D': '<a:dance_D:770117861535907860>', 'd': '<a:dance_D:770117861535907860>', 'E': '<a:dance_E:770117886428577832>', 'e': '<a:dance_E:770117886428577832>', 'F': '<a:dance_F:770117901389922305>', 'f': '<a:dance_F:770117901389922305>', 'G': '<a:dance_G:770117931283251233>', 'g': '<a:dance_G:770117931283251233>', 'H': '<a:dance_H:770118006533128204>', 'h': '<a:dance_H:770118006533128204>', 'I': '<a:dance_I:770118020286251030>', 'i': '<a:dance_I:770118020286251030>', 'J': '<a:dance_J:770118035666501672>', 'j': '<a:dance_J:770118035666501672>', 'K': '<a:dance_K:770118047405965353>', 'k': '<a:dance_K:770118047405965353>', 'L': '<a:dance_L:770118058873323561>', 'l': '<a:dance_L:770118058873323561>', 'M': '<a:dance_M:770118071003643964>', 'm': '<a:dance_M:770118071003643964>', 'N': '<a:dance_N:770118083300950048>', 'n': '<a:dance_N:770118083300950048>', 'O': '<a:dance_O:770118096765059134>', 'o': '<a:dance_O:770118096765059134>', 'P': '<a:dance_P:770118109805019187>', 'p': '<a:dance_P:770118109805019187>', 'Q': '<a:dance_Q:770118122082402334>', 'q': '<a:dance_Q:770118122082402334>', 'R': '<a:dance_R:770118133804433438>', 'r': '<a:dance_R:770118133804433438>', 'S': '<a:dance_S:770118146358116373>', 's': '<a:dance_S:770118146358116373>', 'T': '<a:dance_T:770118158224064542>', 't': '<a:dance_T:770118158224064542>', 'U': '<a:dance_U:770118169163202581>', 'u': '<a:dance_U:770118169163202581>', 'V': '<a:dance_V:770118180865441812>', 'v': '<a:dance_V:770118180865441812>', 'W': '<a:dance_W:770118192101851156>', 'w': '<a:dance_W:770118192101851156>', 'X': '<a:dance_X:770118205016113163>', 'x': '<a:dance_X:770118205016113163>', 'Y': '<a:dance_Y:770118217909272617>', 'y': '<a:dance_Y:770118217909272617>', 'Z': '<a:dance_Z:770118229506785291>', 'z': '<a:dance_Z:770118229506785291>', '?': '<a:dance_qmrk:770121908145618945>', '@': '<a:dance_atsign:770121881869090837>', '!': '<a:dance_exclam:770121870316929025>', '$': '<a:dance_money:770121892707172414>', '0': '<a:dance_0:770121859106603060>', '1': '<a:dance_1:770121745239244831>', '2': '<a:dance_2:770121758484987915>', '3': '<a:dance_3:770121770631299113>', '4': '<a:dance_4:770121782245326848>', '5': '<a:dance_5:770121799324794900>', '6': '<a:dance_6:770121810229592125>', '7': '<a:dance_7:770121822326095872>', '8': '<a:dance_8:770121833223421973>', '9': '<a:dance_9:770121846694608896>'}

        for char in conv_msg:
            if char == ' ':
                new_msg += '  '
            else:
                try:
                    new_msg += let_dict[char]
                except KeyError:
                    continue

        await message.channel.send(new_msg)
        return

    if message.content.startswith('ie.callout') or message.content.startswith('ie.callouts'):
        if (message.content == 'ie.callout') or (message.content == 'ie.callouts'): 
            await message.channel.send('i need a map name 4head')
            return

        msg = message.content.split(' ', 1)
        conv_msg = msg[1]
    
        if ((conv_msg == 'ancho') or (conv_msg == 'ancho-v games') or (conv_msg == 'ancho v games')):
            await message.channel.send('callouts for Ancho-V Games <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/ancho.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'arowana') or (conv_msg == 'mall') or (conv_msg == 'arowana mall')):
            await message.channel.send('callouts for Arowana Mall <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/arrowana.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'blackbelly') or (conv_msg == 'blackbelly skatepark')):
            await message.channel.send('callouts for Blackbelly Skatepark <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/blackbelly.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'camp') or (conv_msg == 'triggerfish') or (conv_msg == 'camp triggerfish')):
            await message.channel.send('callouts for Camp Triggerfish <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/camp.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'goby') or (conv_msg == 'arena') or (conv_msg == 'goby arena')):
            await message.channel.send('callouts for Goby Arena <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/goby.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'humpback') or (conv_msg == 'pumptrack') or (conv_msg == 'humpback pump track')):
            await message.channel.send('callouts for Humpback Pump Track <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/humpback.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'inkblot') or (conv_msg == 'academy') or (conv_msg == 'inkblot academy')):
            await message.channel.send('callouts for Inkblot Art Academy <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/inkblot.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'kelp') or (conv_msg == 'dome') or (conv_msg == 'kelp dome')):
            await message.channel.send('callouts for Kelp Dome <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/kelp.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'mako') or (conv_msg == 'makomart') or (conv_msg == 'mako mart')):
            await message.channel.send('callouts for MakoMart <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/mako.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'manta') or (conv_msg == 'manta maria')):
            await message.channel.send('callouts for Manta Maria <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/manta.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'moray') or (conv_msg == 'moray towers')):
            await message.channel.send('callouts for Moray Towers <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/moray.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'musselforge') or (conv_msg == 'mussel') or (conv_msg == 'musselforge fitness')):
            await message.channel.send('callouts for Musselforge Fitness <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/musselforge.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'albacore') or (conv_msg == 'hotel') or (conv_msg == 'new albacore hotel')):
            await message.channel.send('callouts for New Albacore Hotel <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/albacore.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'pit') or (conv_msg == 'pirahna pit')):
            await message.channel.send('callouts for Pirahna Pit <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/pit.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'port') or (conv_msg == 'port mackarel')):
            await message.channel.send('callouts for Port Mackerel <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/port.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'shellen') or (conv_msg == 'shellendorf') or (conv_msg == 'shellendorf institute') or (conv_msg == 'museum')):
            await message.channel.send('callouts for Shellendorf Institute <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/shellen.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'skipper') or (conv_msg == 'skipper pavilion')):
            await message.channel.send('callouts for Skipper Pavilion <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/skipper.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'snapper') or (conv_msg == 'snapper canal')):
            await message.channel.send('callouts for Snapper Canal <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/snapper.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'starfish') or (conv_msg == 'starfish mainstage')):
            await message.channel.send('callouts for Starfish Mainstage <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/starfish.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'sturgeon') or (conv_msg == 'sturgeon shipyard')):
            await message.channel.send('callouts for Sturgeon Shipyard <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/sturgeon.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'reef') or (conv_msg == 'the reef')):
            await message.channel.send('callouts for The Reef <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/reef.png'))
            await message.channel.send('ur welcome smh')
            return

        if ((conv_msg == 'wahoo') or (conv_msg == 'wahoo world')):
            await message.channel.send('callouts for Wahoo World <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/wahoo.png'))
            await message.channel.send('ur welcome smh')
            return
        
        if ((conv_msg == 'walleye') or (conv_msg == 'walleye warehouse') or (conv_msg == 'warehouse')):
            await message.channel.send('callouts for Walleye Warehouse <:mcchi:804216602753105940>')
            await message.channel.send(file=discord.File('callouts/walley.png'))
            await message.channel.send('ur welcome smh')
            return

        else:
            await message.channel.send('i aint got that one sry')
            return

    if message.content.startswith('ie.maplist'):
        #inquires a specific map pool
        if message.content == 'ie.maplist':
            await message.channel.send('i need a specific map pool name ty')
            return

        #Low ink map pool
        if (message.content == 'ie.maplist LI') or (message.content == 'ie.maplist li') or (message.content == 'ie.maplist'):
            maps_dict = {1: 'Humpback Pump Track', 2: 'Ancho-V Games', 3: 'MakoMart', 4: 'Manta Maria', 5: 'New Albacore Hotel', 6: 'Inkblot Art Academy', 7: 'Starfish Mainstage', 8: 'Snapper Canal',  9: 'Skipper Pavillion', 10: 'Shellendorf Institute', 11: 'Wahoo World', 12: 'Sturgeon Shipyard', 13: 'Blackbelly Skatepark', 14: 'The Reef'}

            sz_list = []
            rm_list = []
            tc_list = []
            cb_list = []
            used = []

            for num in range(20): #rainmaker
                if len(rm_list) != 2: 
                    exclude = [2, 5, 9, 10, 11, 12, 14]
                    rm_int = random.randint(1,14)
                    if (rm_int not in rm_list) and (rm_int not in exclude):
                        rm_list.append(rm_int)
                        used.append(rm_int)

            for num in range(20): #zones
                if len(sz_list) != 2: 
                    exclude = [4, 6, 7, 10, 13, 14]
                    sz_int = random.randint(1,14)
                    if (sz_int not in sz_list) and (sz_int not in exclude) and (sz_int not in used):
                        sz_list.append(sz_int)
                        used.append(sz_int)
            
            for num in range(20): #clams
                if len(cb_list) != 2: 
                    exclude = [3, 7, 9, 10, 13, 14]
                    cb_int = random.randint(1,14)
                    if (cb_int not in cb_list) and (cb_int not in exclude) and (cb_int not in used):
                        cb_list.append(cb_int)
                        used.append(cb_int)

            for num in range(20): #tower 
                if len(tc_list) != 2: 
                    exclude = [1, 5, 8, 9, 13]
                    tc_int = random.randint(1,14)
                    if (tc_int not in tc_list) and (tc_int not in exclude) and (tc_int not in used):
                        tc_list.append(tc_int)

            embed = discord.Embed(color=0x00ff00)
            embed.title = 'Randomly Generated LI Maplist' 
            embed.description = '**Game 1:** Splat Zones - {0}\n **Game 2:** Rainmaker - {1}\n **Game 3:** Tower Control - {2}\n **Game 4:** Clam Blitz - {3}\n **Game 5:** Splat Zones - {4}\n **Game 6:** Rainmaker - {5}\n **Game 7:** Tower Control - {6}\n **Game 8:** Clam Blitz - {7}'.format(maps_dict[sz_list[0]], maps_dict[rm_list[0]], maps_dict[tc_list[0]], maps_dict[cb_list[0]], maps_dict[sz_list[1]], maps_dict[rm_list[1]], maps_dict[tc_list[1]], maps_dict[cb_list[1]])
            
            await message.channel.send(embed=embed)
            return 

        #SOS map pool
        if (message.content == 'ie.maplist SOS') or (message.content == 'ie.maplist sos'):
            maps_dict = {1: 'The Reef', 2: 'Starfish Mainstage', 3: 'Humpback Pump Track', 4: 'Inkblot Art Academy', 5: 'Sturgeon Shipyard', 6: 'Manta Maria', 7: 'Snapper Canal', 8: 'Blackbelly Skatepark',  9: 'MakoMart', 10: 'Pirahna Pit', 11: 'New Albacore Hotel', 12: 'Ancho-V Games', 13: 'Skipper Pavilion'}

            sz_list = []
            rm_list = []
            tc_list = []
            cb_list = []
            used = []

            for num in range(20): #rainmaker
                if len(rm_list) != 2: 
                    exclude = [1, 3, 4, 5, 9, 10, 11, 13]
                    rm_int = random.randint(1,13)
                    if (rm_int not in rm_list) and (rm_int not in exclude):
                        rm_list.append(rm_int)
                        used.append(rm_int)

            for num in range(20): #clams
                if len(cb_list) != 2: 
                    exclude = [2, 5, 6, 8, 12, 13]
                    cb_int = random.randint(1,13)
                    if (cb_int not in cb_list) and (cb_int not in exclude) and (cb_int not in used):
                        cb_list.append(cb_int)
                        used.append(cb_int)

            for num in range(20): #tower 
                if len(tc_list) != 2: 
                    exclude = [3, 7, 8, 9, 10, 11, 13]
                    tc_int = random.randint(1,13)
                    if (tc_int not in tc_list) and (tc_int not in exclude) and (tc_int not in used):
                        tc_list.append(tc_int)
                        used.append(tc_int)
            
            for num in range(20): #zones
                if len(sz_list) != 2: 
                    exclude = [6, 7, 8]
                    sz_int = random.randint(1,13)
                    if (sz_int not in sz_list) and (sz_int not in exclude) and (sz_int not in used):
                        sz_list.append(sz_int)
                        

            embed = discord.Embed(color=0x00ff00)
            embed.title = 'Randomly Generated SOS Maplist' 
            embed.description = '**Game 1:** Splat Zones - {0}\n **Game 2:** Rainmaker - {1}\n **Game 3:** Tower Control - {2}\n **Game 4:** Clam Blitz - {3}\n **Game 5:** Splat Zones - {4}\n **Game 6:** Rainmaker - {5}\n **Game 7:** Tower Control - {6}\n **Game 8:** Clam Blitz - {7}'.format(maps_dict[sz_list[0]], maps_dict[rm_list[0]], maps_dict[tc_list[0]], maps_dict[cb_list[0]], maps_dict[sz_list[1]], maps_dict[rm_list[1]], maps_dict[tc_list[1]], maps_dict[cb_list[1]])
            
            await message.channel.send(embed=embed)
            return 
    
        #world's worst map pool (repeats allowed)
        if (message.content == 'ie.maplist shitty') or (message.content == 'ie.maplist shitty maps'):
            maps_dict = {1: 'Arowana Mall', 2: 'Blackbelly Skatepark', 3: 'Port Mackerel', 4: 'Moray Towers', 5: 'Camp Triggerfish', 6: 'Kelp Dome', 7: 'Shellendorf Institute', 8: 'Goby Arena', 9: 'Snapper Canal'}

            sz_list = []
            rm_list = []
            tc_list = []
            cb_list = []

            for num in range(20): #rainmaker
                if len(rm_list) != 2: 
                    rm_int = random.randint(1,9)
                    if (rm_int not in rm_list):
                        rm_list.append(rm_int)

            for num in range(20): #clams
                if len(cb_list) != 2: 
                    cb_int = random.randint(1,9)
                    if (cb_int not in cb_list):
                        cb_list.append(cb_int)
  
            for num in range(20): #tower 
                if len(tc_list) != 2: 
                    tc_int = random.randint(1,9)
                    if (tc_int not in tc_list):
                        tc_list.append(tc_int)
            
            for num in range(20): #zones
                if len(sz_list) != 2: 
                    sz_int = random.randint(1,9)
                    if (sz_int not in sz_list):
                        sz_list.append(sz_int)

            embed = discord.Embed(color=0x00ff00)
            embed.title = 'Randomly Generated Shitty Maplist' 
            embed.description = '**Game 1:** Splat Zones - {0}\n **Game 2:** Rainmaker - {1}\n **Game 3:** Tower Control - {2}\n **Game 4:** Clam Blitz - {3}\n **Game 5:** Splat Zones - {4}\n **Game 6:** Rainmaker - {5}\n **Game 7:** Tower Control - {6}\n **Game 8:** Clam Blitz - {7}'.format(maps_dict[sz_list[0]], maps_dict[rm_list[0]], maps_dict[tc_list[0]], maps_dict[cb_list[0]], maps_dict[sz_list[1]], maps_dict[rm_list[1]], maps_dict[tc_list[1]], maps_dict[cb_list[1]])
            
            await message.channel.send(embed=embed)
            return 

    else:   
        if message.content.startswith('ie.'):
            await message.channel.send('what do u want')
            return

keep_alive()
client.run(os.getenv('TOKEN'))
