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

<div>
  <div>
    <b>
      Java, SpringBoot, SpringDataJPA를 이용해 RestAPI를 개발합니다.
      <p></p>
      JavaScript, HTML/CSS, React로 간단한 프론트엔드 개발도 가능합니다.
      <p></p>
      ERD를 설계하고, MySQL 및 NoSQL 을 사용할 수 있습니다.
      <p></p>
      현재 신입 백엔드 개발자로 구직중입니다.
    </b>
  </div>
<br>
</div>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ehgur062300&hide=css,HTML&exclude_repo=ehgur062300.github.io&layout=compact&theme=tokyonight" alt="Top Languages" width="33%">

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=ehgur062300)](https://solved.ac/ehgur062300/)  

## 🦾 Skills
| **🌐Languages** | **🖥️Backend**     | **💾Databases** | **☁️Cloud & DevOps** | **🛠️Tools & Others** |
|-----------------|-------------------|-----------------|-----------------------|-----------------------|
| <p align="center"><img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=java&logoColor=white"></p>          | <p align="center"><img src="https://img.shields.io/badge/JPA-6DB33F?style=flat-square&logo=spring&logoColor=white"></p> | <p align="center"><img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"></p>         | <p align="center"><img src="https://img.shields.io/badge/Amazon%20AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white"></p> | <p align="center"><img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"></p> |
|                 | <p align="center"><img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white"></p> | <p align="center"><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"></p>         | <p align="center"><img src="https://img.shields.io/badge/S3-569A31?style=flat-square&logo=amazon-s3&logoColor=white"></p> |                       |
|                 |                   |                 | <p align="center"><img src="https://img.shields.io/badge/RDS-527FFF?style=flat-square&logo=amazon-rds&logoColor=white"></p> |                       |
|                 |                   |                 | <p align="center"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"></p> |                       |


## 💻 DEV's Blog 💻
<a href="https://autoreview.kr/"><img src="https://img.shields.io/badge/AutoReview-FFA500?style=flat-square"></a>
<a href="https://backend-repository.tistory.com/" target="_blank">
  <img src="https://img.shields.io/badge/Tistory-f54?style=flat-square&logo=Tistory&logoColor=white"/>
</a>

"""

resultREADME = f"{preREADME}{markdown_text}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
f.close()
