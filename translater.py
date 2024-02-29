from googletrans import Translator

def translate_to_spanish(text):
    translator = Translator()
    
    # Translate to Spanish
    translated_text = translator.translate(text, src='en', dest='de').text
    
    return translated_text

# Example usage
if __name__ == "__main__":
    input_text = input("Enter English text to translate to Spanish: ")
    translated_result = translate_to_spanish(input_text)
    
    print("Translated Text:", translated_result)
