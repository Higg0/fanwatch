#temporary, manual entry - need to figure out where I'm going to get this from

#just type them in
def get_sports():
    sports=[
        'NFL',
        'EPL'
        ]
    return sports
    

# copy paste list from ESPN (http://espn.go.com/nfl/schedule/_/week/4)
# edit to match format
def get_games():
    games=dict()
    games={
        'August 28, 2015':[
            ['New England', 'Carolina', '7:30 PM'],
    	    ['Detroit', 'Jacksonville', '8:00 PM'],
    	    ['Tennessee', 'Kansas City', '8:00 PM']],
        'August 29, 2015':[
        	['Pittsburgh', 'Buffalo', '4:00 PM'],
    	    ['Atlanta', 'Miami', '7:00 PM'],
    	    ['Cleveland', 'Tampa Bay', '7:00 PM'],
    	    ['Minnesota', 'Dallas', '7:00 PM'],
    	    ['NY Jets', 'NY Giants', '7:00 PM'],
    	    ['Chicago', 'Cincinnati', '7:30 PM'],
    	    ['Washington', 'Baltimore', '7:30 PM'],
    	    ['Seattle', 'San Diego', '8:00 PM'],
    	    ['Philadelphia', 'Green Bay', '8:00 PM'],
    	    ['Indianapolis', 'St. Louis', '8:00 PM'],
    	    ['San Francisco', 'Denver', '9:00 PM']],
    	'August 30, 2015':[
    	    ['Houston', 'New Orleans', '4:00 PM'],
    	    ['Arizona', 'Oakland', '8:00 PM']]}
    return games