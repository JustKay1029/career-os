import unittest
import sys
import os

# Ensure app package is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.chunker import RecursiveTextChunker
from app.schemas import DocumentChunk

class TestRecursiveTextChunker(unittest.TestCase):
    def test_empty_text(self):
        chunker = RecursiveTextChunker(chunk_size=100, chunk_overlap=20)
        chunks = chunker.chunk_text("", doc_id="doc-1", filename="empty.txt")
        self.assertEqual(chunks, [])

    def test_small_text(self):
        chunker = RecursiveTextChunker(chunk_size=500, chunk_overlap=50)
        text = "Machine learning is a subfield of artificial intelligence."
        chunks = chunker.chunk_text(text, doc_id="doc-1", filename="ml.txt", page_number=2)
        
        self.assertEqual(len(chunks), 1)
        chunk = chunks[0]
        self.assertEqual(chunk.content, text)
        self.assertEqual(chunk.metadata.doc_id, "doc-1")
        self.assertEqual(chunk.metadata.filename, "ml.txt")
        self.assertEqual(chunk.metadata.page_number, 2)
        self.assertEqual(chunk.metadata.chunk_index, 0)
        self.assertEqual(chunk.char_count, len(text))

    def test_large_text_splits(self):
        chunker = RecursiveTextChunker(chunk_size=120, chunk_overlap=30)
        paragraph = (
            "Retrieval-Augmented Generation (RAG) optimizes the output of an LLM. "
            "It references an authoritative knowledge base outside of its training data sources. "
            "This ensures that answers are grounded and hallucination-free."
        )
        chunks = chunker.chunk_text(paragraph, doc_id="doc-rag", filename="rag.txt")
        
        self.assertGreater(len(chunks), 1)
        # Verify sequential indices
        for i, c in enumerate(chunks):
            self.assertEqual(c.metadata.chunk_index, i)
            self.assertGreater(len(c.content), 0)
            self.assertEqual(c.metadata.doc_id, "doc-rag")

    def test_invalid_overlap(self):
        with self.assertRaises(ValueError):
            RecursiveTextChunker(chunk_size=100, chunk_overlap=150)

if __name__ == "__main__":
    unittest.main()

