import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a Ruthless Mentor. Help Traders To Fix their Psychology and Improve their Trading Performance. Make it comperatively easier for them to understand and implement the advice. Provide actionable steps and practical tips. Avoid generic advice and focus on specific strategies that can be applied in real trading scenarios."
    ),
    ("human", "{question}")
])

chain = prompt | llm


def ask_ai(question: str):
    response = chain.invoke({
        "question": question
    })

    return response.content