from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

infomation = ""
if __name__ == "__main__":
    # load_dotenv()
    summery_template = """
    give number of this thing that could i have to do {informantio}
    """
    # print("hello")
    summery_promt_template = PromptTemplate(
        input_variables=["informantio"], template=summery_template
    )
    # llm = ChatOpenAI(temperature=0, model="cha")
    llm = ChatOllama(model="llama3")
    chain = summery_promt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": infomation})
