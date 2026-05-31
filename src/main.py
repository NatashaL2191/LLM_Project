import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
import click

load_dotenv()

class Resume:
  def __init__(self, file, name):
    self.name = name
    self.file = file
    pass




class LLM_CLient(Resume):
  '''Class defining the LLM CLient capabilities'''
  def __init__(self,file, m):
    self.file = file
    self.client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key = os.getenv("OPENROUTER_API_KEY")
    )



  def edit_resume(file):
    '''Create function to open and write new section into Resume'''
    with open(file) as f:
      print(f.read())
    with open(file, "w") as f:
      f.write(input)
  def add_to_section(section, description):
    pass

  
  def step(self, user_input: str) -> str:
      """Runs a single reasoning and execution cycle."""
      self.memory.append({"role": "user", "content": user_input}) 
    # First API call with reasoning
      response = self.client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
                {
                  "role": "user",
                  "content": "How many r's are in the word 'strawberry'?"
                }
              ],
        extra_body={"reasoning": {"enabled": True}}
      )
      # Extract the assistant message with reasoning_details
      response = response.choices[0].message

    # Preserve the assistant message with reasoning_details
      messages = [
        {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
        {
          "role": "assistant",
          "content": response.content,
          "reasoning_details": response.reasoning_details  # Pass back unmodified
        },
        {"role": "user", "content": "Are you sure? Think carefully."}
      ]

      # Second API call - model continues reasoning from where it left off
      response2 = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=messages,
        extra_body={"reasoning": {"enabled": True}}
      )





@click.command()
@click.option("--name", Prompt="Enter your preferred name")
def main():
   click.echo('Hello! What would you like to do?')
    
if __name__ == '__main__':
    main()