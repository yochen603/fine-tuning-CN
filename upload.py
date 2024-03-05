from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("output.jsonl", "rb"),
  purpose="fine-tune"
)