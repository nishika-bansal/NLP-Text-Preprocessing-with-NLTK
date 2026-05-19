import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from collections import Counter
import nltk

# First-time downloads (safe check)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        print("\n🔹 Original Text:", text)

        # 1. Lowercase
        text = text.lower()

        # 2. Remove special characters, numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # 3. Tokenization
        words = word_tokenize(text)

        # 4. Remove stopwords
        words = [w for w in words if w not in self.stop_words]

        # 5. Remove duplicates
        words = list(dict.fromkeys(words))

        # 6. Stemming
        words = [self.stemmer.stem(w) for w in words]

        # 7. Lemmatization
        words = [self.lemmatizer.lemmatize(w) for w in words]

        # 8. Frequency (ADDED IMPROVEMENT)
        freq = Counter(words)
        print("\n📊 Top Words:", freq.most_common(5))

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

        with open("output.txt", "a", encoding="utf-8") as file:
            file.write(result + "\n")

        print("💾 Saved to output.txt")