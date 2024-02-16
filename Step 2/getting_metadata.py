from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import GrobidParser
import json
import os

path = ["2024-l1-topics-combined-2.pdf", "2024-l2-topics-combined-2.pdf", "2024-l3-topics-combined-2.pdf"]

if not os.path.exists("Metadata"):
    os.makedirs("Metadata")

for file in path:
    loader = GenericLoader.from_filesystem(
        file,
        parser=GrobidParser(segment_sentences=False),
    )
    docs = loader.load()

    data = file.split("-")

    res = []
    with open(f"Metadata/Grobid_RR_{data[0]}_{data[1]}_combined_metadata.json", "w") as file:
        for i in range(len(docs)):
            res.append({"text": docs[i].metadata['text'], "section_title": docs[i].metadata['section_title'],"file_path": docs[i].metadata['file_path']})
        json.dump(res, file)
