# Discord-bot-mumbot
Mumbot says Hi, (username) when you type ?Hi in the chat. Mumbot joins a voice channel and plays, pauses, resumes and stops music by typing commands like ?play (link).

To get the bot code to work, go to Discord developer portal, create a bot app and give it Administrator permissions, add the bot to your desired channel.
You'll get the key for your bot from the Discord developer portal so paste that to the code.
You'll also need to download the ffmpeg.exe file from https://www.gyan.dev/ffmpeg/builds/ for this project it's ffmpeg-git-full.7z file. Extract the file and under bin you can find ffmpeg.exe. You can just rename the bin folder with ffmpeg and add that to an easy location. I added it under C: so it's easy to find.
Then edit the system environment variables and under system variables go to Path and edit. Press new and add your ffmpeg location. For me it was C:\ffmpeg\bin but it depends on where you put the file. 
For this project you'll also need to install Discord and youtube_dl using pip. 
After setup and when you've added the bot to a server and the bot's key to the code, it should work.
