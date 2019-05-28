import psycopg2
db = psycopg2.connect("dbname=news")


query1 = "select title, count(*) as views from articles join log on articles.slug = substring(log.path,10) group by title order by views desc limit 3;"
query_result1 = dict()
query_result1['title'] = '\nAll articles\n'

query2 = "select authors.name, count(*) as views from authors join articles on articles.author = authors.id join log on articles.slug = substring(log.path,10) group by authors.name order by views desc limit 3;"
query_result2 = dict()
query_result2['title'] = '\nAll articles\n'

#query3 = "select round(numstatus*100.0/visitors, 2) as percentage1, to_char(day2, 'Mon DD, YYYY') from errorsum order by percentage1 limit 1"

query3 = "select round((numstats*100.0)/visitors, 3) as result, to_char(day2, 'Mon DD, YYYY') FROM errorsum ORDER BY result desc limit 1"
query_result3 = dict()
query_result3['title'] = '\nAll articles\n'



def get_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def print_query(query_results):
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views ')

query_result1['results'] = get_query(query1)
print_query(query_result1)
query_result2['results'] = get_query(query2)
print_query(query_result2)
query_result3['results'] = get_query(query3)
print_query(query_result3)
