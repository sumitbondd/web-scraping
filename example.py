import requests
import bs4

# response = request.get("link")
file_path = '/home/ubuntu/code/web-scraping/index.html'
with open ( file_path, 'r',encoding='utf-8')as f:
    html_content = f.read()

soup = bs4.BeautifulSoup(html_content, 'html.parser')

anchor_tag = soup.a
print(anchor_tag['href'])
print(anchor_tag.attrs)
