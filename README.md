# Resume Parser API

This repository contains a simple resume-parsing framework & a REST API around it (FastAPI + Pydantic).

## Features

- Parses PDF and Word (.docx) resumes.  
- Extracts `name`, `email`, and `skills`.  
- Skills extraction uses a dummy LLM-based client (you can swap in a real one).  
- Exposes an HTTP API to upload a resume and get structured JSON.

## Requirements
```
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn app:app --reload
```

Then send a POST request. Example(curl):
```
curl -F "file=@/path/to/resume.pdf" http://localhost:8000/parse-resume/
```

Response:
```
{   "name":"Muhammad Muneeb Arshad",
    "email":"mnbrshd@gmail.com",
    "skills":["ASR","AWS","AWS Bedrock","AWS Lambda","AWS S3","C++","Celery","ChromaDB","CI/CD","Classic ML","Cloud Functions","Cloud Run","Chunking strategies","Contextual reasoning","Distributed inference","Docker","Document processing","Django","Embeddings","Entity extraction","Evaluation loops","Evaluators","Event-driven architecture","FastAPI","Feature engineering","GCP","Gemini","Grafana","Hyperparameter optimization","Kubernetes","Lambda","LangChain","LangGraph","LLM-based extraction","Memory systems","Message queues","Microservices","Milvus","ML lifecycle","MobileSAM","Monitoring","Multi-column layout handling","ONNX","OpenAI Agents SDK","Pinecone","Prometheus","Pub/Sub","Python","PyQt5","PyTorch","RabbitMQ","RAG","Random Forest","SAM","Semantic search","Serverless compute","Serverless pipelines","SQLAlchemy","spaCy NER","Statistical modeling","Summarization","SVM","Table structure extraction","TensorRT","Terraform","Text segmentation","Tool-use agents","TransUNet","Vector databases","Versioning","Weaviate","XGBoost","YOLOv5","YOLOv8"]}
```
