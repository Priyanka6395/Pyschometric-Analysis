import openai

def assess_candidate(response):
    # Set up OpenAI API
    openai.api_key = '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'

    # Define the prompt
    prompt = f"I will provide you with a questions and answers from the student. Based on the response, please assign points up to 10 for psychological behavior, logical behavior, and mental behavior.\n\n{response}\n\nPsychological Behavior:\nScore: \nDescription:\n\nLogical Behavior:\nScore: \nDescription:\n\nMental Behavior:\nScore: \nDescription:\n2. based on emotional intelligence, communication skills, stress management, attitude and motivation, interpersonal skills, professionalism and cultural based on all these parameters you should rate the psychological behaviour not individually. \n3. based on problem solving skills, critical thinking, decision making, creativity and innovation, adaptability, attention to detail and memory recall based on all these parameters you should rate the mental behaviour not individually.\n4. based on clarity of thought, evidence based reasoning, problem solving approach, consistency, logical deduction, analytical skills, decision-making process based on all these parameters you should rate the logical behaviour not individually."

    # Generate completion
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ],
        max_tokens=200
    )

    # Extract the generated completion text
    output = completion['choices'][0]['message']['content'].strip()
    return output

# Example response from the user
response = """
Question: Sure. Moving on, can you tell me about your previous work experience, if any?
Answer: Yeah i worked in rail sadan bbs there i have done project based on web development which is done used by the tech nologies html,css and bootstrap and present at spotmies as an ml developer
"""

# Call the function to assess the candidate
result = assess_candidate(response)
print(result)
