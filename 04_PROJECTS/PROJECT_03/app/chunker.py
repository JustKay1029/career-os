import re
from typing import List
from app.schemas import DocumentChunk, ChunkMetadata

class RecursiveTextChunker:
    """
    Splits continuous text into overlapping semantic chunks along natural 
    text boundaries (paragraphs, lines, sentences, spaces).
    """
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 80):
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be strictly less than chunk_size")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = ["\n\n", "\n", ". ", "? ", "! ", " ", ""]

    def _split_text(self, text: str, separators: List[str]) -> List[str]:
        if not separators:
            return list(text)
        
        separator = separators[0]
        remaining_separators = separators[1:]
        
        if separator == "":
            return list(text)
        
        if separator in text:
            splits = text.split(separator)
            result = []
            for i, piece in enumerate(splits):
                if i < len(splits) - 1:
                    piece += separator
                if len(piece) > self.chunk_size and remaining_separators:
                    result.extend(self._split_text(piece, remaining_separators))
                else:
                    result.append(piece)
            return result
        else:
            return self._split_text(text, remaining_separators)

    def chunk_text(self, text: str, doc_id: str, filename: str, page_number: int = 1) -> List[DocumentChunk]:
        """
        Splits raw text and returns a list of DocumentChunk objects with overlap and metadata.
        """
        text = text.strip()
        if not text:
            return []

        raw_pieces = self._split_text(text, self.separators)
        
        chunks: List[str] = []
        current_chunk = ""
        
        for piece in raw_pieces:
            if len(current_chunk) + len(piece) <= self.chunk_size:
                current_chunk += piece
            else:
                if current_chunk.strip():
                    chunks.append(current_chunk.strip())
                # Start new chunk with overlap from the end of current_chunk
                if self.chunk_overlap > 0 and len(current_chunk) > self.chunk_overlap:
                    current_chunk = current_chunk[-self.chunk_overlap:] + piece
                else:
                    current_chunk = piece
                    
        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        result: List[DocumentChunk] = []
        for index, content in enumerate(chunks):
            metadata = ChunkMetadata(
                doc_id=doc_id,
                filename=filename,
                page_number=page_number,
                chunk_index=index
            )
            result.append(DocumentChunk(content=content, metadata=metadata))
            
        return result
