import os
import requests
import json

def main(event):
  
  key = os.getenv("HuggingFace")
  reason = event.get('inputFields').get('churn_reason')
  content = event.get('inputFields').get('content')
  note = event.get('inputFields').get('hs_note_body')
  email = event.get('inputFields').get('hs_email_html')
  url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
  headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
  }
  data = {
    "inputs": str(content) + str(reason),
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))
  if response.status_code == 200:
    result = response.json()
  else:
    result = response.json()
    
  result = result[0]["summary_text"]
  
  return {
    "outputFields": {
      "Content": content,
      "Reason": reason,
      "Result": result
    }
  }