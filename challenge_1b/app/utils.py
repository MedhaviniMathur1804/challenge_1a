import os
import fitz  # PyMuPDF
import datetime

def load_documents(input_dir):
    docs = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            path = os.path.join(input_dir, file)
            try:
                doc = fitz.open(path)
                if doc.page_count == 0:
                    continue  # skip empty PDFs
                docs.append({"name": file, "path": path, "content": doc})
            except Exception as e:
                print(f"⚠️ Skipping file {file}: {e}")
    return docs


def get_timestamp():
    return datetime.datetime.now().isoformat()

def save_output(data, path="output/result.json"):
    import json
    os.makedirs("output", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)