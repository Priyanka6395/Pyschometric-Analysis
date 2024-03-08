import openai

#openai.api_key = "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"
openai.api_key="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"
def initial():
    description = """I will provide you with questions and answers from the student. Based on the response, please assign points up to 10 for psychological behavior, logical behavior, and mental behavior. For psychological behavior, evaluate emotional intelligence, communication skills, stress management, attitude and motivation, interpersonal skills, professionalism, and cultural understanding. For mental behavior, consider problem-solving skills, critical thinking, decision making, creativity and innovation, adaptability, attention to detail, and memory recall. For logical behavior, assess clarity of thought, evidence-based reasoning, problem-solving approach, consistency, logical deduction, analytical skills, and decision-making process."
the response will follow this format.Psychological Behavior Score:
Description: 
Logical Behavior Score:
Description:
Mental Behavior Score: 
Description: 
the descriptions should strictly be under 10 words."""
    response = openai.ChatCompletion.create(
        model="text-ada-001",
        messages=[{"role": "user", "content": description}]
    )

    return response.choices[0].message.content.strip()

def prompt(input):
    messages = []  # Initialize an empty list for messages
    messages.append({"role": "user", "content": f"this is the question and answer.{input}"})  # Append user input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    response = initial() 
    while True:
        user_input = """Question: That's great, Harsha. Now, can you tell me what motivated you to apply for this job?
                    Answer: I badly need a salary"""
        if user_input.lower() in ["quit", "exit", "bye", "terminate"]:
            break

        response = prompt(user_input)
        print("Chatbot: ", response)
