__module_name__ = "HiEveryone"
__module_version__ = "0.1"
__module_description__ = "Says 'Hi' to everyone on the current channel"
import hexchat
import string
username =  hexchat.get_info("nick")
def cmd_hiall(str, str1, str2):
	"This is basicaly everything"
	temp = 'Hi '
	list = hexchat.get_list("users")
	username =  hexchat.get_info("nick")
	if list:
    		for i in list:
				if(i.nick != username):
					temp = temp + i.nick + "; "
	hexchat.command("say " + temp)
	return
hexchat.hook_command("hiall", cmd_hiall)
