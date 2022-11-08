import subprocess
import os
import os.path
from datetime import date
from datetime import timedelta

#this is a test
#test 2
guildid = ''
token = ''
partition = ''
parent_dir = ''
settingsfilename = "Settings.txt"
settingspath = './/'

#rerad settings from Settings.txt
file_path = os.path.join(settingspath, settingsfilename)

with open(file_path, 'r') as a:
    for line in a:
        if not line == '\n':
            elements = line.split(' ')[0]
            Data = line.split(' ')[1]
            Data1 = Data.replace('\n', '')

            if elements == 'token:':
                token = Data1
                    
            if elements == 'path:':
                parent_dir = Data1
                    
            if elements == 'messages:':
                partition = Data1
                    
if parent_dir == '':
    parent_dir = './/'

print(token)
print(parent_dir)
print(partition)

#downlods list of joined servers
get_guild_list = 'dotnet DiscordChatExporter.Cli.dll guilds --token ' + token +' > .//guilds.txt'

p = subprocess.Popen(get_guild_list, stdout=subprocess.PIPE, text=True, shell=True)
p.wait()
print('downloded list of all joined guilds to find the selected guild name')
print(p.stdout)
with open(file_path, 'r') as a:
    for line in a:
            
        if not line == '\n':
            elements = line.split(' ')[0]
            Data = line.split(' ')[1]
            Data1 = Data.replace('\n', '')

            if elements == 'guildid:':
                guildid = Data1
            
                #downloads channel list of the matching server and saves it in a txt file
               
                    
                get_dfc_channel_list = 'dotnet DiscordChatExporter.Cli.dll channels --guild ' + guildid + ' --token ' + token +' > .//channels.txt'

                p = subprocess.Popen(get_dfc_channel_list, shell=True)
                p.wait()
                print('downloded guild channel list')

                #Find guild name
                with open('guilds.txt', 'r') as f:
                    for line in f:
                            guildelid = line.split(' ')[0]
                            if guildelid == guildid:
                                guildname = line.split('|')[1]
                                replace0 = guildname.strip()
                                replace1 = replace0.replace(' ', '_')
                                replace2 = replace1.replace('\n','')
                                replace3 = replace2.replace('?', '')
                                replace4 = replace3.replace(':', '')
                                replace5 = replace4.replace('"', '')
                                replace6 = replace5.replace('<', '')
                                replace7 = replace6.replace('>', '')
                                replace8 = replace7.replace('|', '')
                                replace9 = replace8.replace('*', '')
                                replace10 = replace9.replace('\x0c', 'girl')
                                replace11 = replace10.replace('\x0b', 'boy')
                                #replace10 = replace8.replace('\', '')
                                servername = replace11.replace('/', '(')
                                print('servername:'+servername)
                                

                    with open('channels.txt', 'r') as f:
                        for line in f:
                            #listet alle channel ids auf
                            channelid = line.split(' ')[0]
                            print(line)
                            #Wandelt die namen der channels in pfäde um und speichert sie als
                            #ordner ab fals sie noch nicht exestiren
                            channelname = line.split('|')[1]
                            areplace0 = channelname.strip()
                            areplace1 = areplace0.replace(' ', '')
                            areplace2 = areplace1.replace('\n','')
                            areplace3 = areplace2.replace('?', '')
                            areplace4 = areplace3.replace(':', '')
                            areplace5 = areplace4.replace('"', '')
                            areplace6 = areplace5.replace('<', '')
                            areplace7 = areplace6.replace('>', '')
                            areplace8 = areplace7.replace('|', '')
                            areplace9 = areplace8.replace('*', '')
                            areplace10 = areplace9.replace('\x0c', 'girl')
                            areplace11 = areplace10.replace('\x0b', 'boy')
                            #areplace10 = areplace8.replace('\', '')
                            nospace = areplace11.replace(' ', '')

                            a = nospace.replace('\n', '')
                            b = servername + '/' + a
                            print(b)
                            print(channelid)

                            

                            path = os.path.join(parent_dir, b)
                            if not os.path.exists(path):
                                os.makedirs(path)
                                print('folder created')

                            html = '0'
                            for file in os.listdir(path):
                                if file.endswith('.html'):
                                    html = '1'

                            filename = "date.txt"
                            file_path = os.path.join(path, filename)

                            today = date.today()
                            yesterday = today - timedelta(days = 1)
                            yesterday_format = yesterday.strftime("%m-%d-20%y")
                            print("Yesterday was: ", yesterday_format)

                            if html == '1':
                                print('is not the first backub')

                                date_from_txt_file = ''

                                with open(file_path, 'r') as f:
                                    for line in f:
                                        date_from_txt_file = line
                                        

                                csf = 'dotnet DiscordChatExporter.Cli.dll export --channel ' + channelid + ' --token ' + token + ' --media true --reuse-media true --partition ' + partition + ' --after ' + date_from_txt_file  + ' --before ' + yesterday_format + ' -o ' + path

                                p = subprocess.Popen(csf, shell=True)
                                p.wait()
                                
                                with open(file_path, "w") as f:
                                    f.write(yesterday_format)

                            if html == '0':
                                #lädt erstes backub herunter
                                

                                create_first_file = 'dotnet DiscordChatExporter.Cli.dll export --channel ' + channelid + ' --token ' + token + ' --media true --reuse-media true --partition ' + partition + ' --before ' + yesterday_format + ' -o ' + path

                                p = subprocess.Popen(create_first_file, shell=True)
                                p.wait()

                                with open(file_path, "w") as f:
                                    f.write(yesterday_format)

    #delete downloded text files for privacy
    with open('channels.txt', "w") as f:
        f.write('')

    with open('guilds.txt', "w") as f:
        f.write('')
    

