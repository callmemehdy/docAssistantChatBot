import argparse
# from langchain.vectorstores.chroma import Chroma # DEPRECATED
from langchain_chroma import Chroma 
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import sys

from embd import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("query_text", type=str, help="The query text.")
    # args = parser.parse_args()
    # query_text = args.query_text
    while True:
        query_text = input("query: ").strip()

        if query_text == "EXIT":
            print("Bye!")
            sys.exit(0)
        print("you will get your response after a while...")
        response_text, sources = query_rag(query_text) 
        formatted_response = f"Response: {response_text}"
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(formatted_response)



def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=2)

    # for doc, _ in results:
    #     print(f"{doc}\n-----------------------------------------------------------------------\n", file=sys.stderr)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = OllamaLLM(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    return response_text, sources

if __name__ == "__main__":
    main()