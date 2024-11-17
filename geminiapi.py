#a

#-!pip install google-generativeai

import google.generativeai as genai
#gemini API key 
GOOGLE_API_KEY = "AIzaSyCfq9PeM1zIFUyLh8we8OqPkwzmU_-PiGs"


user_text1="""
give me hindi translation of this sentance
"hey! you navneet ai boy "
"""
genai.configure(api_key= GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")
response1= model.generate_content(user_text1)
result1 = response1.text

print(result1)
#as
