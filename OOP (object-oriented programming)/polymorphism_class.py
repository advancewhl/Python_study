class Document(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subcalss must implement abstract merthod")


class Pdf(Document):
    def show(self):
        return "show Pdf contents"


class Word(Document):
    def show(self):
        return "show Word contents"


documents = [Pdf("Document1"), Pdf("Document2"), Word("Document3")]
for document in documents:
    print(document.name + ";" + document.show())
