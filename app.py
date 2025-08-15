from flask import Flask, render_template, jsonify,request
from src.helper import download_hugging_face_embedding
from langchain_community.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp
from langchain_pinecone import PineconeVectorStore

from langchain.chains import RetrievalQAWithSourcesChain, create_retrieval_chain
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from dotenv import load_dotenv
from src.prompt import *
import os

# Load the Pinecone api key
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


# Initialize the Flask
app = Flask(__name__)


# Downlaod the embedding model from huggingface 
embeddings = download_hugging_face_embedding()


# Loading the existiong index from pincone cloud
docsearch = PineconeVectorStore.from_existing_index(
    index_name='medicalchatbot', 
    embedding=embeddings
    )

# Create the prompt
prompt = PromptTemplate(
    template=prompt_template,input_variables=['context','input'],
)
chain_type_kwargs = {'prompt':prompt}

#Load the LLM
llm = LlamaCpp(model_path='./model/llama-2-7b-chat.ggmlv3.q4_0.bin',
               temperature =0.8,)
                  


# Create the QA
qa = create_retrieval_chain(
    retriever = docsearch.as_retriever(search_kwargs={'k':2}),
    combine_docs_chain = create_stuff_documents_chain(llm = llm,prompt = prompt),

)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get",methods=['GET','POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    result = qa.invoke({'input':input})
    print("Response :",result['answer'])
    return str(result['answer'])


if __name__ == "__main__":
    app.run(debug = True)