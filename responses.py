import random
def get_response(message: str) -> str:
    p_message = message.lower()

    if message == 'hello':
        return 'Whats up!'
    
    if message == 'I\'m sad':
        return "You're an amazing person, try smiling more often!"
    if message == 'roll':
        return str((random.randint(1,6)) + random.randint(1,6))
    if p_message == '!help':
        return '`This is a message you can modify`'
    
    return 'I didn\'t understand what you wrote, try typing "!help".'



