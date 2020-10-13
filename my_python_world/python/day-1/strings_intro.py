# Various string function concepts used

message = 'Hello World'
print(message)
message = 'Ithi\'s Universe'
print(message)
msg1_quote = '"Quote 1 -Ithi"'
print(msg1_quote)
print(len(message))
print(message[6:])
print(message.lower())
print(message.count('W'))
print(message.find('World'))
new_msg = message.replace('World','Universe')
print(new_msg)
greeting = 'Hello'
name = 'Michael'
message_grt = greeting + ', '+ name +'. Welcome!'
print(message_grt)

message_grt = '{}, {}. Welcome!'.format(greeting,name)
print(message_grt)

message_grt = f'{greeting}, {name}. Welcome!'
print(message_grt)

'''print(dir(name))
print(help(str))
print(help(str.lower))'''

