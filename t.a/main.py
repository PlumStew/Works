class Analiz_Text:
    def __init__(self, file="text.txt", mode="r", encoding="UTF-8"):
        self.file = file
        self.mode = mode
        self.encoding = encoding
        self.read_text()
        self.print_text()

    def open_file(self):
        with open(self.file, self.mode, encoding=self.encoding) as file_object:
            return file_object.read()

    def read_text(self):
        self.txt = self.open_file()

    def text_print(self):
        print(self.txt)


textF = Analiz_Text()
