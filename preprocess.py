import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
<<<<<<< HEAD
from collections import Counter
import nltk

# First-time downloads (safe check)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
=======

>>>>>>> da7d8bd9d986b15b20d16f452c8e6e9e38471890

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        print("\n🔹 Original Text:", text)

        # 1. Lowercase
        text = text.lower()
<<<<<<< HEAD

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

=======
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
>>>>>>> da7d8bd9d986b15b20d16f452c8e6e9e38471890
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

<<<<<<< HEAD
        with open("output.txt", "a", encoding="utf-8") as file:
=======
        # Save output
        with open("output.txt", "a") as file:
>>>>>>> da7d8bd9d986b15b20d16f452c8e6e9e38471890
            file.write(result + "\n")

        print("💾 Saved to output.txt")