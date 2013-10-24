import math
import datetime
from dateutil.relativedelta import *

todays_date = datetime.datetime.now()

# generate some pageviews data
total = 5068503557;
pv_per_day = total / 365;
av_time_per_page = 60;


max_pv_wobble=pv_per_day * 0.1
max_t_wobble=av_time_per_page * 0.02

def generate_pageview_data(period):
    return generate_data(period,'pageviews',pv_per_day,max_pv_wobble)

def generate_timespent_data(period):
    return generate_data(period,'timespent',av_time_per_page,max_t_wobble)
    
def generate_data(period,name,value,wobble):
    
    if period.lower() == 'last month':
        start_date = todays_date + relativedelta(months=-1)
        units=abs((todays_date-start_date).days)
        x_dates=[start_date+datetime.timedelta(days=n) for n in range(units)]
        x_labels=[x.strftime("%d-%m-%Y") for x in x_dates]

    elif period.lower() == 'last quarter':
        start_date = todays_date + relativedelta(months=-3)
        units=abs((todays_date-start_date).days)
        x_dates=[start_date+datetime.timedelta(days=n) for n in range(units)]
        x_labels=[x.strftime("%d-%m-%Y") for x in x_dates]

    elif period.lower() == 'last year':
        #switch to monthlies
        start_date = todays_date + relativedelta(months=-12)
        units = 12
        x_dates=[start_date+datetime.timedelta(days=math.ceil((365.0/12.0)*n)) for n in range(units)]
        x_labels=[x.strftime("%m-%Y") for x in x_dates]
        value=value*30
    else:
        units=1
        x_labels=['null']
    
                
    data = {name:{'x':[],'y':[],'x_labels':x_labels}}
    data[name]['x'] = [x+1 for x in range(units)]
    data[name]['y'] = [value + (wobble*(math.sin(math.pi*((x%7)/7.0)-0.5))) 
                for x in data[name]['x']]
    print period.lower(),start_date,units,data
    return data