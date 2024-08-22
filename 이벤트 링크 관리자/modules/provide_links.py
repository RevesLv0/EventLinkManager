def get_next_unused_link(links):
    """
    사용되지 않은 첫 번째 링크를 반환합니다.
    """
    for link in links:
        if not link['used']:
            return link
    return None

def mark_current_link_as_used(link, links):
    """
    현재 표시된 링크를 사용된 것으로 표시합니다.
    """
    for item in links:
        if item['url'] == link['url']:
            item['used'] = True
            break

def undo_last_link(links):
    """
    마지막으로 사용된 링크를 다시 사용하지 않은 것으로 되돌립니다.
    """
    for link in reversed(links):
        if link['used']:
            link['used'] = False
            break