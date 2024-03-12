# Pyschometric-Analysis

FastAPI Azure OpenAI Assessment
This repository contains a FastAPI application integrated with the Azure OpenAI API to assess candidate responses. The application is designed to evaluate candidate responses based on predefined criteria for psychological behavior, logical behavior, and mental behavior.
------------------------------------------------------PROCEDURE--------------------------------------------------------------------------------------------------
**Getting Started**
To get started with this application, follow these steps:

1. **Clone the repository to your local machine:**
//git clone https://github.com/your_username/your_repository.git//

**2. Install the required dependencies:**
 //pip install -r requirements.txt//

 **3. Set up Azure OpenAI API credentials:**
//Replace "your key here" in the AZURE_OPEN_AI_KEY variable with your Azure OpenAI API key.//
//Ensure the AZURE_OPEN_AI_MODEL, AZURE_API_VERSION, and AZURE_BASE_URL variables are correctly configured according to your Azure OpenAI setup.//

**Usage**
Once the application is set up and dependencies are installed, you can run the FastAPI application using the following command:
//uvicorn appname:app --reload//

///This command starts the FastAPI application on http://localhost:8000.///
In VS Code's terminal, execute the code to obtain a URL, which should then be copied into the Postman API (your_url/assess) with a POST request and along with that in the body choose an input type raw and send the response .

for Eg:

{
"response":"Question: Hello, I am Lucy, an HR interviewer from Reaidy company. Can you please introduce yourself and tell me about your background and experience?Answer: Hello, Good morning my name is Riya at present I am studying in Final year btech in Vignan's institute of information and technology. in branch of artificial intelligence and data science"
}

and click "send".

**4. Then the result will be displayed in this format

{

"result": "Assessment result text here" 

}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
**Endpoint**
The application exposes a single endpoint:
//POST /assess: Accepts a JSON payload containing the candidate response. It then assesses the response using the Azure OpenAI API and returns the evaluation result.//

**Example request body:**
//
{
  "response": "Candidate's response text goes here."
}
//

**Example response:**
//
{
  "result": "Assessment result text here."
}
//

**Customization**
You can customize the assessment criteria and behavior by modifying the assess_candidate function in demo.py. Additionally, you can adjust the prompt template to tailor the assessment process according to your specific requirements.

**Contributions**
Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.















