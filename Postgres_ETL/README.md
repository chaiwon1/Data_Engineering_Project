<h1>Postgres ETL</h1>
<h2>개요</h2>
이번 프로젝트에서 파이썬을 이용하여 Postgres를 이용한 데이터 모델링과 ETL 파이프라인을 구현했다. 비지니스적인 활용을 위해 로그데이터와 노래데이터를 필요할 것으로 예상되는 테이블을 설계하고 DB에 적재하였다 

<br>

<h2>Song Dataset</h2>
노래데이터는 <a href="http://millionsongdataset.com">Million Song Dataset</a>의 일부를 가져왔다. 

데이터 샘플 :

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, 
"artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", 
"title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

<h2>Log Dataset</h2>
로그데이터는 <a href="https://github.com/Interana/eventsim">Event Simulator</a>를 통해 생성되었다. 

데이터 샘플 :

```
{"artist": null, "auth": "Logged In", "firstName": "Walter", "gender": "M", "itemInSession": 0, 
"lastName": "Frye", "length": null, "level": "free", "location": "San Francisco-Oakland-Hayward, CA", 
"method": "GET","page": "Home", "registration": 1540919166796.0, "sessionId": 38, "song": null, 
"status": 200, "ts": 1541105830796, "userAgent": "\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"", 
"userId": "39"}
```

<br>


<h2>Schema</h2>

<p align="center"><img alt="schema" src="https://user-images.githubusercontent.com/95471902/195243526-a690f181-3135-4941-a8c6-35b1861eaccb.png"></p>

<h4>Fact Schema</h4>

songplays - 로그데이터 안의 노래 재생과 관련된 데이터

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

<h4>Dimension Tables</h4>
users - 서비스를 이용하는 user들과 관련된 데이터

```
user_id, first_name, last_name, gender, level
```

songs - 노래데이터 안의 노래들과 관련된 데이터

```
song_id, title, artist_id, year, duration
```

artists - 노래데이터 안의 가수들과 관련된 데이터

```
artist_id, name, location, latitude, longitude
```

time - `songplays` 테이블 안의 `start_time` 필드를 잘게 쪼갠 타임스탬프 데이터

```
start_time, hour, day, week, month, year, weekday
```

<br>


<h2>Project Files</h2>

`sql_queries.py` ->  fact table과 dimension table 생성 쿼리와 insert 쿼리.

`create_tables.py` -> DB 생성 및 테이블 생성 코드.

`etl.ipynb` -> 데이터 로드 전 데이터 확인용 jupyter notebook.

`etl.py` -> 노래데이터와 로그데이터 로드와 적재.

`test.ipynb` -> 데이터 적재 확인용 jupyter notebook.


<br>


<h2>개발환경</h2>

`Python` 3.6 or above

`PostgresSQL` 9.5 or above

`psycopg2` - PostgreSQL database adapter for Python


<br>


<h2>시행 결과</h2>
<p align="center"><img alt="스크린샷 2022-10-12 오후 12 52 59" src="https://user-images.githubusercontent.com/95471902/195246167-babe7479-ba4f-4475-8815-0cae15c27d1c.png"></p>



