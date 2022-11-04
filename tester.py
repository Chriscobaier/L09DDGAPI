from main import test_ddg0


# List of presidents
pres = ['George Washington', 'John Adams', 'Thomas Jefferson', 'James Madison', 'James Monroe', 'John Quincy Adams',
        'Andrew Jackson', 'Martin Van Buren',
        'William Henry Harrison', 'John Tyler', 'James K. Polk', 'Zachary Taylor', 'Millard Fillmore',
        'Franklin Pierce', 'James Buchanan', 'Abraham Lincoln',
        'Andrew Johnson', 'Ulysses S. Grant', 'Rutherford B. Hayes', 'James A. Garfield', 'Chester A. Arthur',
        'Grover Cleveland', 'Benjamin Harrison',
        'Grover Cleveland', 'William McKinley', 'Theodore Roosevelt', 'William Howard Taft', 'Woodrow Wilson',
        'Warren G. Harding', 'Calvin Coolidge',
        'Herbert Hoover', 'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower', 'John F. Kennedy',
        'Lyndon B. Johnson', 'Richard Nixon',
        'Gerald Ford', 'Jimmy Carter', 'Ronald Reagan', 'George H. W. Bush', 'Bill Clinton', 'George W. Bush',
        'Barack Obama', 'Donald Trump', "Joe Biden"]

# As of November 3rd 2022 there are 46 presidents
assert len(pres) == 46

# assuming no human interaction, otherwise query = userinput
query = 'presidents of the united states'

# Send to our API query, it returns json data
ddgData = test_ddg0(query)

# Empty list to store presidents
returnedData = []
# Loop all json data and format as needed for this specific scenario

# Just read that we have to use text..
#for i in ddgData:
#    data = i["FirstURL"]
#    formatData = data.split('m/', 1)[-1]
#    formatData = formatData.replace('_', ' ')
#    returnedData.append(formatData)
# if this gets populated then the president lost popularity contest
# loops all presidents, make sure all are in list of returned data
#loserPresidents = [x for x in pres if x not in returnedData]

for i in ddgData:
    data = i["Text"]
    returnedData.append(data)

# for all returned data text strings
for i in returnedData:
    #loop each president (alphabeical order helps runtime)
    for j in pres:
        #if president's name is in the list
        if j in i:
            #for each instance ... (Grover Cleveland's interupted two terms make it weird')
            while j in pres:
                #remove from list of presidents
                pres.remove(j)



assert len(pres) == 0

