import re

def extract_new_links(text, existing_links):
    """
    입력된 텍스트에서 링크를 추출하고,
    이미 존재하지 않는 새로운 링크들만 반환합니다.
    """
    # 간단한 링크 패턴 (http/https로 시작하는 URL)
    pattern = r'(https?://\S+)'
    
    # 정규 표현식으로 텍스트에서 모든 링크를 추출
    potential_links = re.findall(pattern, text)
    
    # 중복 제거 및 새로운 링크 필터링
    new_links = [link for link in potential_links if link not in existing_links]
    
    # 새로운 링크들을 리스트로 반환 (딕셔너리 형식)
    return [{'url': link, 'used': False} for link in new_links]