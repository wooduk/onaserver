import math


# generate some pageviews data
total = 5068503557;
pv_per_day = total / 365;
av_time_per_page = 60;

max_pv_wobble=pv_per_day * 0.1
max_t_wobble=av_time_per_page * 0.02

def generate_pageview_data(units):
    return generate_data(units,'pageviews',pv_per_day,max_pv_wobble)

def generate_timespent_data(units):
    return generate_data(units,'timespent',av_time_per_page,max_t_wobble)
    
def generate_data(units,name,value,wobble):
    data = {name:{'x':[],'y':[]}}
    data[name]['x'] = [x+1 for x in range(units)]
    data[name]['y'] = [value + (wobble*(math.sin(math.pi*((x%7)/7.0)-0.5))) 
                for x in data[name]['x']]
    return data