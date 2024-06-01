import lorem


class GenerateTextMixin:
   def generate_lorem(cls):
        with open(f"media/task2/tmp.txt", "w") as file:
            file.write(lorem.text())