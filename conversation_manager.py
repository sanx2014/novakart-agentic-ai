from rag_engine import load_vector_store
from langchain_groq import ChatGroq
import os
from guardrails import hallucination_check, policy_violation_check
from sales_engine import recommend_product
from escalation_engine import check_escalation

vectorstore = load_vector_store()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="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"
)


def generate_response(query, order_context):

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""

You are NovaKart AI Support Agent.

Use ONLY the policy documents provided.

Order Details:
{order_context}

Knowledge Base:
{context}

Customer Question:
{query}

Rules:
Follow company policies strictly
Be polite and empathetic
Do not hallucinate
Offer solution

Answer:
"""

    response = llm.invoke(prompt).content

    if not hallucination_check(response, context):
        return "ESCALATE"

    if not policy_violation_check(response):
        return "ESCALATE"

    return response