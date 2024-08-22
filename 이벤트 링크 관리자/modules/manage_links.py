def mark_link_as_used(used_link, links):
    """
    주어진 링크를 사용된 링크로 표시합니다.
    """
    for link in links:
        if link['url'] == used_link:
            link['used'] = True
            break

def add_or_mark_link(used_link, links):
    """
    입력된 링크가 리스트에 없으면 추가하고, 사용된 것으로 표시합니다.
    """
    # 링크가 이미 리스트에 있는지 확인
    for link in links:
        if link['url'] == used_link:
            link['used'] = True
            return
    
    # 링크가 리스트에 없으면 추가
    links.append({'url': used_link, 'used': True})