from pypdf import PdfReader
import os
from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET

path = ["2024-l1-topics-combined-2.pdf", "2024-l2-topics-combined-2.pdf", "2024-l3-topics-combined-2.pdf"]
client = GrobidClient(config_path="./config.json")

def extract_text_from_xml(xml_string):
    root = ET.fromstring(xml_string)
    extracted_text = ""

    for p in root.findall(".//{http://www.tei-c.org/ns/1.0}p"):
        for s in p.findall(".//{http://www.tei-c.org/ns/1.0}s"):
            extracted_text += s.text.strip() + "\n"

    return extracted_text


if not os.path.exists("PyPDF"):
    os.makedirs("PyPDF")

if not os.path.exists("Grobid"):
    os.makedirs("Grobid")

for _path in path:
    pdf_reader = PdfReader(_path)

    data = _path.split("-")

    file=open(f"PyPDF/PyPDF_RR_{data[0]}_{data[1]}_combined.txt","a")

    for i in range(len(pdf_reader.pages)):
        page_pypdf = pdf_reader.pages[i].extract_text()
        file.writelines(page_pypdf)

    file.flush()
    file.close()

for _path in path:
    rsp = client.process_pdf("processFulltextDocument", _path, 
                            generateIDs=True, 
                            consolidate_header=True, 
                            consolidate_citations=True, 
                            include_raw_citations=True, 
                            include_raw_affiliations=True, 
                            tei_coordinates=True, 
                            segment_sentences=True)
    extracted_text = extract_text_from_xml(rsp[2])

    data = _path.split("-")

    with open(f"Grobid/Grobid_RR_{data[0]}_{data[1]}_combined.txt", "w", encoding="utf-8") as file:
        file.write(extracted_text)
        file.flush()
        file.close()
