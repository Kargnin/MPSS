
import sqlite3


# CONNECT TO DATABASE

DATBASE_LOCATION = "./StatsData.db"


def init():
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

# if conn.isOpen():
#     print("Database connected")

def get_globals():
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Globals")
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data

def update_globals(data):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    cur.execute("UPDATE Globals SET date = (?) ,invoice_number = (?) ",(data[0],data[1]))
    conn.commit()
    conn.close()


def insert_data(data,column_names,table_name):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    column_str = "("
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += ","

    column_str += str(column_names[-1])
    column_str += ")"

    values_str = "("
    for name in column_names[:-1]:
        values_str += "?"
        values_str += ","

    values_str += "?"
    values_str += ")"

    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''INSERT INTO {0} {1} 
             VALUES {2}'''.format(table_name,column_str,values_str)
    cur.execute(sql,data)
    conn.commit()
    conn.close()



def update_or_create(id_, data,column_names,table_name):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

    column_str = ""
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += " = (?) ,"

    column_str += str(column_names[-1])
    column_str += " = (?) "

    sql = '''UPDATE {0} 
             SET {1}
             WHERE rowid = (?)'''.format(table_name,column_str)

    tuple_ = []
    for d in data:
        tuple_.append(d)
    tuple_.append(str(id_))
    cur.execute(sql,tuple(tuple_))
    print("updated")
    conn.commit()
    conn.close()


def get_single_data(id_,table_name):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE rowid = (?)'''.format(table_name)
    str_id = str(id_)
    cur.execute(sql,str_id)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data


def get_multiple_data(table_name):
    """
    get document data by document ID
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* FROM {0}'''.format(table_name)
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return list(data)

#Fetchmany using invoice number
def get_multiple_data_invoice(id_,table_name):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE invoice_number = (?)'''.format(table_name)
    str_id = str(id_)
    cur.execute(sql,str_id)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return data

#Fetchmany using days 
def get_multiple_data_days(date,table_name):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    date_ = "Date"
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM {0}
             WHERE {1} = (?)'''.format(table_name,date_)
    str_id = str(date)
    cur.execute(sql,str_id)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    print(sql)
    print(date)
    print("Data: ")
    print(data)
    return data

#Update Stock
def update_existing_stock(vol,vendor,part,vehicle):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

    cur.execute('''UPDATE Stats 
             SET stock = stock - (?)
             WHERE vendor_name = (?) AND
             part_name = (?) AND
             vehicle_type = (?) ''',(vol,vendor,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

def update_existing_stock_add(vol,vendor,part,vehicle):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    # print(vol)
    # print(vendor)
    # print(part)
    # print(vehicle)
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

    cur.execute('''UPDATE Stats 
             SET stock = stock + (?)
             WHERE vendor_name = (?) AND
             part_name = (?) AND
             vehicle_type = (?) ''',(vol,vendor,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

#Update Threshold
def update_existing_Threshold(days,vol,part,vehicle):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

    cur.execute('''UPDATE Parts 
             SET Threshold = Threshold  + ((?)/(?))
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',(vol,days,part,vehicle))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True

def update_existing(id_, data,column_names,table_name):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

    column_str = ""
    for name in column_names[:-1]:
        column_str += str(name)
        column_str += " = (?) ,"

    column_str += str(column_names[-1])
    column_str += " = (?) "

    sql = '''UPDATE {0} 
             SET {1}
             WHERE rowid = (?)'''.format(table_name,column_str)


    tuple_ = []
    for d in data:
        tuple_.append(d)
    tuple_.append(str(id_))

    cur.execute(sql,tuple(tuple_))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True


def remove_data(id_,table_name):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    str_id = str(id_)
    cur.execute('''DELETE FROM {0} WHERE rowid = (?)'''.format(table_name),(str_id,))
    conn.commit()
    conn.close()

def remove_data_from_list(details,data,table_name):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    table_name = "Stats"
    tuple_ = []
    if len(details) == 1:
        sql = '''DELETE FROM {0} WHERE vendor_name = (?) AND part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        tuple_.append(details[0])
        tuple_.append(data[0])
        tuple_.append(data[1])
        print(tuple_)
        cur.execute(sql,tuple(tuple_))

    else:
        sql = '''DELETE FROM {0} WHERE vendor_name = (?) AND part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        tuple_.append(data[0])
        tuple_.append(details[0])
        tuple_.append(details[1])
        cur.execute(sql,tuple(tuple_))

    
    conn.commit()
    conn.close()

def remove_data_vendor_part(details,table_name):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    table_name = "Stats"
    tuple_ = []
    if len(details) == 1: #Vendor
        tuple_.append(details[0])
        cur.execute('''DELETE FROM Vendors WHERE name = (?)''',tuple(tuple_))
        sql = '''DELETE FROM {0} WHERE vendor_name = (?)'''.format(table_name)
        
        cur.execute(sql,tuple(tuple_))

    else:
        tuple_.append(details[0])
        tuple_.append(details[1])
        
        cur.execute('''DELETE FROM Parts WHERE part_name = (?) AND vehicle_type = (?)''',tuple(tuple_))
        sql = '''DELETE FROM {0} WHERE part_name = (?) AND vehicle_type = (?)'''.format(table_name)
        cur.execute(sql,tuple(tuple_))
    
    conn.commit()
    conn.close()


def get_threshold(details):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    tuple_ = []
    tuple_.append(details[0])
    tuple_.append(details[1])
    cur.execute('''SELECT Threshold FROM Parts
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',tuple(tuple_))
    data = cur.fetchone()
    conn.commit()
    conn.close()
    print(data)
    return int(data[0])

def get_stocksum(details):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    tuple_ = []
    tuple_.append(details[0])
    tuple_.append(details[1])
    cur.execute('''SELECT * FROM Stats
             WHERE part_name = (?) AND
             vehicle_type = (?) ''',tuple(tuple_))
    data = cur.fetchall()
    sum_ = 0
    for d in data:
        sum_ += int(d[3])

    conn.commit()
    conn.close()
    return sum_
# if __name__ == "__main__":
#     main()

def close():
    conn.commit()
    conn.close()
# CLOSE DATABASE
