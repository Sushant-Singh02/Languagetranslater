from googletrans import Translator

def translate_to_german(text):
    translator = Translator()
    
    # Translate to German
    translated_text = translator.translate(text, src='en', dest='de').text
    
    return translated_text

# Example usage
if __name__ == "__main__":
    input_text = input("Enter English text to translate to German: ")
    translated_result = translate_to_german(input_text)
    
    print("Translated Text:", translated_result)
