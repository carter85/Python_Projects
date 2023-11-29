bank = ['noun','noun','adjective','noun','verb','verb ending with -ing',
    'verb ending with -ing','adjective',
    'job','candy','adjective','adjective']

for index in range(len(bank)):    
    bank[index] = input( f"Please choose a {bank[index]}:\n" )
    
story = f"""
On Halloween, you get to go trick-or-treating! Everyone will dress up in costumes, 
like a/an {bank[0]} or a/an {bank[1]}. This year, you decided to dress up as a/an 
{bank[2]} {bank[3]}. Your mom takes you and your best friend trick-or-treating. While you 
are out, your dad stays at home and {bank[4]}. Other fun things to do on Halloween are 
{bank[5]} scary movies and {bank[6]}. This year, you get lots of {bank[7]} candy! When you 
get home, your dad says he wants some, because he works hard as a {bank[8]} and he 
deserves some of your {bank[9]}. You are {bank[10]} but you give it to him anyway. 
Dads are so {bank[11]} but you love him!
"""

print(story)