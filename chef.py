import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please speak your ingredients")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't hear you.")
            return None
        except sr.RequestError:
            speak("oh no! I had a problem connecting to the speech services.")
            return None


def generate_recipe(ingredients, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate a recipe using the following ingredients: {', '.join(ingredients)}"
    response = model.generate_content(prompt)

    return response.text

speak("Please enter your ingredients for your recipe. Seperate your ingredients with a comma")

user_input = get_voice_input()
if user_input:
    ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

    api_key = "AIzaSyCioqqaiWEacgniO7lXyjmx_YFgFUvbvUA"

    generated_recipe = generate_recipe(ingredients, api_key)


    print(generated_recipe)
    speak(generated_recipe)

else:
    speak("No ingredients were provided.")