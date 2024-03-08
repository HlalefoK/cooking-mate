import google.generativeai as genai
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def generate_recipe(ingredients, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate a recipe using the following ingredients: {', '.join(ingredients)}"
    response = model.generate_content(prompt)

    return response.text

speak("Please enter your ingredients for your recipe. Seperate your ingredients with a comma")

user_input = input("enter your ingredients for your recipe (Seperate the ingredients with a comma (,) ): ")

ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

api_key = "AIzaSyCioqqaiWEacgniO7lXyjmx_YFgFUvbvUA"

generated_recipe = generate_recipe(ingredients, api_key)


print(generated_recipe)
speak(generated_recipe)