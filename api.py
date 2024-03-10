from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

# Define a request model for the candidate response
class CandidateResponse(BaseModel):
    response: str

# Define function to assess candidate response
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
        max_tokens=500
    )

    # Extract the generated completion text
    output = completion['choices'][0]['message']['content'].strip()
    return output

# Define POST endpoint to assess candidate response
@app.post("/assess")
async def assess_candidate_api(candidate_response: CandidateResponse):
    try:
        result = assess_candidate(candidate_response.response)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#uvicorn api:app --reload
