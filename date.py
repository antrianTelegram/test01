xx=isinstance(command, datetime.date)
                if xx==True:
                    yy=datetime.date(command)
                    formatdate ="%a %d %b %Y"
                    b=command.strftime(formattime)
                    bot.sendMessage(chat_id, "%s\n%s"%(b,yy))
                elif xx==False:
                    bot.sendMessage(chat_id, "Sorry i don't understand\n\n%s"%menu)
