class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π,
Β© π΄πππ ππππππ π
Β© <a href =https://t.me/lord1of5darkness9>π·πππ ππ π―πππππππ</a>"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έ
β― γπ²ππ΄π°ππΎπγ   : <a href=https://t.me/mwpro11>π·πππ ππ π―πππππππ</a>
β 
β― γπ»πΈπ±ππ°ππγ   : <a href=https://docs.pyrogram.org/>πΏπππΎπΆππ°πΌ</a>
β 
β― γπ»π°π½πΆππ°πΆπ΄γ  : <a href=https://www.python.org/>πΏπππ·πΎπ½ πΉ</a>
β 
β― γπ³π°ππ° π±π°ππ΄γ : <a href=https://www.mongodb.com/>πΌπΎπ½πΆπΎ π³π±</a>
β 
β― γπ±πΎπ ππ΄πππ΄πγ: <a href=https://id.heroku.com/login>π·π΄ππΎπΊπ</a>
β 
β― γπ²πΎπ³π΄π³ π±πγ  : <a href=https://github.com/LordSA>π»πΎππ³ ππ°</a>
β 
β― γππ΄πππΈπΎπ½γ   : v5.0.9 [ π±π΄ππ° ]
β«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έβ«·β«Έ"""
    SOURCE_TXT = """<b>γπ½πΎππ΄γ:</b>
β― γππ°π»πΊγ  - π΄ππ΄π½ ππ΄π°πΆπ΄ππ πΈπ π° πΏππΈππ°ππ΄ π±πΎπ ππΎπ π²π°π½ πππ΄ πΌπ΄ π±ππ πΌπ ππΎπππ²π΄ πΈπ π½πΎπ π°ππ°πΈπ»π°π±π»π΄
β― γππΎπππ²π΄γ- <a href=https://t.me/mwmoviespro>π΄ππ΄π½ ππ΄π°πΆπ΄ππ</a>  

<b>ππ’π³π’π©π¬π­π’π―:</b>
- <a href=https://t.me/lord1of5darkness9>π·πππ ππ π―πππππππ</a>"""
    WHOIS_TXT ="""<b>α΄‘Κα΄Ιͺs α΄α΄α΄α΄Κα΄</b>
Ι΄α΄α΄α΄:- Ι’Ιͺα΄ α΄ α΄ α΄sα΄Κ α΄α΄α΄α΄ΙͺΚs
β’/whois : Ι’Ιͺα΄ α΄ α΄ α΄sα΄Κ πα΄ΚΚ α΄α΄α΄α΄ΙͺΚs"""
    MANUELFILTER_TXT = """Κα΄Κα΄: <b>π΅πΈπ»ππ΄ππ</b>

β― ?ΙͺΚα΄α΄Κ Ιͺs ππ·π΄ π΅π΄π°ππππ΄ ππ΄ππ΄ πππ΄ππ π²π°π½ ππ΄π π°πππΎπΌπ°ππ΄π³ ππ΄πΏπ»πΈπ΄π π΅πΎπ π° πΏπ°πππΈπ²ππ»π°π πΊπ΄πππΎππ³ π°π½π³ πΌπΎππΈπ΄ ππΎππ»π³ ππΈπ»π» ππ΄ππΏπΎπ½π³ ππ·π΄π½π΄ππ΄π π° πΊπ΄πππΎππ³ πΈπ π΅πΎππ½π³ ππ·π΄ πΌπ΄πππ°πΆπ΄

<b>Ι΄α΄α΄α΄:</b>
1. α΄Κα΄Ι΄ Κα΄α΄Ι’α΄Κ sΚα΄α΄Κα΄ Κα΄α΄ α΄ α΄α΄α΄ΙͺΙ΄ α΄ΚΙͺα΄ ΙͺΚΚα΄Ι’α΄.
2. α΄Ι΄ΚΚ α΄α΄α΄ΙͺΙ΄s α΄α΄Ι΄ α΄α΄α΄ ?ΙͺΚα΄α΄Κs ΙͺΙ΄ α΄ α΄Κα΄α΄.
3. α΄Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄s Κα΄α΄ α΄ α΄ ΚΙͺα΄Ιͺα΄ α΄? 64 α΄Κα΄Κα΄α΄α΄α΄Κs.

<b>α΄α΄α΄α΄α΄Ι΄α΄s α΄Ι΄α΄ α΄sα΄Ι’α΄:</b>
β’ /filter - <code>α΄α΄α΄ α΄ ?ΙͺΚα΄α΄Κ ΙͺΙ΄ α΄Κα΄α΄</code>
β’ /filters - <code>ΚΙͺsα΄ α΄ΚΚ α΄Κα΄ ?ΙͺΚα΄α΄Κs α΄? α΄ α΄Κα΄α΄</code>
β’ /del - <code>α΄α΄Κα΄α΄α΄ α΄ sα΄α΄α΄Ιͺ?Ιͺα΄ ?ΙͺΚα΄α΄Κ ΙͺΙ΄ α΄Κα΄α΄</code>
β’ /delall - <code>α΄α΄Κα΄α΄α΄ α΄Κα΄ α΄‘Κα΄Κα΄ ?ΙͺΚα΄α΄Κs ΙͺΙ΄ α΄ α΄Κα΄α΄ [α΄Κα΄α΄ α΄α΄‘Ι΄α΄Κ α΄Ι΄ΚΚ]</code>"""
    BUTTON_TXT = """Κα΄Κα΄: <b>Κα΄α΄α΄α΄Ι΄s</b>πππ‘πππΏπΏπΎπππΈπ½πΆγ- π΄ππ΄π½ ππ΄π°πΆπ΄ππ Supports both url and alert inline buttons.

<b>π½πΎππ΄:</b>
1. ππππππππ π πππ πππ πππππ π π’ππ ππ ππππ πππππππ π ππππππ πππ’ πππππππ, ππ πππππππ ππ πΌππππππππ’.
2. πΌ ππππππππ π±ππππππ π πππ πππ’ ππππππππ πΌππππ ππ’ππ.
3. π±ππππππ ππππππ ππ ππππππππ’ ππππππ ππ πππππππ π ππππππ

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mwpro2_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """π·π΄π»πΏ: <b>π°πππΎ π΅πΈπ»ππ΄π</b>

<b>π½πΎππ΄:</b>
1. πΌπππ ππ πππ πππππ ππ π’πππ πππππππ ππ ππ'π πππππππ.
2. ππππ ππππ ππππ π’πππ πππππππ ππππ πππ ππππππππ πππππππ, ππππ πππ ππππ πππππ.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Movie World

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
β’ /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    TGRAPH_TXT = """Help: <b>TELEGRAPH & PASTE</b>

<b>NOTE:</b>
β’ IMDb should have admin privillage
β’ These commands works on both pm and group
β’ These commands can be used by any group member

<b>Commands and Usage:</b>

β’ /tgmedia or /tgraph - <code>upload supported media (within 5MB) to telegraph.</code>"""
    STICKER_TXT = """πππ‘π₯ ππ€π§ ππ©πππ ππ§ ππ
    
β’ ππ¨πππ

To Get Sticker ID
 
 β­ ππ€π¬ ππ€ ππ¨π
  
β Reply To Any Sticker [/stickerid]"""
    RESTRIC_TXT = """Help: <b>Restrictions</b>

<b>What is this?</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
β’ /ban - ban a user.
β’ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /mute - mute a user.
β’ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""
    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
β’ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
β’ /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works only group.
β’ These commands can be used by Only admin."""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
β’ /paste [text] - paste the given text on Pasty
β’ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
β’ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""
    OTH_TXT = """EXTRA BUTTONS FOR USE...."""
    FILT_TXT = """ALL FILTER BUTTONS ARE HERE"""
    MANEGER_TXT = """Do You Think I can Manage Your Group Then Don't Think Use My Features"""
    TEXTWORK_TXT = """Text Editing and Link Editing or Regeneration"""
    PINGS_TXT ="""<b>π Ping:</b>
Helps you to know your ping πΆπΌββοΈ

<b>Commands:</b>

β’ /alive - To check you are alive.
β’ /help - To get help 
β’ /ping - To get your ping 
β’ /repo - Source Code.

<b>πΉUsageπΉ :</b>

β’ This commands can be used in pms and groups
β’ This commands can be used buy everyone in the groups and bots pm
β’ Share us for more features"""
    TORRENT_TXT = """<b>Torrent Search</b>

<b>Commands and Usage:</b>
β’ /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
β’ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    MEMES_TXT = """Help: <b>FUN</b>

Some dank memes for fun or whatever!

<b>Commands and Usage:</b>
β’ /throw or /dart - tπ mπΊππΎ drat 
β’ /roll or /dice - roll the dice 
β’ /goal or /shoot - to make a goal or shoot
β’ /luck or /cownd - Spin the Lucky
β’ /runs strings

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    INFO_TXT = """Help: <b>Json</b>

<b>Commands and Usage:</b>
β’ /json - <code>get the json details of a message.<code>
<code> /id & /info is not from json it's just added to this.<code>

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TTS_TXT = """π·πππ: <b>πππ‘π ππ ππππππ</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
β’ /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
β’ /song  (songname) - download song from yt servers.
β’ /video (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
β’ /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
β’ /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
β’ Only Digits Are Allowed
β’ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
β’ /share (text or reply to message)

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""
    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """βYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """π? Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """βI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
