from MQLibrary import MQLibrary

message = MQLibrary().getMessage('127.0.0.1', 61613, 'admin', 'admin', 'python.queue')

print (message)