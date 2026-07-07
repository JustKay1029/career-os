# AI Engineer Roadmap

An AI Engineer bridges the gap between raw data, machine learning models, software engineering, and production operations (LLMOps). This roadmap defines the critical phases of learning to become production-ready.

---

## 🗺️ Learning Phases

### Phase 1: Software Engineering & Data Foundations
Before running models, an AI engineer must write clean, production-grade code.
- **Languages:** Python (Advanced OOP, Async programming, Packaging).
- **Core Libraries:** NumPy (vectorized operations), Pandas (efficient data wrangling).
- **Tools:** Git, Linux Shell scripting, Docker containers.

### Phase 2: Classical Machine Learning & Mathematics
Understanding what happens under the hood prevents treating models as black boxes.
- **Math:** Linear Algebra (matrix multiplication, eigenvalues), Calculus (gradient descent), Probability & Statistics.
- **Classical ML:** Regression (Linear, Logistic), Trees & Ensembles (Decision Trees, Random Forest, XGBoost), Unsupervised Learning (K-Means, PCA).
- **Frameworks:** Scikit-Learn.

### Phase 3: Deep Learning (DL)
Transitioning from traditional feature engineering to feature learning.
- **Foundations:** Multi-layer Perceptrons (MLPs), Backpropagation, Activation functions.
- **Architectures:** Convolutional Neural Networks (CNNs for vision), Recurrent Networks (LSTMs/GRUs for sequences), Attention Mechanism & Transformers.
- **Framework:** PyTorch (preferred over TensorFlow in research and modern AI engineering).

### Phase 4: Generative AI & Large Language Models (LLMs)
Building applications on top of foundation models.
- **APIs & Local Models:** Structured generation, prompt engineering, rate limit handling, token optimization, running local models via Ollama.
- **Embeddings & Vector Search:** Vector databases (Pinecone, Qdrant, Chroma), semantic search, metadata filtering.
- **RAG (Retrieval-Augmented Generation):** Naive RAG, Parent Document Retrieval, Hybrid Search, Query Translation, and RAG evaluation (using Ragas framework).
- **Agents:** ReAct pattern, state management (LangGraph), custom tool use, structured output parsing.

### Phase 5: LLMOps & Production Deployment
Taking models from notebooks and serving them to millions of users.
- **Web Services:** FastAPI, Streamlit (for quick prototyping).
- **Observability:** Langfuse, Langsmith, Arize (tracking latency, token cost, prompt versioning).
- **Model Efficiency:** Quantization (GGUF, AWQ), caching, inference engines (vLLM).
