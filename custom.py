import openai

openai.api_key = "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"

def initial():
    description = """
1. "I will provide you with a questions and answers from the student. Based on the response, please assign points up to 10 for psychological behavior, logical behavior, and mental behavior." 
2. based on emotional intelligence, communication skills, stress management, attitude and motivation, interpersonal skills, professionalism and cultural based on all these parameters you should rate the psychological behaviour not individually.   
3. based on problem solving skills, critical thinking, decision making, creativity and innovation, adaptability, attention to detail and memory recall based on all these parameters you should rate the mental behaviour not individually.
4. based on clarity of thought, evidence based reasoning, problem solving approach, consistency, logical deduction, analytical skills, decision-making process based on all these parameters you should rate the logical behaviour not individually.
5. the side headings should be in a new line psychological behavior heading followed by in a new line score followed by with a new line description, logical behavior  heading followed by in a new line score followed by with a new line description, and mental behavior  heading followed by in a new line score followed by with a new line description not individually."
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": description}]
    )

    return response.choices[0].message.content.strip()

def prompt(input):
    messages = []  # Initialize an empty list for messages
    messages.append({"role": "user", "content": input})  # Append user input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    response = initial() 
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye", "terminate"]:
            break

        response = prompt(user_input)
        print("Chatbot: ", response)
