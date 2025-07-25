## Overview

This solution aims to extract and rank relevant document sections and subsections based on a specific persona and their associated job-to-be-done. The objective is to provide intelligent, ranked outputs from a diverse PDF collection.

## Methodology

### 1. Document Parsing

- **Tool Used**: PyMuPDF
- We use PyMuPDF to parse each PDF file and extract raw text from each page.
- Extracted text is split into lines for identifying potential section headers.

### 2. Section Detection

- Heuristics are applied to detect section titles:
  - Line is in title case
  - Line length is sufficient (> 5 characters)
- These heuristics are fast and avoid needing a pretrained model.

### 3. Vector Representation and Ranking

- **Technique**: TF-IDF + Cosine Similarity
- The persona and job description are combined into a query.
- TF-IDF is applied to the query and all extracted section texts.
- Cosine similarity measures how relevant each section is to the query.
- Top 10 sections are selected and ranked.

### 4. Subsection Analysis

- From the top-ranked sections, we extract the first 500 characters of raw text as the refined snippet.
- Each snippet is labeled with document name and page number.

### 5. Output Generation

- Results are saved in a JSON format including:
  - Metadata (persona, job, timestamp)
  - Top extracted sections with importance rank
  - Refined subsections for granular context

## Compliance

- 🖥️ **CPU Only** execution
- 📦 **Model size < 1GB**
- ⚡ **Execution time ≤ 60 seconds**
- 📡 **No internet access** required

This approach ensures lightweight, interpretable, and fast document intelligence tailored to the given persona and job description.
