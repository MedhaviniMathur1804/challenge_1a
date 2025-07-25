import os
import json
import fitz  # PyMuPDF
from collections import defaultdict
from sklearn.cluster import KMeans
import pandas as pd

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    blocks_data = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        blocks_data.append({
                            "text": span["text"].strip(),
                            "size": round(span["size"], 2),
                            "font": span["font"],
                            "flags": span["flags"],
                            "page": page_num,
                            "y": span["origin"][1]
                        })

    blocks_df = pd.DataFrame(blocks_data)
    blocks_df = blocks_df[blocks_df["text"].str.len() > 3].reset_index(drop=True)

    font_sizes = blocks_df[["size"]].values
    n_clusters = min(len(set(blocks_df["size"])), 4)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(font_sizes)
    blocks_df["cluster"] = kmeans.labels_

    cluster_sizes = blocks_df.groupby("cluster")["size"].mean().sort_values(ascending=False)
    level_map = {cid: f"H{idx+1}" for idx, cid in enumerate(cluster_sizes.index)}
    blocks_df["level"] = blocks_df["cluster"].map(level_map)

    page1_blocks = blocks_df[(blocks_df["page"] == 1)]
    top_blocks = page1_blocks.sort_values(by=["size", "y"], ascending=[False, True])
    title = top_blocks.iloc[0]["text"] if not top_blocks.empty else "Untitled Document"

    outline = []
    seen = set()
    for _, row in blocks_df.iterrows():
        key = (row["text"], row["level"], row["page"])
        if key not in seen:
            seen.add(key)
            outline.append({
                "level": row["level"],
                "text": row["text"],
                "page": row["page"]
            })

    return {
        "title": title,
        "outline": outline
    }

def main():
    # Use local path if running outside Docker
    input_dir = "/app/input" if os.path.exists("/app/input") else "./input"
    output_dir = "/app/output" if os.path.exists("/app/output") else "./output"
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            json_path = os.path.join(output_dir, file.replace(".pdf", ".json"))
            result = extract_outline_from_pdf(pdf_path)
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
