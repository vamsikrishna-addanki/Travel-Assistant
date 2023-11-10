from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain import VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import ConversationalRetrievalChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA, LLMChain
from langchain.memory import ConversationBufferMemory
import config
import logging
import time
import os
​
​
def answer(days, start, end, mode) -> str:
​
    prompt_template = PromptTemplate(template=config.prompt_template, input_variables=["days", "start", "end", "mode"])
    # memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    # doc_chain = LLMChain(
    #     llm=ChatOpenAI(
    #         openai_api_key=config.OPENAI_API_KEY,
    #         streaming=True,
    #         model_name="gpt-4",
    #         temperature=0,
    #         max_tokens=300
    #     ),
    #     chain_type="stuff",
    #     memory=memory,
    #     prompt=prompt_template,
    # )
    model = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.4, openai_api_key=config.OPENAI_API_KEY)
    gen = LLMChain(llm=model, prompt=prompt_template)
    res = gen({"days": days, "start": start, "end": end, "mode": mode})
    ans = res["text"]
    # chat_history = []
    # while True:
    #     query = prompt
    #     if query == "exit" or query == "quit" or query == "q":
    #         print('Exiting')
    #         sys.exit()
    #     result = qa({"query": prompt})
    #     print('Answer: ' + result["result"])
    #     chat_history.append((prompt, result["result"]))
    return ans
​
​
if __name__ == "__main__":
    days1 = 4
    start1 = "chennai"
    end1 = "bangalore"
    mode1 = "pubic travels"
    theme1 = "chill"
    # days1 = input("days:")
    # start1 = input("start:")
    # end1 = input("end:")
    # mode1 = input("mode:")
    # theme1 = input("theme:")
    result = answer(days1, start1, end1, mode1)
    print(result)