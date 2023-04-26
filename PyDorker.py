try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
print("""                                                                       
    ____        ____             __            
   / __ \__  __/ __ \____  _____/ /_____  _____
  / /_/ / / / / / / / __ \/ ___/ //_/ _ \/ ___/
 / ____/ /_/ / /_/ / /_/ / /  / ,< /  __/ /    
/_/    \__, /_____/\____/_/  /_/|_|\___/_/     
      /____/                                    
 
 [+] Author: Ph.Sk1d
 [+] Mindanao Cyber Army
 [+] Philippines Cyber Alliances
                                                                       """)
query = input("Enter your dork: ")
print('')
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)