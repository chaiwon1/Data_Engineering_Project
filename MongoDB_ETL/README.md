<h1>MongoDB ETL</h1>
<h2>개요</h2>


- 책 소개 페이지에서 데이터를 스크랩 후 DB에 적재.

- 스크랩되는 정보는 `title`, `price`, `rating`, `in stock`, `url`이다. 


- 스크랩하는 페이지는 <a href="http://books.toscrape.com/">books.toscrape.com이다. </a>


- 스크랩된 데이터는 localhost port:27017에 `books`라는 이름의 db에 `titles`라는 이름으로 적재된다. 
<br>

<h2>개발환경</h2>

`Python` 3.6 or above

그 외 package는 `requirements.txt` 확인

<br>


<h2>시행 결과</h2>
<p align="center"><img width=80% alt="스크린샷 2022-10-12 오후 1 02 20" src="https://user-images.githubusercontent.com/95471902/195249583-594b8f3e-995e-44c9-99b2-86c0b1b17a09.png"></p>
