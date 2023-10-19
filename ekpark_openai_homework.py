import os
import time
import json

import openai

from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("ORGANIZATION")


# Initialize the saved_messages list
saved_messages = [

]

def query_prompt(messages: []):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=True
  )

  return response

def read_file_content(filename):
    """Read the content of the file with the given filename using 'utf-8' encoding."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
   
    # 가상환경에서 실행하는 경우 경로를 가져옴 
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the files and append their contents to the list as dictionaries
    for i in range(1, 6):  # Loop from 1 to 5
        filename = os.path.join(script_dir, "data", f"review{i}.txt")
        
        try:
            content = read_file_content(filename)
            message_dict = {
                f"role{i}": i,
                f"content{i}": content
            }
            saved_messages.append(message_dict)
            print(f"Contents of {filename} added to saved_messages.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except UnicodeDecodeError:
            print(f"Failed to decode {filename}. Ensure it is saved in utf-8 format.")

    # Optional: print out the saved messages to verify
    for message in saved_messages:
        for key, value in message.items():
            print(f"{key}: {value}\n")

if __name__ == "__main__":
    main()