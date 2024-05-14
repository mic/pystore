import psycopg2
import sys

def main():
    conn_string = "host='postgres' dbname='slackbot' user='mic' password='test'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")
    # Add your database operations here

if __name__ == "__main__":
    main()