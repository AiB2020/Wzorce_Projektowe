"Prototype Use Case Example Code"
from document import Document


ORIGINAL_DOCUMENT = Document("Original", [[1, 2, 3, 4], [5, 6, 7, 8]])
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_1 = ORIGINAL_DOCUMENT.clone(1) 
DOCUMENT_COPY_1.name = "Copy 1"

DOCUMENT_COPY_1.list[1][2] = 200
print(DOCUMENT_COPY_1)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_2 = ORIGINAL_DOCUMENT.clone(2) 
DOCUMENT_COPY_2.name = "Copy 2"

DOCUMENT_COPY_2.list[1] = [9, 10, 11, 12]
print(DOCUMENT_COPY_2)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_3 = ORIGINAL_DOCUMENT.clone(2) 
DOCUMENT_COPY_3.name = "Copy 3"

DOCUMENT_COPY_3.list[1][0] = "1234"
print(DOCUMENT_COPY_3)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_4 = ORIGINAL_DOCUMENT.clone(3) 
DOCUMENT_COPY_4.name = "Copy 4"

DOCUMENT_COPY_4.list[1][0] = "5678"
print(DOCUMENT_COPY_4)
print(ORIGINAL_DOCUMENT)
print()