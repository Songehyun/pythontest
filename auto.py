import subprocess
import re

# 질문 목록 준비
questions = [
    "파이썬을 새로 배우려고해 자바스크립트와 비교해서 설명해줘. 한국어로",
    "파이썬의 기초적인 정보들을 나에게 알려줘. 한국어로",
    "파이썬에 익숙해지기 위해서 몇가지 코드를 작성해보려고 해, 익숙해지기 위한 초보자용 연습문제를 만들어줄래? 한국어로",
]

# 각 질문에 대한 답변을 개별 파일에 저장
for idx, question in enumerate(questions, start=1):
    print(f"Processing question {idx}: {question}")
    
    # Ollama 명령 실행
    result = subprocess.run(
        ["ollama", "run", "llama3:8b", question], 
        capture_output=True, text=True, encoding='utf-8'
    )
    
    # 오류 확인
    if result.returncode != 0:
        print(f"Error with question {idx}: {result.stderr}")
        continue

    # 파일명 생성 (문장 앞 부분만 사용)
    # "." 또는 "?" 앞의 내용을 추출
    title = re.split(r'[.?]', question)[0]
    # 파일명을 안전하게 하기 위해 공백을 "_"로 치환
    safe_title = re.sub(r'\s+', '_', title)
    
    # 파일명 지정 (질문에서 생성한 safe_title 사용)
    file_name = fr"C:\Users\Administrator\Desktop\ollama\{safe_title}.md"
    
    # 답변을 파일로 저장
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Question: {question}\n\n")
        file.write(f"Answer:\n{result.stdout}\n")
    
    print(f"Saved answer {idx} to {file_name}")