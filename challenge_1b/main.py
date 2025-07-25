import sys
from app.utils import load_documents, save_output, get_timestamp
from app.extractor import extract_sections
from app.ranker import rank_sections

def main():
    input_dir = sys.argv[1]
    persona = sys.argv[2]
    job = sys.argv[3]

    docs = load_documents(input_dir)
    timestamp = get_timestamp()
    extracted = extract_sections(docs)
    ranked = rank_sections(extracted, persona, job)

    output = {
        "metadata": {
            "input_documents": [d["name"] for d in docs],
            "persona": persona,
            "job": job,
            "processing_timestamp": timestamp
        },
        "extracted_sections": ranked["sections"],
        "sub_section_analysis": ranked["subsections"]
    }

    save_output(output)

if __name__ == "__main__":
    main()
