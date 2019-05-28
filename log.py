import psycopg2

query1 = "SELECT title, count(*) AS views FROM articles JOIN log ON articles.slug = substring(log.path,10) GROUP BY title ORDER BY views DESC LIMIT 3;" #First query
#Which articles have been accessed the most?
#Presenting this information as a sorted list with the most popular article at the top
query_result1 = dict() #Creating a dict object
query_result1['title'] = '\nAll articles\n'

query2 = "SELECT authors.name, count(*) AS views FROM authors JOIN articles ON articles.author = authors.id JOIN log ON articles.slug = substring(log.path,10) GROUP BY authors.name ORDER BY views DESC LIMIT 3;" #Second query
#Who are the most popular article authors of all time?
#when you sum up all of the articles each author has written, which authors get the most page views?
#Presenting this as a sorted list with the most popular author at the top.
query_result2 = dict()
query_result2['title'] = '\nAll articles\n'

query3 = "SELECT to_char(day2, 'Mon DD, YYYY'), round((numstats*100.0)/visitors, 3) AS result FROM errorsum ORDER BY result DESC LIMIT 1" #Third query
#On which days did more than 1% of requests lead to errors?
query_result3 = dict()
query_result3['title'] = '\nAll articles\n'

def get_query(query): #Function to get query
    db = psycopg2.connect("dbname=news") #Connecting to the database
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close() #Closing the database
    return results #Returning the results

def print_query(query_results): #Printing first and second queries
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ' ---- ' + str(result[1]) + ' views') #Printing the first two parts of the result

def print_3rd_query(query_results): #Printing third query
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ' ---- ' + str(result[1]) + '% errors') #Printing as % error

query_result1['results'] = get_query(query1) #Getting the query and storing in the dict object
print_query(query_result1) #Printing the dict object
query_result2['results'] = get_query(query2)
print_query(query_result2)
query_result3['results'] = get_query(query3)
print_3rd_query(query_result3)
