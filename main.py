## update_blogPost.py
import feedparser, time

blog_url = "https://backend-repository.tistory.com/feed"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""
markdown_text = """
## ✅ Latest Blog Post

"""
for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  else:
        feed_date = entrie['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {entrie['title']}]({entrie['link']}) <br/>\n"

preREADME = """

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fehgur062300&count_bg=%23575554&title_bg=%23000000&icon=github.svg&icon_color=%23FFFFFF&title=Github&edge_flat=false)](https://hits.seeyoufarm.com)

## 📞 Contact 📞
<div>
  <a href="mailto:ehgur062300@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/ehgur062300@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=black"/>
  </a>
  <a href="https://open.kakao.com/o/sRzRHFZf" target="_blank">
    <img src="https://img.shields.io/badge/KakaoTalk-FFCD00?style=flat-square&logo=KakaoTalk&logoColor=black"/>
  </a>
</div>
<br>
<div align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ehgur062300&hide=css,HTML&exclude_repo=ehgur062300.github.io&layout=compact&theme=tokyonight" alt="Top Languages" width="37%" align="right">
  <div align="left">
    <b>
      Java, SpringBoot, SpringDataJPA를 이용해 RestAPI를 개발합니다.
      <p></p>
      JavaScript, TypeScript, HTML/CSS, React로 간단한 프론트엔드 개발도 가능합니다.
      <p></p>
      ERD를 설계하고, MySQL 및 NoSQL 을 사용할 수 있습니다.
      <p></p>
      현재 신입 백엔드 개발자로 구직중입니다.
    </b>
  </div>
<br>
</div>

## 🦾 Skills
### Languages
<div>
  <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=java&logoColor=white">
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
</div>

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=ehgur062300)](https://solved.ac/ehgur062300/)  

### Framework
<div>
  <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white">
  <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white">
</div>

### Tools
<div>
  <img src="https://img.shields.io/badge/oracle-F80000?style=flat-square&logo=oracle&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazon aws&logoColor=white">
  <img src="https://img.shields.io/badge/IntelliJ IDEA-000000?style=flat-square&logo=intellij-idea&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white">
</div>

## 💻 DEV's log 💻
<a href="#"><img src="https://img.shields.io/badge/Portfolio-FFC0CB?style=flat-square"></a>
<a href="https://velog.io/@ehgur062300/posts" target="_blank">
  <img src="https://img.shields.io/badge/Velog-20C997?style=flat-square&logo=Velog&logoColor=white"/>
</a>
<a href="https://backend-repository.tistory.com/" target="_blank">
  <img src="https://img.shields.io/badge/Tistory-f54?style=flat-square&logo=Tistory&logoColor=white"/>
</a>

"""

resultREADME = f"{preREADME}{markdown_text}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
f.close()
