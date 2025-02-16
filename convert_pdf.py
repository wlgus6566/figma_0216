import pdfplumber
import json

pdf_path = "assets/NHN_Coding_Conventions_for_Markup_Languages.pdf"
json_output_path = "assets/NHN_Coding_Conventions.json"

# PDF에서 텍스트 추출
extracted_text = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        extracted_text.append(page.extract_text())

# JSON 변환
data = {"NHN_Coding_Conventions": "\n".join(extracted_text)}

# JSON 파일로 저장
with open(json_output_path, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON 파일이 생성되었습니다: {json_output_path}")
