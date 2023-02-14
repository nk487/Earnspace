from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_MESSAGE = '''👋Hello, {}
 I am Mdiskshortx.in , Bulk Link Converter. I Can Convert Links Directly From Your mdiskshortX.in Account,
    
1. Go To 👉 https://Mdiskshortx.in/member/tools/api 


2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)

/api<space>API Key 
(See Example.👇)
Example:
/api 5bc1058c2060d4247a90a1cc1d2aa829918ba08a 

Anyone who want to use any other shortner instead of Mdiskshortner than contact at 👉 @mr_Rahul_tk (all shortners support avilable.).
'''


HELP_MESSAGE = '''
🔗 𝙞𝙛 𝙮𝙤𝙪 𝙙𝙤𝙣'𝙩 𝙠𝙣𝙤𝙬 𝙝𝙤𝙬 𝙩𝙤 𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙨𝙝𝙤𝙧𝙩𝙣𝙚𝙧 𝙖𝙣𝙙 𝙗𝙤𝙩 𝙏𝙝𝙚𝙣 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙢𝙚 :- @mr_Rahul_tk 

:-
'''


ABOUT_TEXT = """
💁 If you want any other changing in this bot

➕ Hit 👉 /header - set header text  more info.

➕ Hit 👉 /footer - set footer text and click on command check out more info.

➕ Hit 👉 /username - set username 
➕ Hit 👉 /banner_image - set banner img and click on command

➕ Hit 👉 /me - your account information and on|off all settings.

"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('🏠 𝗛𝗼𝗺𝗲', callback_data='start_command')
    ]
])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('❌ 𝗰𝗹𝗼𝘀𝗲', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('💁 𝗛𝗲𝗹𝗽', callback_data=f'help_command'),
        
    ],
        [
        InlineKeyboardButton('⚙️ 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀', callback_data='about_command'),
        InlineKeyboardButton('❤️ 𝗷𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹', url='https://t.me/mdisk_shortx')
    ],
            [
        InlineKeyboardButton('🔗 𝘆𝗼𝘂𝗿 𝘀𝗵𝗼𝗿𝘁𝗻𝗲𝗿 𝗔𝗽𝗶 ', url='https://mdiskshortX.in/member/tools/api'),
    ],


])


BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('🫥 Back', callback_data=f'start_command')
    ],

])

USER_ABOUT_MESSAGE = """
✳️ Shortener Website: {base_site}
✳️ {base_site} API: {shortener_api}
✳️ Username: @{username}
✳️ Header Text: {header_text}
✳️ Footer Text: {footer_text}
✳️ Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """✅To add or update your Shortner Website API, /shortener_api api
            
✳️Ex: /shortener_api 6LZq851sXofffPHugiKQq
            
✳️Shortener API of your preferred shortener API.
✳️Current Website: {base_site}
✳️Current Shortener API: {shortener_api}"""

HEADER_MESSAGE = """✅Reply to the Header Text You Want
✳️This Text will be added to the top of every message caption or text
✳️To Remove Header Text: /header remove"""

FOOTER_MESSAGE = """✅Reply to the Footer Text You Want
✳️This Text will be added to the bottom of every message caption or text
✳️To Remove Footer Text: /footer remove"""

USERNAME_TEXT = """✅Current Username: {username}
✳️Usage: /username your_username
✳️For just removing the username from the post: 
/username none
✳️This username will be automatically replaced with other usernames in the post
✳️To remove current username, /username remove"""

BANNER_IMAGE = """✅Current Banner Image URL: {banner_image}
✳️Usage: /banner_image image_url
✳️This image will be automatically replaced with other images in the post
✳️To remove custom image, /banner_image remove
✳️Eg: /banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png"""
