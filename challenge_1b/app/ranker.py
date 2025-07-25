from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rank_sections(sections, persona, job):
    query = persona + " " + job
    corpus = [s["section_title"] + " " + s["raw_text"] for s in sections]

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([query] + corpus)
    sims = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    ranked_idx = np.argsort(sims)[::-1]

    top_sections = []
    sub_analysis = []

    for rank, idx in enumerate(ranked_idx[:10]):
        s = sections[idx]
        top_sections.append({
            "document": s["document"],
            "page_number": s["page_number"],
            "section_title": s["section_title"],
            "importance_rank": rank + 1
        })
        sub_analysis.append({
            "document": s["document"],
            "page_number": s["page_number"],
            "refined_text": s["raw_text"][:500]  # Just a sample snippet
        })

    return {"sections": top_sections, "subsections": sub_analysis}