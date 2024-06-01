import zipfile
import lorem
import re
import string

from mixins import GenerateTextMixin

class RegexWorker(GenerateTextMixin):  
    DIR_NAME = "media/task2"

    def __init__(self):
        self.generate_lorem()
    
    def common_task(self):
        """Common task that works with text file and performs some operations on it(task2 compolsary requirements)
        """
        with open(f"{self.DIR_NAME}/tmp.txt", "r") as file:
            content = file.read()

        # Sentences
        sentences = re.split(r'[.?!]', content)
        declarative_sentences = re.split(r'[.]', content)
        interrogative_sentences =  re.split(r'[?]', content)
        imperative_sentences = re.split(r'[!]', content)

        print(f"Number of sentences: {len(sentences)-1}")
        print(f"Number of declarative sentences: {len(declarative_sentences)-1}")
        print(f"Number of interrogative sentences: {len(interrogative_sentences)-1}")
        print(f"Number of imperative sentences: {len(imperative_sentences)-1}")

        words = re.split(r'\s+', content)
        sentence_lengths = [len(s) for s in sentences]
        word_lengths = [len(w) for w in words]

        print(f"Average sentence length: {sum(sentence_lengths) / len(sentence_lengths)}")
        print(f"Average word length: {sum(word_lengths) / len(word_lengths)}")        
    

    def task(self):
        """Task that works with text file and performs some operations on it
        """
        # Output uppercase letters in text
        with open(f"{self.DIR_NAME}/tmp.txt", "r") as file:
            content = file.read()

        # Output uppercase letters in text
        sentences = content.translate(str.maketrans('', '', string.punctuation))
        uppercase_letters = re.findall(r'[A-Z]', sentences)

        sentences = re.sub(r'r+b+c+', 'ddd', sentences)

        # Word less than 5
        words = content.split()
        short_words = [word for word in words if len(word) < 5]

        # Shortest word ending with 'd'
        words_ending_with_d = [word for word in words if word.endswith('d')]
        shortest_word = min(words_ending_with_d, key=len, default=None)

        # All words in descending order of their lengths
        words_sorted_by_length = sorted(words, key=lambda word: len(word), reverse=True)

        # Count smileys
        smileys = re.findall(r'[:;]-*[()\[\]]+', content)

        # Prepare the information to be saved
        info = f"Uppercase letters in text: {uppercase_letters}\n"
        info += f"Sentences after substitution: {sentences}\n"
        info += f"Words less than 5 characters: {short_words}\n"
        info += f"Shortest word ending with 'd': {shortest_word}\n"
        info += f"All words sorted by length: {words_sorted_by_length}\n"
        info += f"Number of smileys: {len(smileys)}\n"

        # Save the information to a file
        with open(f"{self.DIR_NAME}/analysis.txt", "w") as file:
            file.write(info)

        # Archive the file in a ZIP
        with zipfile.ZipFile(f"{self.DIR_NAME}/analysis.zip", "w") as zipf:
            zipf.write(f"{self.DIR_NAME}/analysis.txt")


def task2():
    obj = RegexWorker()
    is_breaked = False
    while True:
        print("---------------------------------------")
        step = int(input("Other steps:\n1. Common task\n2. Task from your variant\n3. Exit\n"))
        print("---------------------------------------")
        match step:
            case 1:
                obj.common_task()
            case 2:
                obj.task()
            case 3:
                is_breaked = True
                break
            case _:
                print("Wtf are you doing here?")
        if is_breaked:
            break
        continue