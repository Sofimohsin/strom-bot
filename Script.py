import os
class script(object):
    #  
    START_TXT = """<b>Jᴀɪ sʜʀᴇᴇ ʀᴀᴍ 🚩 {} {},

✦ ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ʙᴏᴛ.
✦ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴡᴇʙ sᴇʀɪᴇs.
✦ ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ.

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href=https://t.me/moviehiap>ᴅʀᴀɢᴏɴ ʙᴏᴛᴢ 🤖</a></b>"""
    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href=https://t.me/moviehiap>ᴅʀᴀɢᴏɴ ʙᴏᴛᴢ 🤖</a></b>"""

    GSTART_TXT = """<b>ᴏᴋ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴊᴜsᴛ sᴛᴀʀᴛ ᴘᴍ</b>"""
    
    #MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""
    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🍁 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n🌟 {} \n\n🔍 ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ 🔎\n\n⚠️ ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ 👇</b>"""
    
    GROUP_TXT = """
<b>⍟ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢʀᴏᴜᴘs ᴍᴏᴅᴜʟᴇ ⍟</b>

<b>🍿  ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ.
🗣️  ʙᴏᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.
🚦  ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ.
🎬  ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇsᴛɪɴɢ ɢʀᴏᴜᴘ.</b>"""

    AVADS_TXT = """<b>🔰 Ad Placement Opportunity

Reach a wider audience at a minimal cost with impression-based ads!

✅ Pay only when your ad is displayed – no extra charges, no hidden costs!
✅ Maximize visibility while staying within budget.
✅ Perfect for businesses, brands, and services looking to expand their reach.

📌 Demo Available – <a href='https://telegra.ph/Ads-Placement-12-30'>Check out the screenshot for reference.</a>
📩 To place your ad, contact: <a href='https://t.me/Dg_shiva'>Shiva Charan</a>

🚫 Note: We do not accept ads for movie groups or channels.</b>"""
    
    ABOUT_TEXT = """<b>╔══❰ {} ❱═❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/{}'>{}</a>
║┣⪼👦ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Dg_shiva'>Shiva Charan</a>
║┣⪼❣️ᴜᴘᴅᴀᴛᴇ : <a href=http://t.me/moviehiap>ᴅʀᴀɢᴏɴ ʙᴏᴛᴢ 🤖</a>
║┣⪼📡 ʙᴏᴛ ꜱᴇʀᴠᴇʀ : <a href='https://t.me/moviehiap'>ᴠᴘs</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼📥 ᴅᴀᴛᴀʙᴀꜱᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : v4.8 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍</b>"""
    
    SUBSCRIPTION_TXT = """
<b>ʀᴇғᴇʀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ғʀɪᴇɴᴅs, ғᴀᴍɪʟʏ, ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ғᴏʀ {}

ʀᴇғᴇʀᴀʟ ʟɪɴᴋ - https://t.me/{}?start=reff_{}

ɪғ {} ᴜɴɪǫᴜᴇ ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅᴇᴅ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.

ʙᴜʏ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ - /plan</b>"""

    FILE_CAPTION = """ 
<b>🗂️ ɴᴀᴍᴇ :  <a href="http://t.me/dragonmoviesbot">{file_name}</a></b>"""
   
    IMDB_TEMPLATE_TXT = """
🍿 Title: {title}
🎃 Genres: {genres}
📆 Year: {release_date}
⭐ Rating: {rating} / 10</b>
"""
    

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs & ɪᴛ's ᴘʀɪᴄᴇs
</b>"""    
    
    HELP_TXT = """<b>ʜᴇʏ {},\n\n ʜᴇʀᴇ ɪꜱ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴇꜱ.</b>"""
    
    TELE_TXT = """<b>/telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ɪɴ ʙᴏᴛʜ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛ ᴘᴍ</b>"""
    
    RULES_TXT = """<b>✗ 𝐌𝐎𝐕𝐈𝐄/𝐒𝐄𝐑𝐈𝐄𝐒 𝐒𝐄𝐀𝐑𝐂𝐇 𝐑𝐔𝐋𝐄𝐒

◉ ᴀʟᴡᴀʏꜱ ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ/ꜱᴇʀɪᴇꜱ ɪɴ ᴇɴɢʟɪꜱʜ. ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴏᴛʜᴇʀꜱ ʟᴀɴɢᴜᴀɢᴇ.

◉ ᴀʟᴡᴀʏꜱ ᴜꜱᴇ ᴄᴏʀʀᴇᴄᴛ ꜱᴘᴇʟʟɪɴɢ. ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ʀɪɢʜᴛ ꜱᴘᴇʟʟɪɴɢ ꜰʀᴏᴍ ɢᴏᴏɢʟᴇ.

◉ ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ ʟɪᴋᴇ ᴛʜɪꜱ :- 
› ꜱᴀʟᴀᴀʀ 2023 ✔️ 
› ꜱᴀʟᴀᴀʀ ʜɪɴᴅɪ ✔️ 
› ꜱᴀʟᴀᴀʀ ᴍᴏᴠɪᴇ ❌ 
› ꜱᴀʟᴀᴀʀ ꜱᴏᴜᴛʜ ᴍᴏᴠɪᴇ ❌ 
› ꜱᴀʟᴀᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ ❌  

◉ ꜱᴇᴀʀᴄʜ ꜱᴇʀɪᴇꜱ ʟɪᴋᴇ ᴛʜɪꜱ :- 
› ᴠɪᴋɪɴɢꜱ ✔️ 
› ᴠɪᴋɪɴɢꜱ ꜱ01 ✔️ 
› ᴠɪᴋɪɴɢꜱ ꜱ01ᴇ01 ✔️ 
› ᴠɪᴋɪɴɢꜱ ꜱ01 ʜɪɴᴅɪ ✔️
› ᴠɪᴋɪɴɢꜱ ꜱᴇᴀꜱᴏɴ 1 ❌  
› ᴠɪᴋɪɴɢꜱ ᴡᴇʙ ꜱᴇʀɪᴇꜱ ❌   
› ᴠɪᴋɪɴɢꜱ ꜱ01ᴇ01 ʜɪɴᴅɪ ❌ 
› ᴠɪᴋɪɴɢꜱ ꜱ01 ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ ❌ 

◉ ᴅᴏɴᴛ ʀᴇ𝚀ᴜᴇꜱᴛ ᴀɴʏᴛʜɪɴɢ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ , ꜱᴇʀɪᴇꜱ , ᴀɴɪᴍᴇ.

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ - @moviehiap</b>"""
    
    ADMIN_CMD_TXT = """<b>
/premium
/premium_user
/add_redeem
/broadcast
/grp_broadcast
/remove_premium
/groups
/leave
/send
/stats
/deleteall
/delete
/getfile
/check_plan
/del_file
/deletefiles
/del_ads
/set_ads
/search
/channel
/invite
/index
/pm_search_off
/pm_search_on
/movie_update_on
/movie_update_off
</b>"""
    TTS_TXT="""
<b>😊 ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ 😊
    
/set_shortner - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ
/set_shortner_2 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰᴏʀ 𝟸ɴᴅ ᴠᴇʀɪꜰʏ
/set_time - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ
/set_log - ᴛᴏ ꜱᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴜꜱᴇʀꜱ ᴅᴀᴛᴀ
/set_tutorial - ᴛᴏ ꜱᴇᴛ 𝟷ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/set_tutorial_2 - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/set_caption - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰɪʟᴇ ᴄᴀᴘᴛɪᴏɴ
/set_template - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ
/fsub - ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ
/del_fsub - ᴛᴏ ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ
/show_fsub - ᴛᴏ ᴄʜᴇᴄᴋ ғsᴜʙ sᴛᴀᴛᴜs
/details - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟꜱ

ɪғ ʏᴏᴜ ᴅᴏ ᴀʟʟ ᴛʜɪs ᴛʜᴀɴ ᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴠᴇʀʏ ᴄᴏᴏʟ..</b>"""

    MONEY_TXT="""<b>🤑 ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴛʜɪs ʙᴏᴛ -

1:- ʏᴏᴜ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ.

2:- ᴍᴀᴋᴇ ᴛʜɪs <a href='https://t.me/{}'>{}</a> ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

3:- ᴄʀᴇᴀᴛᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ ᴀɴʏ sʜᴏʀᴛɴᴇʀ ʟɪᴋᴇ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴛʜɪs ʙᴇsᴛ sʜᴏʀᴛɴᴇʀ <a href='https://Arlinks.in/ref/shiva'>Arlinks</a>.

4:- ᴛʜᴇɴ sᴇᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴅᴇᴛᴀɪʟs ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ 👇

/set_shortner Arlinks.in 1ec5154e19e7e771b5987cf0952261f0b489125d

/set_shortner_2 arlinks.in 30fb79c81157036d36e76dca142ebfba6291c4a0

/set_tutorial https://t.me/

5:- ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log -100*******

ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ

💯 ɴᴏᴛᴇ - ᴛʜɪs ʙᴏᴛ ɪs ꜰʀᴇᴇ ᴛᴏ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ᴇᴀʀɴ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏɴᴇʏ.</b>"""

    
    SETTINGS_TEXT = """<b>~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ <a href=https://t.me/aimoviefilterbot>ᴄᴜsᴛᴏᴍɪᴢᴇ</a> ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

~ ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.

~ ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

Cᴏᴍᴍᴀɴᴅs & Usᴀɢᴇ :

• /reload - ʀᴇғʀᴇꜱʜ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs ʟɪꜱᴛ.
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.</b>"""

    HELP2_TEXT="""<b>/set_shortner - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Sʜᴏʀᴛᴇɴᴇʀ
/set_tutorial - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Tᴜᴛᴏʀɪᴀʟ
/set_caption - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
/fsub - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Fᴏʀᴄᴇ Sᴜʙꜱᴄʀɪʙᴇ
/set_template - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ
/details - Tᴏ Cʜᴇᴄᴋ Yᴏᴜʀ Vᴀʟᴜᴇs

/set_shortner_2 - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Sʜᴏʀᴛᴇɴᴇʀ [ Fᴏʀ Vᴇʀɪꜰʏ Mᴏᴅ ]
/set_log_channel - Tᴏ Sᴇᴛ Lᴏɢ Cʜᴀɴɴᴇʟ [ Fᴏʀ Vᴇʀɪꜰʏ Mᴏᴅ ]
/set_time - Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Sᴇᴄᴏɴᴅ Vᴇʀɪꜰɪᴄᴀᴛɪᴏɴ Tɪᴍᴇ.</b>"""

    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    REFER_TEXT = """ Hay Your refer link:\n\nhttps://t.me/{}?start=reff_{}\n\nShare this link with your friends, Each time they join,  you will get 1 refferal points and after 15 points you will get 7 day premium subscription."""

    REFER_TXT = """ Hay Your refer link:\n\nhttps://t.me/{}?start=reff_{}\n\nShare this link with your friends, Each time they join,  you will get 1 refferal points and after 15 points you will get 7  day premium subscription."""
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    RESTART_TXT = """<b>
📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """ᴊᴀʟᴅɪ ʏᴇʜᴀ sᴇ ʜᴀᴛᴏ !"""

    OLD_ALRT_TXT = """ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇs..sᴇɴᴅ ᴀ ɴᴇᴡ ʀᴇǫᴜᴇsᴛ.."""

    NO_RESULT_TXT = """<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🙄</b>"""

    NOT_AVAILABLE_TXT = """{}
ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ"""
    
    SERIES_FORMAT_TXT = """{}
    
ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ғᴏʀᴍᴀᴛ ᴡʀᴏɴɢ❌ 
ғᴏʟʟᴏᴡ ᴛʜɪs ғᴏʀᴍᴀᴛ 👇
Money heist S01E01
Money heist S01"""
    
    UPLOADED_TXT = """{}
    
ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴜᴘʟᴏᴀᴅᴇᴅ ✅
sᴇᴀʀᴄʜ 🔍 ᴀɢᴀɪɴ ᴀɴᴅ ɪɴᴊᴏʏ"""
    
    NOT_RELEASE_TXT = """{} 
    
ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ɴᴏᴛ ʀᴇʟᴇᴀsᴇ 
ᴘʟᴇᴀsᴇ🙏 ᴡᴀɪᴛ ᴛʜᴇ ʀᴇʟᴇᴀsᴇ ᴅᴀʏ"""
    
    NORSLTS = """
#NoResult
★ Gʀᴏᴜᴘ Nᴀᴍᴇ <b>: {}</b>(<code>{}</code>)
★ Tᴏᴛᴀʟ Usᴇʀs {}
★ Bᴏᴛ {}
★ Usᴇʀ <b>: {}</b>
★ Mᴇssᴀɢᴇ <code>{}</code>"""
    
    PMNORSLTS = """
#Pm_NoResult
★ Bᴏᴛ {}
★ Uᴇʀ <b>: {}</b>
★ Mᴇssᴀɢᴇ <code>{}</code>"""
    
    SPELL_TXT = """{} 
ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ ɴᴀᴍᴇ ɴᴏᴛ ᴍᴀᴛᴄʜ ᴀɴʏ sᴇʀɪᴇs ᴏʀ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ 
ᴘʟᴇᴀsᴇ ʀᴇǫᴜᴇsᴛ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ"""
    
    MVE_NT_FND = """<i>ᴡᴇ ᴅɪᴅ ɴᴏᴛ ғɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ᴡɪᴛʜ ᴛʜɪs ɴᴀᴍᴇ 🙅,
ᴛʜɪs ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ</i>..."""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗻𝗮𝗺𝗲.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 😞... 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 𝗱𝗶𝗱 𝘆𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 ?? 👇"""
    
    FONT_TXT= """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

<code>/font hi how are you</code></b>"""

    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ 😐
ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ 😊.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/2

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1st ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✅️...

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ❤️‍🔥...

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)

ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʟɪᴄᴋ ⇓</b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ‼️
ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛᴏᴅᴀʏ 🔋.

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/2

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪꜰɪᴇᴅ ꜰᴏʀ ᴛᴏᴅᴀʏ ☺️.
ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs 💥.

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)

ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʟɪᴄᴋ ⇓</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_{}_completed"""

    #PLANS

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>
    
❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

<a href='t.me/'>💁 Pʀᴇᴍɪᴜᴍ Pʀᴏᴏꜰꜱ </a> 

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs & ɪᴛ's ᴘʀɪᴄᴇs.</b>"""

    CPREMIUM_TEXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>
    
❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs & ɪᴛ's ᴘʀɪᴄᴇs.</b>"""

    PLAN_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>
    
❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ] 

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs & ɪᴛ's ᴘʀɪᴄᴇs.</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>👋 ʜᴇʏ {},
    
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 7 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 15₹

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>👋 ʜᴇʏ {},
    
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 49₹

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>👋 ʜᴇʏ {},
    
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 90 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 110₹

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 ʜᴇʏ {},
    
🏅 <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
⏰ 180 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 199₹

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>👋 ʜᴇʏ {},

💎 <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
⏰ 365 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 399₹

🏦 ᴜᴘɪ ɪᴅ ➩ <code>shivamcharan7773@okicici</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/Dg_shiva'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>shivamcharan7773@okicici</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""
    

