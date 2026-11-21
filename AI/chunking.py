def index_documents(docs):
    chunk = []

    for doc in docs:
        for chunk_text in split_into_chunks(doc, size="1-3 sentences"):
            vector = embed(chunk_text)

            save_to_vector(
                text=chunk_text,
                vector=vector,
                metadata={"price": "price_list_2026", "source": "Diobu"}
            )

    return "Indexed"



def search_shop_doc(question):
    question_vector = embed(question)

    results = vector_db.search(question_vector, top_k=3)

    return results


def answer_customer(question):
    context = search_shop_doc(question)

    if not context:
        return {"price_found": False, "reply": "Let me check in with mama first"}

    return llm_call(
        prompt="Always answer from context. Never Invent",
        context=context,
        question=question
    )                    