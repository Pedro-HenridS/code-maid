import google.generativeai as genai

def generativeResponse(question: str):
    
   genai.configure(api_key="AIzaSyD9pDmnEkbkOTi4uzWPtd6RqnSxj-yEQbI")

   for m in genai.list_models():
      if 'generateContent' in m.supported_generation_methods:
         print(m.name)

   model = genai.GenerativeModel('gemini-pro')

   res = model.generate_content(f"{question}. Responda mostrando apensa o código.")
   

   return res

if __name__ == "__generativeResponse__":
    generativeResponse()

