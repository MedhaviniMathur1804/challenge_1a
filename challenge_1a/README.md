# PDF Outline Extractor

Extracts a structured outline (Title, H1, H2, H3 headings) from PDFs for smarter document understanding.

## Features
- **Title & Headings Extraction**: Uses PDF bookmarks if available, otherwise clusters font sizes and uses regex for robust heading detection.
- **Batch Processing**: Processes all PDFs in `/input` and outputs JSONs to `/output`.
- **Dockerized**: Runs fully offline, CPU-only, and is compatible with `linux/amd64`.

## Usage

### 1. Build Docker Image
```sh
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

### 2. Run the Container
```sh
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline-extractor:latest
```
- Place your PDFs in the `input/` directory (max 50 pages each).
- Extracted outlines will appear as `.json` files in `output/`.

## Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Requirements
- No internet required. All dependencies are included in the Docker image.
- Model size and dependencies < 200MB.
- Runs on CPU (amd64/x86_64).

## Notes
- If the PDF has bookmarks (table of contents), those are used for the outline.
- Otherwise, headings are detected using font size clustering and regex for numbered/roman headings.
- Only H1, H2, H3 levels are output.

## License
MIT 