import abc
import databaseOperations
## GLOBALS
# VENDORS
VENDORS_TABLE_NAME = "Vendors"
VENDORS_DATA = databaseOperations.get_multiple_data(VENDORS_TABLE_NAME)
VENDORS_HEADERS = ["id_","Name","Address","Contact"]
VENDORS_COLUMN_NAMES = ["name","address","contact"]

# PARTS
PARTS_TABLE_NAME = "Parts"
PARTS_DATA = databaseOperations.get_multiple_data(PARTS_TABLE_NAME)
PARTS_HEADERS = ["id_","Name","Vehicle Type","Rack Number","Threshold"]
PARTS_COLUMN_NAMES = ["part_name","vehicle_type","rack_number","Threshold"]

# STATS
STATS_TABLE_NAME = "Stats"
STATS_DATA = databaseOperations.get_multiple_data(STATS_TABLE_NAME)
STATS_HEADERS = ["id_","Vendor Name","Part Name","Vehicle Type","Stock","Cost Price"]
STATS_COLUMN_NAMES = ["vendor_name","part_name","vehicle_type","stock","cp"]

# INVOICE
INVOICE_TABLE_NAME = "Invoice"
INVOICE_DATA = databaseOperations.get_multiple_data(INVOICE_TABLE_NAME)
INVOICE_HEADERS = ["id_","Invoice Number","Part Name","Vehicle Type","Price","Volume","Amount","Vendor Name","Cost Price"]
INVOICE_COLUMN_NAMES = ["invoice_number","part_name","vehicle_type","price","volume","amount","vendor_name","cp"]

# SALES
SALES_TABLE_NAME = "Sales"
SALES_DATA = databaseOperations.get_multiple_data(SALES_TABLE_NAME)
SALES_HEADERS = ["id_","Date","Invoice Number"]
SALES_COLUMN_NAMES = ["Date","invoice_number"]



class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
        	cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]
        


class Vendors():
	__metaclass__ = Singleton

	def __init__(self):
		self.name = VENDORS_TABLE_NAME
		self.data = VENDORS_DATA
		self.headers = VENDORS_HEADERS
		self.column_names = VENDORS_COLUMN_NAMES

class Parts():
	__metaclass__ = Singleton
	
	def __init__(self):
		self.name = PARTS_TABLE_NAME
		self.data = PARTS_DATA
		self.headers = PARTS_HEADERS
		self.column_names = PARTS_COLUMN_NAMES

class Stats():
	__metaclass__ = Singleton
	
	def __init__(self):
		self.name = STATS_TABLE_NAME
		self.data = STATS_DATA
		self.headers = STATS_HEADERS
		self.column_names = STATS_COLUMN_NAMES


class Invoice():
	__metaclass__ = Singleton
	
	def __init__(self):
		self.name = INVOICE_TABLE_NAME
		self.data = INVOICE_DATA
		self.headers = INVOICE_HEADERS
		self.column_names = INVOICE_COLUMN_NAMES

class Sales():
	__metaclass__ = Singleton
	
	def __init__(self):
		self.name = SALES_TABLE_NAME
		self.data = SALES_DATA
		self.headers = SALES_HEADERS
		self.column_names = STATS_COLUMN_NAMES

		










