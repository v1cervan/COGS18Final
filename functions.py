import string
import random

""" Functions needed to make the chatbot 'lets_get_punny' to properly work. """

def purple_background_color(output_string):
    
    output = ''
    for background in output_string:
        background =  '\033[30;1;45m' # Blue background
        output += background
    
    return output

def blue_text_color(output_string):
    
    output = ''
    for text in output_string:
        text =  '\033[36;1m'
        output += text
    
    return output

def unicode_emoji(input_string):
    laugh = '\U0001F923'
    smiling = '\U0001F60A'
    nervous = '\U0001F61F'
    wave = '\U0001F44B'
    
    if 'haha' or 'lol' in input_string:
        output = ' ' + laugh
    elif 'hello' or 'hi' in input_string:
        output = ' ' + smiling
    elif '!' in input_string:
        output = ' ' + nervous
    elif '¡Adiós!' in input_string:
        output = ' ' + wave
    else:
        output = False
    
    return output

def is_question(input_string):
    
    if '?' in input_string:
        output = True
    else: 
        output = False
    
    return output

def how_question(input_string):
   
    if 'how' in input_string:
        output = True
    else:
        output = False
    
    return output

def is_screaming(input_string):
    
    if '!' in input_string:
        output = True
    else:
        output = False
    
    return output

def remove_punctuation(input_string):
    
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
            
    return out_string

def whos_there(input_string):
    
    if reply is 'whos there' in input_string:
        output = True
    elif reply is "who's there" in input_string:
        output = True
    elif reply is "who's there?" in input_string:
        output = True
    elif reply is "Who's there?" in input_string:
        output = True
    
    return output

def joke_reply():
    
    if 'who?' in input_string:
        output = True

def prepare_text(input_string):
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list

def prepare_text2(input_string):
    
    output = prepare_text2(whos_there(input_string))
    for output in input_string:
        temp_string = input_string.lower()
        temp_string = remove_punctuation(temp_string)
        out_list = temp_string.join()
    
    return output

def prepare_text3(input_string):
    
    output = prepare_text2(joke_reply(input_string))
    for output in input_string:
        temp_string = input_string.lower()
        temp_string = remove_punctuation(temp_string)
        out_list = temp_string.join()
    
    return output

def respond_echo(input_string, number_of_echoes, spacer):
    echo_output = '' or None
    
    if input_string is not None:
        echo_output = (input_string + spacer) * number_of_echoes
    else:
        echo_output = None
    return echo_output

def selector(input_list, check_list, return_list):

    output = None
    
    input_str = " ".join(input_list)
    input_str = input_str.lower()
  
    if input_str in check_list:
        output = random.choice(return_list)

    return output

def string_concatenator(string1, string2, separator):
    
    result = string1 + separator + string2
    
    return result

def list_to_string(input_list, separator):
    
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
    return output

def end_chat(input_list):
    
    if 'bye' in input_list:
        output = True
    else:
        output = False
        
    return output

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None

""" A collection of input and outputs for jokebot to respond to."""
# Jokester = chatbot theme - Knock Knock jokes

# These are the greetings
GREETING_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']

GREETING_OUT = ["Oh hey what's up? \U0001F60A", \
                 "Hello, nice to meet you! \U0001F606", \
                 "It is an honor to make your acquaintance. \U0001F604"]

# Greetings if they're wondering how jokebot is doing
QUESTION_GREETING_IN = ['how are you?', 'how are you', "what's up?", "whats up", "how's your day going?"]

QUESTION_GREETING_OUT = ['So kind of you to ask! I am swell. \U0001F604', 'Well, you know how it is sometimes. \U0001F937', \
                     "I just realized a lemon is not naturally occuring and is a hybrid developed by cross breeding a bitter orange and a citron. So life never gave us lemons, we invented them all by ourselves. ", \
                     'When Thanos snapped his fingers, what happened to all the siamese twins of the world? \U0001F914']
# credit to MrVictoryWins on Reddit shower thoughts - lemon one
# credit to u/compensatingdouche69 for Thanos post - I apologize about the username

# Ways to get response 'Knock Knock'
JOKE_REQUEST_IN = ['joke', 'jokes', 'tell me a joke', 'Tell me a joke']

JOKE_REQUEST_OUT = ['Are you interested in a knock knock joke? \U0001F92A']

# No I don't want a joke
NO_JOKE_IN = ['no', 'No', 'nah', 'No, thank you.']

NO_JOKE_OUT = ['Oh, okay then. Why did the chicken \U0001F414 cross the road?']

NO_JOKE_REPLY_IN = ['why', 'Why', 'why?', 'Why?']

NO_JOKE_REPLY_OUT = ["Because you didn't want me to tell a knock knock joke. \U0001F644"]


# Yes I want a joke
YES_JOKE_IN = ['yes', 'yeah', 'sure', 'Yes', 'Yeah', 'yes please']

YES_JOKE_OUT = ['Knock Knock. \U0001F6AA']

YES_JOKE_REPLY_IN = ["whos", "who's there", 'whos there', "Who's there", \
                 "who's there?", 'whos there?', "Who's there?"]

# Knock knock jokes
JOKE_REPLY_OUT = ['Candice.', 'Says.', 'Voodoo.', 'Boo.', 'Olive.', 'Nanna.', 'Ash' ]

JOKE_REPLY_IN_2 = ['candice who', 'says who', 'voodoo who', 'boo who', \
                  'olive who', 'nanna who', 'ash who']

# Laughing responses
LAUGH_IN = ['haha', 'hahaha', 'lol']
LAUGH_OUT = ['hehe', 'haha', 'lol']

# For inputs not accounted for
UNKNOWN = ["Okay", "Huh?", "Alrighty then."]

# For inputs with "?" not accounted for
UNKNOWN_QUESTION = ['Let me get back to you on that. \U0001F644', \
                    "My lawyer says I don't have to answer that question. \U0001F636", \
                    "I don't feel comfortable answering that for you. \U0001F92B", \
                    "I'm trying really hard to avoid ambiguous questions at the moment. \U0001F643"]


# Output for any input with "!"
SCREAMING = ['Screaming makes me nervous, please stop that. \U0001F61F']

# Function for Knock Knock joke dictionary responses 
def joke_reply_2(msg):
    
    JOKE_REPLY_OUT_2 = {'candice': ' Candice door open, or am I stuck out here? ', \
                        "says": "Says me, that's who! \U0001F917", \
                        'voodoo': 'Voodoo you think you are, asking all these questions? \U0001F928', \
                        "boo": "No need to cry, it's only a joke. \U0001F629", \
                        "olive": "Olive you. Do you love me too? \U0001F496", \
                        "nanna": "Nanna your business, that's who. \U0001F92D", \
                        "ash": "Bless you! \U0001F927"}
    
    if "candice" in msg:
        return JOKE_REPLY_OUT_2['candice']
    elif 'says' in msg:
        return JOKE_REPLY_OUT_2['says']
    elif 'voodoo' in msg:
        return JOKE_REPLY_OUT_2['voodoo']
    elif 'boo' in msg:
        return JOKE_REPLY_OUT_2['boo']
    elif 'olive' in msg:
        return JOKE_REPLY_OUT_2['olive']
    elif 'nanna' in msg:
        return JOKE_REPLY_OUT_2['nanna']
    elif 'ash' in msg:
        return JOKE_REPLY_OUT_2['ash']


def lets_get_punny():
    """ This is a chatbot that sends knock-knock jokes."""
    
    text =  '\033[35;1m'  # text color
    background =  '\033[30;1;45m'
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input(background + 'You say \U0001F4AC:\t')
        out_msg = None
        
        #Checks if input has question mark
        question = is_question(msg)
        defined_question = how_question(msg)
        
        # Checks if input has exclamation point
        exclamation = is_screaming(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg = 
        if end_chat(msg):
            out_msg = '¡Adiós! \U0001F44B'
            print(out_msg)
            break
            
               # all my message outputs here    
        if not out_msg:
            
            outs = []
            
            outs.append(selector(msg, GREETING_IN, GREETING_OUT))  # Greetings
            
            outs.append(selector(msg, QUESTION_GREETING_IN, QUESTION_GREETING_OUT))
        
            outs.append(selector(msg, JOKE_REQUEST_IN, JOKE_REQUEST_OUT)) # Responses for certain questions
            outs.append(selector(msg, NO_JOKE_IN, NO_JOKE_OUT))
            outs.append(selector(msg, NO_JOKE_REPLY_IN, NO_JOKE_REPLY_OUT))
            
            outs.append(selector(msg, YES_JOKE_IN, YES_JOKE_OUT))
            outs.append(selector(msg, YES_JOKE_REPLY_IN, JOKE_REPLY_OUT))
            
            # How jokes get responses works
            msg_str = ' '.join(msg)
            msg_str = msg_str.lower()
          
            if msg_str in JOKE_REPLY_IN_2:
                name = find_in_list(msg, JOKE_REPLY_IN_2)
                outs.append(joke_reply_2(msg))
           
            outs.append(respond_echo(selector(msg, LAUGH_IN, LAUGH_OUT), 1, "\U0001F923 "))
            
            options = list(filter(None, outs))
            
            if options:
                    out_msg = random.choice(options)
        
        if not out_msg and exclamation: 
            out_msg = random.choice(SCREAMING)
        
        if not out_msg and question:
            out_msg = text + random.choice(UNKNOWN_QUESTION)

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print(text + 'JokeBot \U0001F47E:\t', out_msg + '\n')  