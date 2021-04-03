
import sqlite3


# CONNECT TO DATABASE
DATBASE_LOCATION = "D:\\StatsData.db"

def init():
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()

# if conn.isOpen():
#     print("Database connected")



def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''INSERT INTO Vendors (Name,Address,Contact) 
             VALUES (?,?,?)'''
    cur.execute(sql,data)
    conn.commit()
    conn.close()



def update_or_create(id_, data):
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
    sql = '''UPDATE Vendors 
             SET Name = (?) ,
                 Address = (?), 
                 Contact = (?) 
             WHERE rowid = (?)'''
    tuple_ = (data[0],data[1],data[2],str(id_))
    cur.execute(sql,tuple_)
    print("updated")
    conn.commit()
    conn.close()


def get_single_data(id_):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* 
             FROM Vendors
             WHERE rowid = (?)'''
    str_id = str(id_)
    cur.execute(sql,str_id)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return data


def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''SELECT rowid,* FROM Vendors'''
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    return list(data)


def update_existing(id_, data):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''UPDATE Vendors 
             SET Name = (?) ,
                 Address = (?), 
                 Contact = (?) 
             WHERE rowid = (?)'''
    tuple_ = (data[0],data[1],data[2],str(id_))
    cur.execute(sql,tuple_)
    data = cur.fetchone()
    conn.commit()
    conn.close()
    return True


def remove_data(id_):
    conn = sqlite3.connect(DATBASE_LOCATION)
    cur = conn.cursor()
    sql = '''DELETE FROM Vendors WHERE rowid = (?)'''
    str_id = str(id_)
    cur.execute(sql,str_id)
    conn.commit()
    conn.close()



# def main():
#     # update_or_create(10,["Hema","Mumbai","222121"])
#     k =8
#     print(get_single_data(k))
#     print(get_multiple_data())




# if __name__ == "__main__":
#     main()

def close():
    conn.commit()
    conn.close()
# CLOSE DATABASE
