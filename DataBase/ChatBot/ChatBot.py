import random

Hello = ('hello','hey', 'hi')

reply_Hello = ('Hello Sir, how are you today?',
            "Good day sir",
            "welcome back sir",
            "Hello Sir , Nice To talk to You Again.")

Bye = ('bye','exit','sleep','go', 'goodbye')

reply_bye = ('Bye Sir.',
            "Sure sir, good bye",
            "Of course sir, see you next time",
            "Good bye sir")

How_Are_You = ('how are you','are you fine', 'how are you doing')

reply_how = ("Excellent sir, thanks for asking.",
            "Absolutely Fine sir.",
            "I am Fine, thank you.")

thanks = ('thank you', 'thanks')

reply_thanks = ('Of course sir, any time',
                'My pleasure')

nice = ('nice','good', 'good to know')

reply_nice = ('Thank you sir.',
            "Thanks To You sir.")

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform a Varieties Of Tasks, What do you want me to do?',
            'I Can Call Your GirlFriend if you want.',
            'I Can Message Your Mom That You Are Not Studying for example.',
            'I Can program an alarm for you, if you want',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !',
            'I can put on a reminder so you dont forget stuff as you always do')

sorry_reply = ("Sorry sir, That's Beyond My Abilities .",
                "I'm Sorry sir, I'm affraid I Can't Do That.",
                "Sorry sir, That's Above Me.")

def ChatterBot(Text):

    Text = str(Text)

    for word in Text.split():

        if word in Hello:

            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_bye)

            return reply

        elif word in How_Are_You:

            reply_ = random.choice(reply_how)

            return reply_
        
        elif word in nice:
            
            reply = random.choice(reply_nice)
            
        elif word in thanks:
            
            reply = random.choice(reply_thanks)

        elif word in Functions:

            reply___ = random.choice(reply_Functions)

            return reply___

        else:

            return random.choice(sorry_reply)
