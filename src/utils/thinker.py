from ollama import chat
import langid

systemLanguage = 0
class Thinker:
    def __init__(self):
        print("Thinker initialized")
        self.messages = [
            {'role': 'system', 'content': 'only speak english, and not speak more then 100 tokens'}
            ]
        

    def think(self, text):
        # check text langugaes to decide system language
        systemMessage = {'role': 'system', 'content': 'only speak english, and not speak more then 100 tokens'}
        textLang = self.detect_languages(text)
        if textLang == 'zh':
            print("Chinese detected")
            systemMessage['content'] = '說中文,並且不超過100個令牌'
        
        # set system language
        self.messages[systemLanguage] = systemMessage

        # add user content
        self.messages.append({'role': 'user', 'content': text})
        
        stream = chat(
            model='llama3.2',
            messages=self.messages,
            stream=True
        )

        # remove use ask content(must last message)
        self.messages.pop(-1)
        response_text = ""
        for chunk in stream:
            # cleaned_content = ''.join(filter(lambda x: x.isalnum() or x.isspace(), chunk['message']['content']))
            # response_text += cleaned_content

            response_text += chunk['message']['content']
            # print(chunk['message']['content'], end='', flush=True)
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
    text = "請自我介紹"
    response = thinker.think(text)
    print(f"Response: {response}")