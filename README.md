# Geneie (The Gene Searcher) 
## Purpose 
This is a program that searches wikipedia and mousmine for genes you provide in a list. It then makes an excel file to review the results.

## Inspiration 
I was tasked with searching for information on a list of 500+ genes (obtained from genearray data). I needed tounderstand which were related to the NFkB immunological pathway. The act of searching manually seemed like a task worth automating.  Since we get lots of gene data this program can be used in the fiture to contine to automate the process of gathering information for manual review.

## Required Modules
 - openpyxl 
 - wikipedia
 - argparse
 - intermine

## Sample Usage: 
 - ./genie.py -i genelist.txt -o my.search.results

## Sample Gene File: 
 - Included file "**genelist.txt**" is a sample of genes you can use for the program
 - You need to specify INPUT data via argument on the command line.  The program is expecting a simple text file of one gene per line. 
 
## What's inside: 
 - README.md  
 - genelist.long.txt: Example list of genes to search for. 
 - genelist.short.txt: Short example list of genes to search for. 
 - genie.py: The main program.  
 - mouseminesearch.py: Modified code partially sourced from [Mousemine.org's Search Tool](http://www.mousemine.org/mousemine/template.do?name=Organism_genes&scope=global) and used as the function "genefind" imported into the primary program. 

 
