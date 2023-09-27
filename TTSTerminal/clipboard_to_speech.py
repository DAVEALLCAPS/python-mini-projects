import pyttsx3
import pyperclip

def main():
    # Initialize the TTS engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 250)

    # Get text from clipboard
    text = pyperclip.paste()
    if not text.strip():  # Check if clipboard is not empty
        print("Clipboard is empty. Please copy some text and then run the script again.")
        return
    
    print("Text from clipboard:")
    print(text)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
