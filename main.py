import argparse
from document_parser import extract_text_from_pdf, chunk_text
from retriever import embed_texts, retrieve_top_k
from gpt_answer import get_answer_from_context
from utils import get_api_key

def main(file_args):
    # Step 1: Get OpenAI API key from user input
    api_key = get_api_key()

    # Step 2: Choose PDF file to parse
    default_file = "whitepaper_Foundational Large Language models & text gen.pdf"
    file = file_args if file_args else default_file
    print(f"Parsing PDF document: {file}")

    # Step 3: Extract and chunk text from the PDF
    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)

    # Step 4: Generate embeddings for each chunk using OpenAI API
    embeddings = embed_texts(chunks, api_key)

    # Step 5: Start user input loop
    print("\n✅ Ready! You can now ask questions.")
    while True:
        question = input("\n> Enter your question (or 'exit' to quit): ")
        if question.strip().lower() == "exit":
            break

        print("Retrieving relevant document chunks...")
        top_chunks = retrieve_top_k(question, chunks, embeddings, api_key)
        print("Generating answer...")
        context = "\n".join(top_chunks)
        answer = get_answer_from_context(question, context, api_key)
        print(f"\n> Answer: {answer}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=False, help="PDF file path")
    args = parser.parse_args()
    main(args.file)