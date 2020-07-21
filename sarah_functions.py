import datetime
import string
import numpy as np

def remove_punctuation(str1): 
    
    for char in str1.lower():
        
        if char in string.punctuation: 
            
            str1 = str1.replace(char,"")          
    
    return str1

def unique_word_calc(str1):
    
    text_str = str(str1).lower()
    no_punct_str = remove_punctuation(text_str)

    d = {} # initialize an empty dictionary
    for word in no_punct_str.split():
        try:
            d[word] += 1 # the entry exists
        except KeyError:
            d[word] = 1 # a new entry
        
    return len(d.keys())

def total_word_calc(str1): 
    
    text_str = str(str1).lower()
    no_punct_str = remove_punctuation(text_str)
    lst_wrds = no_punct_str.split()
    
    return len(lst_wrds)
    
def day_week(date):
    
    '''When given a date, this function returns the corresponding day of the week.'''
    
    weekdays= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    year=int(date.split('-')[0])
    month=int(date.split('-')[1])
    day = int(date.split('-')[2])
    
    dt=datetime.datetime(year,month,day)
    
    return weekdays[dt.weekday()]

def time_day(time):
    
    """When given a specific time (hours,minuites,seconds), this function returns the hour"""
    
    Hours = ['12:00 AM', '1:00 AM','2:00 AM','3:00 AM','4:00 AM','5:00 AM','6:00 AM',
                 '7:00 AM','8:00 AM','9:00 AM','10:00 AM','11:00 AM', '12:00 PM',
                 '1:00 PM', '2:00 PM','3:00 PM','4:00 PM','5:00 PM','6:00 PM',
                 '7:00 PM','8:00 PM','9:00 PM','10:00 PM','11:00 PM']
        
    times = time.split(':')[0]
    times = times.rstrip()
        
    if times == '00':
        hour = Hours[0]
        
    elif times == '01':  
        hour = Hours[1]
        
    elif times == '02':  
        hour = Hours[2]
        
    elif times == '03':
        hour = Hours[3]
    
    elif times == '04':  
        hour = Hours[4]
        
    elif times == '05':
        hour = Hours[5]
        
    elif times == '06':
        hour = Hours[6]
        
    elif times == '07': 
        hour = Hours[7]
        
    elif times == '08':   
        hour = Hours[8]
        
    elif times == '09':
        hour = Hours[9]
        
    elif times == '10': 
        hour = Hours[10]
        
    elif times == '11':
        hour = Hours[11]
        
    elif times == '12':
        hour = Hours[12]
        
    elif times == '13': 
        hour = Hours[13]
        
    elif times == '14':
        hour = Hours[14]
        
    elif times == '15':
        hour = Hours[15]
        
    elif times == '16': 
        hour = Hours[16]
        
    elif times == '17':
        hour = Hours[17]
        
    elif times == '18':
        hour = Hours[18]
        
    elif times == '19': 
        hour = Hours[19]
        
    elif times == '20':
        hour = Hours[20]
        
    elif times == '21':
        hour = Hours[21]
        
    elif times == '22': 
        hour = Hours[22]
        
    elif times == '23':
        hour = Hours[23]
        
    elif times == '24':
        hour = Hours[24]
        
    else: 
        hour = np.nan
            
    return hour