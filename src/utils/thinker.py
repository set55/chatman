from ollama import chat


class Thinker:
    def __init__(self):
        print("Thinker initialized")
        

    def think(self, text):
        stream = chat(
            model='llama3.2',
            messages=[
                {'role': 'system', 'content': '你是一個AI聊天助手,簡短的口語回答。字數不要超過100字,不要有emoji,不要太多段落,不要幻覺,答案不清楚就回答不清楚'},
            ] + [{'role': 'user', 'content': text}],
            stream=True
        )
        response_text = ""
        for chunk in stream:
            cleaned_content = ''.join(filter(str.isalnum, chunk['message']['content']))
            response_text += cleaned_content
            # print(chunk['message']['content'], end='', flush=True)
        return response_text

# Example usage
if __name__ == "__main__":
    thinker = Thinker()
    text = "Hello, I am Set"
    response = thinker.think(text)
    print(f"Response: {response}")