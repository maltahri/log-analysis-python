#!Import for postreSQL
import psycopg2


def fire_query(q):
    # Connect the database
    db = psycopg2.connect(database='news')
    # Pointer
    c = db.cursor()
    # Excecute the query
    c.execute(q)
    data = c.fetchall()
    db.close()
    return data


def find_populer_articles():
    query = ("""
    SELECT a.title, count(*) AS total
     FROM articles as a join log as l ON
      l.path = concat('/article/',a.slug)
       group by a.title order by total DESC LIMIT 3;
        """)
    res = fire_query(query)
    print '******************Top 3 Articles**************'
    for title, total in res:
        print '"%s" Article is populer with %s numbers.' % (title, total)
    pass


def find_article_authors():
    query = """
            SELECT a.name, COUNT(*) AS total
             FROM authors as a
              JOIN articles as t
               ON a.id = t.author
                JOIN log ON log.path = concat
                ('/article/', t.slug) GROUP BY a.name
                 ORDER BY total DESC
                  LIMIT 3;
        """
    res = fire_query(query)
    print '********************Top 3 Authors****************'
    for author_name, total in res:
        print '"%s" is populer with %s numbers.' % (author_name, total)


def find_error_days():
    query = """
        SELECT n.day,
          ROUND(((e.error*1.0) / n.request), 3) AS p
           FROM (SELECT date_trunc('day', time) "day",
            count(*) AS error FROM log WHERE status LIKE '404%'
             GROUP BY day ) AS e
        JOIN (SELECT date_trunc('day', time) "day", count(*) AS request
         FROM log
          GROUP BY day) AS n ON n.day = e.day
           WHERE (ROUND(((e.error*1.0) / n.request), 3) > 0.01)
            ORDER BY p DESC;
    """
    res = fire_query(query)
    print('******Days on which >1% HTTP requests returned 404 errors*******')
    for res_date, http_404 in res:
        error_date = res_date.strftime('%d - %m- %Y')
        errors = str(round(http_404*100)) + '%'
        print '"%s" is date with %s errors.' % (error_date, errors)


if __name__ == "__main__":
    find_populer_articles()
    print '\n\n'
    find_article_authors()
    print '\n\n'
    find_error_days()
