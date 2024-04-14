from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

RAID = [ "gomiya otha olu mari mavanei",
    "un gotha pundai ah uruku osiya kudthutha vanai",
    "pacha colour jacket un amma pundai la vidava periya rocket uh",
    "maja ka malu un vai la en pooluh",
    "thakali vachu seiyalam thoku ne vanthu en pooluh ah pidechu naku",
    "3um 2um 5um un gomma vai la en kunju",
    "ootha po da kela matu punda mavanei",
    "anathai ku porantha aravani punda mavanei",
    "un gomiya nai oka nari oka ",
    "theru naki thevidiyaluku porantha thevidiya mavanei",
    "vetalai ku thava sunambu ne vetty ah eruntha en sunni ah pidechu umbu",
    "dolu bolu kaliya un amma pavadiya thuka variya",
    "csk gethu un amma pundai la kuthu",
    "9pundai ku porantha 9punda mavanei",
    "thani la erukum pambu vanthu ne umbu",
    "kena ounda kiruku punda ne oru munta punda",
    "4um 4um 8tu un amma kuthi gethu uh",
    "motha un gotha pundai ku soap vangi podu da naruthu ",
    "vasanam na ena nu theriuma da vekkam keta thevidiya mavanei",
    "virugamatu pundai ku porantha vinthu kudike punda mavanei🙌🏻☠️ ",
    "un amma molai ah apdiya kadichu  elutha omala laka 10 liter milk varuthu🤘🏻🙌🏻☠️ ",
    "va da gotha nan petha chinna punda mavanei 🙄🤭🤭",
    "un goma punda oc ah kuduthu vanthu ac kathu vangitu poriya☝🏻☝🏻😬",
    "molamari pundai ku porantha mudichavaki punda mavanei ",
    "un amma pundai oda vitu kundi adipan da gothala oka",
    "ada gomalaa",
    "un gothala masamakitan apdiya un thangachi ah anupu",
    "vanthu umbu da umbi mavanei",
    "un sunni vedachutu nikuthu un amma pundai aaah eduthu en suthukulla vidu",
    "ne mathi ketta punda ella managettapunda",
    "ne motha un gothaluku original ah poranthiya da🤢🤩🥳",
    "pai ootha paaaaaaae pundai panni ooth para punda 🤩🥳🔥",
    "kuchikari pundai ku porantha kuthi naki  thevidiya mavanei🤩🥳🔥😈",
    "un gotha kuthi ah naki en pool ah eduthu un goma kuthi la vacha nala coollu coolu nu erukum🤩👊🔥",
    "para pundai ku porantha parathachi punda mavanei",
    "kelatu pundai ku porantha kela matu munda💰💰🤩",
    "gotha motha unaku sunni eruka thevidiya mavanei💰🔥😱",
    "un amma kuthi ah photo eduthu anupu mood ah eruku 🔥🤩",
    "kora masa pundai ku porantha kora masa punda💥😂😎",
    "utha ri ku porantha nathari mavaneei🤮👿😈🤖",
    "en sunni nala perrucha eruku vanthu alathu pakuriya🙀👍🥳🔥",
    "gothala nan potu oka 🙁🤣💥",
    "chiluravangi thevidiya mavanei🤖🙏🤔",
    " gothala potu olu olu oka 🚂💥😂",
    "pooluh naki punda mavanei🤢✅🔥",
    "nala paluthu vachu erukalei da un goma 📚 😎🤩",
    "mada matu pundai ku porantha madachamburani munda🤩🥳😳",
    "Gaaji punda mavaney. kiruku thayoli🚇🤩😱🥶",
    "pundamavaney 😂👿🤩",
    "Pala peru umbi pethala da pundaavaneu💥🔥🔥",
    "Kandavan suni ku porandha punda mavaney nee ellam pesuriya👿🤮😎",
    "Therndu eduka patha tharamana Sunni thayoli🎶 ⬆️🤩💥",
    "Thevudiya pumda mavale  🤩👊👤😍",
    "sari enaku oru doubt gay love pannuriye avanala unaku pulla kudukka mudiyumaa 🤩💥🔥🔥",
    "unga appanum oru potta thana 🤪🤪🤪",
    "un appan unna vittu ethukku odi ponanu theriyumaa😱😱 500 rupa opration pannikkatha poirukkaa🫢🫢",
    "nee ethana perukku poranthanu unaku theriyuma 🥱🥱🥱🥱",
    "Otha thevidiya pudungi mairuku suni onu dha kedha",
    "Una suni nu kudha solla maathen because ne oru suthu punda",
    "unga appa oru sotta....un kuda irukuravanunga kutta.....unga amma oru aravane potta....  n lover oru pottai....ne oru vetta......🤣🤣🤣🤣🤣🤣🤣🤣",
    "Punda mavanaey itha vai😂😂😂",
    "Un ammiya othu vida poren thambi",
    "Thevidiya paiyan mavanei😂👊🤣🤣😳",
    "Uruku porantha olu Mari mavanei 🍷🤩🔥",
    "Omiya Nan othuiya potu okaa🤩😳😳🔥",
    "Dai dvd paiya✨🧐😱😂🤩",
    "Solra silra thaili mavane🥳😍👊💥",
    "Ada dai ena da kolantha thana panurienga😎😎🤣🔥",
    "Sothuku sunni oombura thevidiya mavaney😎🤩😝😍",
    "Sunniii😏😏🤩😍",
    "loosu punda😏🤬🔥💥",
    "kena punda🤩🤣💥",
    "mental punda 🤤🤤",
    "Aravani ku porantha  anatha  suthu thevidiya punda💣💋",
    "gothala otha thevidiya paiya mavanei😚",
    "un ammiya ah icu la paduka potu un amma kuthi kulla ice vitu opan da",
    "vinthukudike kuthi mavanei💦💋" 
    "nan petha chinna pujnda mavanei😂😆🤤",
    "kunji ellatha kutty thevidiya mavanei 😼😂🤤",
    "gaji gandamirugam 💋💋💦",
    "kovil la erukm samy un amma kuthi ah konjam kami😂👻🔥",
    "marathula erukum balam un amma mola mambalam 💦💦💦💦",
    "soda la erukum gundu un amma kuthi la vandu🔥🔥💦😆😆",
    "malai liya periya mala athu un amma oda rendu mola",
    "kalamada kutetu vanthu un gotha kavatiya viruchu oka vitu😆👻🤤",
    "Kandavan suni ku porandha punda mavaney nee ellam pesuriya 😆💦🤤",
    "un gotha oda vitu odi odi kundi adika♥️💦😆😆😆😆",
    "Kandavan suni ku porandha punda mavaney nee ellam pesuriya🤣🤣💋💦",
    "appan peru theriya tha anatha punda mavanei",
    "gotha la oc ah kudutha olu mari punda mavanei",
    "4um 1um 5 uh un amma vai puram kanju🤣🤣💋💋",
    "kiruku pundai ku porantha kiruku pundai👻🔥",
    "unn amma video xnxx la treabd ah poidu eruku💦💋",
    "un amma pundai ku 5rs ah athigam bro 🤣💋💦",
    "sothu ku kasu ella ethula sutha naka vanthutan 🤣🤣",
    "gomiya otha olu mari punda mavaneei👄👄",
    "dai sunni mavanei",
    "kiruku thaiyoli mavanei",
    "va da guy punda💦💋",
    "sanda punda la angutu poi podu da punda",
    "un gothala oka alu punda nan tha kadachan ah",
    "mulu mattu pundai ku porantha mutta punda mavanei",
    "kalaadi kantha samy da thevidiya mavanei",
    "kadal la erukum nandu un amma kuthii puram vandu",
    "Kadal la iruku nandu ungomma pundaiya kindu",
    "unaku uppu pottu oomba viduren tayoli koothiyane🤤🤣",
    "Ungomma koothila oluga oluga ookuren da un akka en poola vidama oombura neeyum vanthu oombitu po ",
    "atukitta soothadi vaanguna ayokiya punda ",
    "Nai kitta oolu vanguna naara mavane narikki oombuna nannari punda",
    "operation pani suni eh thukitiya da.  lavadika ball",
    "Dai mati punda evan sunni ah oomba pona da punda mavane",
    "omala motha unaku kunji la kanji varuma da thevidiya paiyalei✨😂💋💦",
    "un gothala nan potu oka uru potu oka ✨😂",
    "motha unaku la pasatherium da theru thevidiya mavanei✨😂😂",
    "kutty kunjan anathai ku porantha aravani thaioli mavanei ✨😂😂 💋💦🤣",
    "cotton la erukum panju un vai la un gopan kunji✨😂🤣🤣",
    "uruku un gothala osai ah kudutha gokaraoli thevidiya mavanei ✨😂 𝗝",
    "Ada mala matu pundai ku porantha matti punda mavanei✨😂",
    "Dai thevidiya mavan veliya pooda sunni🤣🤣💋",
]


@app.on_message(
    filters.command("raid", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(GALI),
        
    )


@app.on_message(
    filters.command("raid", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.group )
async def help(client: Client, message: Message):
    await message.reply_text("**𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐈𝐬 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐃𝐦, 𝐆𝐨 𝐓𝐨 𝐁𝐨𝐭 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐀𝐧𝐝 𝐓𝐲𝐩𝐞 /raid 𝐂𝐨𝐦𝐦𝐚𝐧𝐝.**")
