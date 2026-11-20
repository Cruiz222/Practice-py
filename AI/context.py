def build_context(customer_message, customer_id):

    system = """
        you are a shopPay helper for Mama Nkechi.
        Rules: Answer only from CONTEXT, never invent prices.
        If price not in Context, say let me check with Mama Nkechi.
        Dont handle BVN, pin, passwords, or refunds above N5k.
        """

    context_docs = search_shop_doc(customer_message, top_k=3)

    history_summary = get_summery(customer_id)

    messages = [
        {"role": system, "content": system},
        {"role": "user", "content": f"CONTEXT: {context_docs}\nHISTORY{history_summary}\nQUESTION{customer_message}"}
    ]

    return messages