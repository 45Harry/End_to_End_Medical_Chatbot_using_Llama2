# End-to-End Medical Chatbot using Llama2

This project is an end-to-end medical chatbot application powered by Llama2, LangChain, and Pinecone. It allows users to interact with a medical knowledge base through a conversational web interface, providing helpful and context-aware answers to medical queries.

---

## Features

- **Conversational Medical Assistant:** Ask medical questions and receive contextually relevant answers.
- **Llama2 Language Model:** Utilizes a local Llama2 model for generating responses.
- **Document Retrieval:** Uses Pinecone vector database and HuggingFace embeddings to retrieve relevant medical documents.
- **PDF Knowledge Base:** Easily ingest and index medical PDFs for chatbot knowledge.
- **Modern Web UI:** Clean, Bootstrap-based chat interface for seamless user experience.

---

## How It Works

1. **PDF Ingestion:** Medical PDFs are loaded and split into text chunks.
2. **Embedding & Indexing:** Chunks are embedded using HuggingFace models and indexed in Pinecone.
3. **User Query:** User submits a question via the web chat.
4. **Retrieval & Response:** Relevant chunks are retrieved, and Llama2 generates a helpful answer using a custom prompt template.

---

## Project Structure

- `app.py` — Main Flask app, handles chat logic and model inference.
- `src/helper.py` — PDF loading, text splitting, and embedding utilities.
- `src/prompt.py` — Custom prompt template for Llama2.
- `templates/chat.html` — Bootstrap-based chat UI.
- `requirements.txt` — Python dependencies.
- `model/` — Directory for the Llama2 model file.
- `data/` — Directory for PDF documents.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone git@github.com:45Harry/End_to_End_Medical_Chatbot_using_Llama2.git
   cd End_to_End_Medical_Chatbot_using_Llama2
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Llama2 model:**
   - Place your `llama-2-7b-chat.ggmlv3.q4_0.bin` file in the `model/` directory.

4. **Set up Pinecone:**
   - Create a `.env` file with your Pinecone API key:
     ```
     PINECONE_API_KEY=your_pinecone_api_key
     ```

5. **Add your medical PDFs:**
   - Place PDF files in the `data/` directory and run the indexing script if needed.

6. **Run the app:**
   ```bash
   python app.py
   ```
   - Access the chatbot at `http://localhost:5000`.

---

## Example Prompt Template

```
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {input}

Only return the helpful answer below and nothing else.
Helpful answer:
```

---

## License

This project is licensed under the MIT License.