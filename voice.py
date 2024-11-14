import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manage driver

class Voice:
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()
        
    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    #print('Listening...')
                    audio = self.recognizer.listen(source)
                    
                    # Recognize the spoken command and print it
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Recognized command: {command}")  # Print command to console
                    
                    # Check if "search" is in the command
                    if "search" in command:
                        search_query = command.replace("search ", "")
                        print(f"Searching for: {search_query}")  # Print the search query
                        
                        # Set up Chrome options
                        options = webdriver.ChromeOptions()
                        options.add_argument('--no-sandbox')
                        options.add_argument('--disable-dev-shm-usage')

                        # Use WebDriverManager to handle ChromeDriver
                        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                        driver.get(f"https://www.google.com/search?q={search_query}")
                        
                        # Optional: Close the browser after the search
                        # driver.quit()
                        
            except sr.UnknownValueError:
                # Speech was not recognized
                print("Could not understand audio")
                
            except sr.RequestError:
                # Issue with Google Speech Recognition service
                print("Could not request results; check your network connection.")
                
            except Exception as e:
                print(f"An error occurred: {e}")

listener = Voice()
