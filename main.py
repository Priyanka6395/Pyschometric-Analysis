import openai

openai.api_key="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"

def chat_with_gpt(prompt):
    response=openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__== "__main__":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye","terminate"]:
            break

        response=chat_with_gpt(user_input)
        print("Chatbot: ", response)