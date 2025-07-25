from app.utils import *

def extract_sections(documents):
    all_sections = []
    for doc in documents:
        for i, page in enumerate(doc["content"]):
            text = page.get_text("text")
            lines = text.split("\n")
            for line in lines:
                if len(line.strip()) > 5 and line.istitle():
                    all_sections.append({
                        "document": doc["name"],
                        "page_number": i + 1,
                        "section_title": line.strip(),
                        "raw_text": text
                    })
    return all_sections