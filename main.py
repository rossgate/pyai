import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt

model = "gemini-2.5-flash"

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    if api_key == None:
        raise Exception('api key cannot be blank')
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    for i in range (1,20):
        if i >= 20:
            break
        try:

            response = generate_content(messages)
            
            if response.candidates != None:
                for candidate in response.candidates:
                    messages.append(candidate.content)

            if response.usage_metadata == None:
                raise RunTimeError("no usage metadata returned")
            
            if args.verbose == True:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            if response.function_calls:
                function_results = []
                for function_call in response.function_calls:
                    
                    function_call_result = call_function(function_call, args.verbose)

                    if function_call_result.parts == None:
                        raise Exception("empty parts list in function call result")
                    if function_call_result.parts[0].function_response == None:
                        raise Exception("function_response should not be None")
                    if function_call_result.parts[0].function_response.response == None:
                        raise Exception("response in function_response should not be None")

                    function_results.append(function_call_result.parts[0])
                    messages.append(
                        types.Content(
                            role="user",
                            parts=function_results
                        )
                    )
                    
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
            
            if response.function_calls == None and response.text != None:
                print(f"final response: {response.text}")
                break

        except Exception as e:
            print(f"ERROR: {e}")
            return
        

def generate_content(messages):

    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    return response

if __name__ == "__main__":
    main()