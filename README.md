# End-to-End Medical Chatbot using Llama2

This project is an end-to-end medical chatbot application powered by Llama2/Groq, LangChain, and Pinecone. It provides accurate medical information through a conversational web interface, leveraging advanced language models and vector search capabilities.

## Features

- **Advanced Medical Assistant:** 
  - Structured responses for medical queries
  - Natural conversation handling
  - Context-aware answers
  - Source citations when available

- **Multiple LLM Support:** 
  - Local Llama2 model integration
  - Groq cloud API integration
  - Flexible model switching

- **Vector Search:** 
  - Pinecone vector database integration
  - HuggingFace embeddings
  - Efficient medical document retrieval

- **Enhanced User Experience:**
  - Clean Bootstrap-based chat interface
  - Markdown-formatted responses
  - Mobile-responsive design

## Technical Architecture

1. **Document Processing Pipeline:**
   - PDF ingestion and chunking
   - HuggingFace embedding generation
   - Pinecone vector indexing

2. **Query Processing:**
   - User input analysis
   - Context-based retrieval
   - Structured response generation

3. **Response Generation:**
   - Custom prompt templates
   - Source-backed answers
   - Format-specific outputs

## Project Structure

```
End_to_End_Medical_Chatbot_using_Llama2/
├── app.py              # Main Flask application
├── src/
│   ├── helper.py       # Utility functions
│   └── prompt.py       # Prompt templates
├── templates/
│   └── chat.html       # Web interface
├── model/              # LLM model directory
├── data/              # Medical PDF storage
└── requirements.txt    # Dependencies
```

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

3. **Environment Setup:**
   Create a `.env` file:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Model Setup:**
   - For Local Llama2:
     Place `llama-2-7b-chat.ggmlv3.q4_0.bin` in `model/` directory
   - For Groq:
     Ensure valid API key in `.env`

5. **Data Preparation:**
   - Add medical PDFs to `data/` directory
   - Run indexing script if needed

6. **Launch Application:**
   ```bash
   python app.py
   ```
   Access at `http://localhost:5000`

## Response Format

The chatbot provides structured responses for medical queries:

- **Basic Definition:** Clear, concise explanation
- **Key Characteristics:** Main features and details
- **Types and Classifications:** Categories if applicable
- **Clinical Significance:** Impact and implications

## Environment Variables

Required environment variables:
- `PINECONE_API_KEY`: For vector database access
- `GROQ_API_KEY`: For cloud LLM access (if using Groq)

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Acknowledgments

- LangChain for the chain-of-thought framework
- Pinecone for vector search capabilities
- Meta for Llama2 model
- Groq for cloud LLM services