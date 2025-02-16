import requests
import json

# Figma API 설정
FIGMA_FILE_ID = "wzuz5loypUCjBClXQXl3OA"  # 변환할 Figma 파일의 ID
ACCESS_TOKEN = ""  # Figma에서 발급받은 API 토큰

# API 요청 URL
FIGMA_API_URL = f"https://api.figma.com/v1/files/{FIGMA_FILE_ID}"

# API 호출
headers = {"X-Figma-Token": ACCESS_TOKEN}
response = requests.get(FIGMA_API_URL, headers=headers)

# JSON 데이터 가져오기
if response.status_code == 200:
    figma_data = response.json()
    with open("figma_data.json", "w", encoding="utf-8") as f:
        json.dump(figma_data, f, indent=4)
    print("✅ Figma 데이터 저장 완료!")
else:
    print(f"❌ API 요청 실패! 상태 코드: {response.status_code}")
