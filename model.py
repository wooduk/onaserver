# values taken from spreadsheet for 2012/13 analysis

DEVICE_TYPES = ['desktop','laptop','tablet','smartphone','ereader']

proportion_of_pageviews = {
    'desktop':0.354, 
    'laptop':0.254,
    'tablet':0.171,
    'smartphone':0.211,
    'ereader':0.001
    }

power_consumption = {
    # Watts
    'desktop':114, 
    'laptop':27+24,
    'tablet':3,
    'smartphone':1,
    'ereader':0.01
}    

download_energy = {
    # Joules
    'desktop':50, 
    'laptop':50,
    'tablet':20,
    'smartphone':20,
    'ereader':2
}

#C1i = tau_i * phi_i
#C2i = rho_i * phi_i

# phi_i = proportion that device type 'i' makes of total pageviews 
# rho_i = power consumption of device type 'i'
# tau_i = energy required to download page content for device 'i'

def device_multiply(q1,q2):
    s=[]
    for device in DEVICE_TYPES:
        s.append(q1[device]*q2[device])
    return s
         
# User devices
C1 = sum(device_multiply(download_energy, proportion_of_pageviews))
C2 = sum(device_multiply(power_consumption, proportion_of_pageviews))

# Origin Servers as proportion of user device energy
C3 = 0.047680113

# 3rd Party Servers as proportion of user device energy
C4 = 0.003751395

# Shared Network as proportion of user device energy
C5 = 0.073034502 + 0.297165569 + 0.015906306

# servers = pageviews*(% of page size) * conversion_factor
# obtained from analysis of web page?
servers = [
        {'name':'guardian.com', 'd':0.2,'c':1},
        {'name':'interroute', 'd':0.25,'c':1},
        {'name':'akamai', 'd':0.1,'c':1},
        {'name':'cdnNetworks', 'd':0.1,'c':1},
        {'name':'Level 3', 'd':0.1,'c':1},
        {'name':'AWS', 'd':0.1,'c':1},
        {'name':'GAE', 'd':0.1,'c':1},
        {'name':'other', 'd':0.05,'c':1}
        ]
 
udevices = [
    {'name':'desktop','d':0,'c':0},
    {'name':'laptop','d':0,'c':0},
    {'name':'tablet','d':0,'c':0},
    {'name':'mobile','d':0,'c':0},
    {'name':'other','d':0,'c':0}
    ]
    

d_param = { 
            'C1':C1,
            'C2':C2,
            'C3':C3,
            'C4':C4,
            'C5':C5,
            'servers':servers,
            'udevices':udevices
        }





    