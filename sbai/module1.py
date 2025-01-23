from openai import OpenAI
import google.generativeai as genai

class ChatGPT:
    def __init__(self, api_key, model="gpt-4o-mini", temperature=0, top_p=0, instructions="", max_token=200, memory=False):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.instructions = instructions
        self.max_token = max_token
        self.memory = memory
        self.history = []
        self.client = OpenAI(api_key=self.api_key)

    def prompt(self, prompt):
        messages = [{"role": "system", "content": self.instructions}]
        
        if self.memory:
            messages.extend(self.history)

        messages.append({"role": "user", "content": prompt})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_token
            )
            reply = response.choices[0].message.content
            
            if self.memory:
                self.add_to_history({"role": "user", "content": prompt})
                self.add_to_history({"role": "assistant", "content": reply})

            return reply
        except Exception as e:
            return str(e)

    def add_to_history(self, message):
        if len(self.history) >= 5:
            self.history.pop(0)
        self.history.append(message)

    def clear_history(self):
        self.history = []

class Gemini:
    def __init__(self, api_key, model="gemini-2.0-flash-exp", temperature=0, top_p=0, max_token=200, memory=False, instructions=""):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.max_token = max_token
        self.memory = memory
        self.instructions = instructions
        self.history = [ 
           {"role": "user", "parts": [self.instructions]},
           {"role": "model", "parts": ["Ok, I will follow your guidelines accurately."] if instructions else ""}
        ]

        genai.configure(api_key=self.api_key)

        generation_config = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": 40,
            "max_output_tokens": self.max_token,
        }

        self.model = genai.GenerativeModel(
            model_name=self.model,
            generation_config=generation_config,
            system_instruction=self.instructions if self.instructions else None
        )

        self.chat_session = self.model.start_chat(history=self.history)

    def prompt(self, prompt):
        try:
            if self.memory:
                response = self.chat_session.send_message(prompt)
            else:
                self.chat_session = self.model.start_chat()
                response = self.chat_session.send_message(prompt)

            return response.text
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def clear_history(self):
        self.chat_session = self.model.start_chat()