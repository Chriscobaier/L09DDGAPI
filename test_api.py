import pytest
import requests

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



def test_length_of_list():
    assert len(pres) == 46

def test_ddg0():
    url_ddg = "https://api.duckduckgo.com"

    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json&pretty=1&nohtml=1")
    rsp_data = resp.json()
    # print(rsp_data)
    goodData = rsp_data["RelatedTopics"]
    # for i in goodData:
    # print(i["FirstURL"])

    # Loop all json data and format as needed for this specific scenario

    # Just read that we have to use text.
    # for i in goodData:
    #    data = i["FirstURL"]
    #    formatData = data.split('m/', 1)[-1]
    #    formatData = formatData.replace('_', ' ')
    #    returnedData.append(formatData)
    # if this gets populated then the president lost popularity contest
    # loops all presidents, make sure all are in list of returned data
    # loserPresidents = [x for x in pres if x not in returnedData]


    returnedData = []
    for i in goodData:
        data = i["Text"]
        returnedData.append(data)
        
    # if this remains populated then the president lost popularity contest, or code is bad
    loserpresidents = pres
    # for all returned data text strings
    for i in returnedData:
        # loop each president (alphabetical order helps runtime)
        for j in loserpresidents:
            # if president's name is in the list
            if j in i:
                # for each instance ... (Grover Cleveland's interrupted two terms make it weird')
                while j in loserpresidents:
                    # remove from list of presidents
                    loserpresidents.remove(j)
    
    assert len(loserpresidents) == 0
