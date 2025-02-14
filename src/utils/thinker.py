from ollama import chat
import langid

systemLanguage = 0
class Thinker:
    def __init__(self, history_messages=[], system_messages=[]):
        print("Thinker initialized")
        #default system message
        self.messages = [
            {'role': 'system', 'content': 'only speak english, and not speak more then 100 tokens'}
            ]
        
        # load system message from config
        self.system_messages = system_messages
        self.messages += self.system_messages

        self.history_message = history_messages
        if self.history_message:
            self.messages += self.history_message
        

    def think(self, text):
        # check text langugaes to decide system language
        systemMessage = {'role': 'system', 'content': 'only speak english, and not speak more then 100 tokens'}
        textLang = self.detect_languages(text)
        if textLang == 'zh':
            print("Chinese detected")
            systemMessage['content'] = '說中文,並且不超過100個令牌'
        
        # set system language
        self.messages[systemLanguage] = systemMessage

        # add user content this time
        self.messages.append({'role': 'user', 'content': text})
        self.history_message.append({'role': 'user', 'content': text})
        
        stream = chat(
            model='llama3.2',
            messages=self.messages,
            stream=True
        )

        response_text = ""
        for chunk in stream:
            # cleaned_content = ''.join(filter(lambda x: x.isalnum() or x.isspace(), chunk['message']['content']))
            # response_text += cleaned_content

            response_text += chunk['message']['content']
            # print(chunk['message']['content'], end='', flush=True)
        
        # record assistant message to self.messages for chat history
        self.messages.append({'role': 'assistant', 'content': response_text})
        self.history_message.append({'role': 'assistant', 'content': response_text})
        
        return response_text
    
    def detect_languages(self, text):
        langid.set_languages(['en', 'zh'])
        words = text.split()
        for word in words:
            if langid.classify(word)[0] == 'zh':
                return 'zh'
        return 'en'
    


# Example usage
if __name__ == "__main__":
    thinker = Thinker()
    # show memory
    print(thinker.messages)


    # test think
    text = "Introduce yourself"
    response = thinker.think(text)
    print(f"Response: {response}")
