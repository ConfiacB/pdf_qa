from document_parser import extract_text_from_pdf, chunk_text
from retriever import embed_texts, retrieve_top_k
from gpt_answer import get_answer_from_context

def main():
    api_key = input("Enter your OpenAI API Key: ").strip()
    file_path = "whitepaper_Foundational Large Language models & text gen.pdf"
    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)
    embeddings =  embed_texts(chunks, api_key)

    while True:
        question = input("\n> Enter your question (or 'exit'): ")
        if question.lower() == "exit":
            break

        top_chunks = retrieve_top_k(question, chunks, embeddings, api_key)
        context = "\n".join(top_chunks)
        answer = get_answer_from_context(question, context, api_key)
        print(f"> Answer: {answer}")

if __name__=="__main__":
    main()