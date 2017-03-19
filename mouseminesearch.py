#!/usr/local/bin/python3

# modified script provided by intermine, turned into a function
# Their search function online gives you reference python code, which is awesome of them

# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/
#     http://www.mousemine.org/mousemine/template.do?name=Organism_genes&scope=global

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://www.mousemine.org/mousemine/service")

def genefind(x,y):
 returnrow="Nothing"
 # Get a new query on the class (table) you will be querying:
 query = service.new_query("Gene")
 # The view specifies the output columns
 query.add_view(
    "primaryIdentifier", "symbol", "name", "sequenceOntologyTerm.name",
    "organism.name"
 )
 # This query's custom sort order is specified below:
 query.add_sort_order("Gene.symbol", "ASC")
 # You can edit the constraint values below
 query.add_constraint("symbol", "=",x, code = "B")
 #query.add_constraint("symbol", "CONTAINS",x, code = "B")
 query.add_constraint("organism.name", "=", y, code = "A")
 # Uncomment and edit the code below to specify your own custom logic:
 # query.set_logic("B and A")

 for rows in query.rows():
  returnrow=rows
  break #I only want the first search result.  This is probably an odd way of doing it, but what came to me first. 

 if returnrow=='Nothing':
   #give pseudogene a try
   query = service.new_query("Pseudogene")
   # The view specifies the output columns
   query.add_view(
      "primaryIdentifier", "symbol", "name", "sequenceOntologyTerm.name",
      "organism.name"
   )
   # This query's custom sort order is specified below:
   query.add_sort_order("Pseudogene.symbol", "ASC")
   # You can edit the constraint values below
   query.add_constraint("symbol", "=",x, code = "B")
   #query.add_constraint("symbol", "CONTAINS",x, code = "B")
   query.add_constraint("organism.name", "=", y, code = "A")
   # Uncomment and edit the code below to specify your own custom logic:
   # query.set_logic("B and A")
   for rows in query.rows():
    returnrow=rows
    break 


 return returnrow

#print(query.rows)
#    print (row["primaryIdentifier"], row["symbol"], row["name"], row["sequenceOntologyTerm.name"], \
#        row["organism.name"])
#  return

#make url after being sent row["primaryIdentifier"]
def jaxify(x):
 y=str(x)
 jaxurl='http://www.informatics.jax.org/marker/'+y
 return jaxurl
 
#make url after being sent row["id"] from genefind
def mouselink(x):
 y=str(x)
 mouseurl='http://www.mousemine.org/mousemine/report.do?id='+y
 return mouseurl
