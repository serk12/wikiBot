import telebot
import wikipedia

API_TOKEN = 'token'

bot = telebot.TeleBot(API_TOKEN)

def del_comand(command, mes):
    return mes.text.replace('/' + command + ' ', '')

explein = "this bot search in wikipedia www.wikipedia.org \nyou can ask me by sending these commands: \n"

commands = {'help' : "ask for help",
           'info' : "search the summary of a argument",
           'lenguage' : "set the lenguage of the search",
           'random' : "get a random page"}

iso_639_1 = "aa ab ace ady af ak als am an ang ar arc arz as ast av ay az azb ba bar bat-smg bcl be be-tarask bg bh bi bjn bm bn bo bpy br bs bug bxr ca cbk-zam cdo ce ceb ch cho chr chy ckb co cr crh cs csb cu cv cy da de diq dsb dv dz ee el eml en eo es et eu  ext fa ff fi fiu-vro fj fo fr frp frr fur fy ga gag gan gd gl glk gn gom got gu gv ha hak haw he hi hif ho hr hsb ht hu hy hz ia id ie ig ii ik ilo io is it iu ja jbo jv ka kaa kab kbd kg ki kj kk kl km kn ko koi kr krc ks ksh ku kv kwy la lad lb lbe lez lg li lij lmo ln lo lrc lt ltg lv mai map-bms mdf mg mh mhr mi min mk ml mn mr mrj ms mt mus mwl my myv mzn na na nap nds nds-nl ne new ng nl nn no nov nrm nso nv ny oc om or os pa pag pam pap pcd pdc pfl pi pih pl pms pnb pnt ps pt qu rm rmy rn ro roa-rup roa-tara ru rue rw sa sah sc scn sco sd se sg sh si simple sk sl sm sn so sq sr srn ss st stq su sv sw szl ta te tet tg th ti tk tl tn to tpi tr ts tt tum tw ty tyv udm ug uk ur uz ve vec vep vi vls vo wa war wo wuu xal xh xmf yi yo za zea zh zh-classical zh-min-nan zh-yue zu"

@bot.message_handler(commands = ['start', 'help'])
def send_help(mes):
    help_text = explein
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(mes.chat.id, help_text)
    
@bot.message_handler(commands = ['info'])
def smallInfo(mes):
    get = del_comand('info', mes)
    search = wikipedia.summary(get)
    bot.send_message(mes.chat.id, search)
    
@bot.message_handler(commands = ['lenguage'])
def lenguage(mes):
    get = del_comand('lenguage', mes)
    if (iso_639_1.find(get) != -1):
        wikipedia.set_lang(get)
        bot.send_message(mes.chat.id, 'lenguage set to: ' + get)
    else:
        bot.send_message(mes.chat.id, "this lenguage don't exist")
    
bot.polling()