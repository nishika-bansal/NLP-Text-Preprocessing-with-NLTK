import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer


class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        print("\n🔹 Original Text:", text)

        # 1. Lowercase
        text = text.lower()
        print("Lowercase:", text)

        # 2. Remove emojis, symbols, numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        print("Only letters:", text)

        # 3. Tokenization
        words = word_tokenize(text)
        print("Tokens:", words)

        # 4. Remove stopwords
        words = [word for word in words if word not in self.stop_words]
        print("After stopwords removal:", words)

        # 5. Remove duplicates
        words = list(dict.fromkeys(words))
        print("After removing duplicates:", words)

        # 6. Stemming
        words = [self.stemmer.stem(word) for word in words]
        print("After stemming:", words)

        # 7. Lemmatization
        words = [self.lemmatizer.lemmatize(word) for word in words]
        print("After lemmatization:", words)

        # Final cleaned text
        return " ".join(words)


# MAIN PROGRAM
if __name__ == "__main__":
    processor = TextPreprocessor()

    while True:
        user_input = input("\nEnter text (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        result = processor.clean_text(user_input)

        print("✅ Final Cleaned Text:", result)

        # Save output
        with open("output.txt", "a") as file:
            file.write(result + "\n")

        print("💾 Saved to output.txt")