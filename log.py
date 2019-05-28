import psycopg2
db = psycopg2.connect("dbname=news")

query1 = "SELECT title, count(*) AS views FROM articles JOIN log ON articles.slug = substring(log.path,10) GROUP BY title ORDER BY views DESC LIMIT 3;"
query_result1 = dict()
query_result1['title'] = '\nAll articles\n'

query2 = "SELECT authors.name, count(*) AS views FROM authors JOIN articles ON articles.author = authors.id JOIN log ON articles.slug = substring(log.path,10) GROUP BY authors.name ORDER BY views DESC LIMIT 3;"
query_result2 = dict()
query_result2['title'] = '\nAll articles\n'

query3 = "SELECT to_char(day2, 'Mon DD, YYYY'), round((numstats*100.0)/visitors, 3) AS result FROM errorsum ORDER BY result DESC LIMIT 1"
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
        print ('\t' + str(result[0]) + ' ---- ' + str(result[1]) + ' views')

def print_3rd_query(query_results):
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ' ---- ' + str(result[1]) + '% errors')

query_result1['results'] = get_query(query1)
print_query(query_result1)
query_result2['results'] = get_query(query2)
print_query(query_result2)
query_result3['results'] = get_query(query3)
print_3rd_query(query_result3)
