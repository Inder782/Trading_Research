import datetime 

def convert_date(date):
    date_object=datetime.datetime.strptime(date,"%d-%m-%Y")
    timestamp=date_object.isoformat()
    return timestamp