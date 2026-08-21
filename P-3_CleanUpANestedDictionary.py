''' Write a Python program to clean up a nested dictionary 
(representing countries, states, and cities) by removing any 
empty lists from the lowest-level values. '''

def del_empty_dict(data):
    result = {}
    for key, value in data.items():

        if isinstance(value, dict):
            value = del_empty_dict(value)

        if value:
            result[key] = value

    return result

data = {'India':{'MP':['Indore','Ujjain'],
        'Maharastra':[],
        'Gujarat':['Surat','Ahmedabad'],
        },
    'USA':{'California':[' Los Angeles', 'San Francisco', 'San Diego'],
        'Texas':['Austin', 'Dallas'],
        'New York':[],
        },
    'UK':{'test_state':[]}
    }

print("\nNew Dictionary is :\n",del_empty_dict(data))

                
               