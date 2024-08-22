from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# 데이터 파일 경로
LINKS_FILE = 'data/links.json'

# 데이터 로드 함수
def load_links():
    if not os.path.exists(LINKS_FILE):
        return []
    with open(LINKS_FILE, 'r') as file:
        return json.load(file)

# 데이터 저장 함수
def save_links(links):
    with open(LINKS_FILE, 'w') as file:
        json.dump(links, file)

# 메인 페이지 라우트
@app.route('/')
def main_page():
    return render_template('main_page.html')

# 링크 추출 페이지 라우트
@app.route('/extract_links', methods=['GET', 'POST'])
def extract_links():
    if request.method == 'POST':
        text = request.form['text']
        links = load_links()
        new_links = extract_new_links(text, links)
        links.extend(new_links)
        save_links(links)
        return redirect(url_for('main_page'))
    return render_template('extract_links.html')

# 링크 관리 페이지 라우트
@app.route('/manage_links', methods=['GET', 'POST'])
def manage_links():
    links = load_links()
    if request.method == 'POST':
        used_link = request.form['used_link']
        mark_link_as_used(used_link, links)
        save_links(links)
    return render_template('manage_links.html', links=links)

# 사용 가능한 링크 제공 페이지 라우트
@app.route('/provide_links', methods=['GET'])
def provide_links():
    links = load_links()
    unused_links = [link for link in links if not link['used']]
    return render_template('provide_links.html', link=unused_links[0] if unused_links else None)

# 링크 추출 기능 (단순 예시)
def extract_new_links(text, existing_links):
    # 간단한 텍스트에서 링크 추출 예시
    potential_links = text.split()  # 텍스트를 공백으로 분리
    new_links = [link for link in potential_links if link not in existing_links]
    return [{'url': link, 'used': False} for link in new_links]

# 링크 사용 처리 기능 (단순 예시)
def mark_link_as_used(link, links):
    for item in links:
        if item['url'] == link:
            item['used'] = True
            break

if __name__ == '__main__':
    app.run(debug=True)
	