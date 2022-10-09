import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# Create DB first
def create_database() :

    # connect to default database
    conn = psycopg2.connect(
                            host="127.0.0.1",
                            database="defaultdb",
                            user="chaiwonhyun",
                            password="chaiwon1"
                            )
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    print("디폴트DB에 접속하였습니다.")

    # drop and create sparkifydb
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    print("sparkifydb를 삭제하였습니다.")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    print("sparkifydb를 생성하였습니다.")

    conn.close()

    # connect to sparkifydb
    conn = psycopg2.connect(
                            host="127.0.0.1",
                            dbname="sparkifydb",
                            user="chaiwonhyun" ,
                            password="chaiwon1"
                            )
    cur = conn.cursor()
    print("sparkifydb에 접속하였습니다.")

    # return sparkifydb's cursor and connect
    return cur, conn


# If there are tables, drop the tables
def drop_tables(cur, conn) :
    for q in drop_table_queries :
        cur.execute(q)
        conn.commit()

# Create tables 
def create_tables(cur, conn) :
    for q in create_table_queries :
        cur.execute(q)
        conn.commit()
    

def main() :
    cur, conn = create_database()
    print("DB를 생성하고 접속하였습니다.")

    drop_tables(cur, conn)
    print("테이블들을 삭제하였습니다.")

    create_tables(cur, conn)
    print("테이블들을 생성하였습니다.")

    conn.close()

if __name__== "__main__" :
    main()