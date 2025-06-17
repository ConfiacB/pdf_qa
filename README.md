# Document QA using OpenAI API

## Overview

This project allows you to upload a PDF file and ask questions about its content. It uses OpenAI's ChatGPT and Embedding APIs to generate document-grounded answers — avoiding hallucinations by only relying on the content of the file.

## Requirements

- openai
- PyMuPDF (fitz)
- numpy

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the program

   ```bash
   python main.py
   ```

   or

   ```bash
   python main.py --file "document.pdf"
   ```

3. Set your API key

4. Ask questions

## Project Structure

```bash
pdf_qa/
│
├── main.py              # Entry point - load file, run pipeline
├── parser.py            # PDF loading and chunking
├── retriever.py         # Embedding + similarity search
├── gpt_answer.py        # ChatGPT call
├── utils.py             # Helper functions
├── requirements.txt     # Dependencies
└── README.md            # You’re here
```

## Hallucination Strategy

- Restrict GPT’s knowledge to the document with system prompt in the Chat API call
- Parsing the PDF into small parts (chunks), embed them, and then search for the most relevant chunks
- Use the most relevant chunk as context for GPT
- Fallback response when answer is missing, we tell GPT to say "Not available"
