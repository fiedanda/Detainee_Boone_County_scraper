import peewee

db = peewee.SqLiteDatabase(
	'Detainee.db',
	pragmas={'foreign_keys': 1}
	)

class Detainee(peewee.Model):
	case_numb = peewee.CharField(primary_key=True)
	charge_description = peewee.CharField()
	charge_status = peewee.CharField()
	bail_amount = peewee.CharField()
	bond_type = peewee.CharField()
	court_date = peewee.DateField()
	court_time = peewee.TimeField()
	juristriction_court = peewee.CharField() 
	height = peewee.FloatField()
	weight = peewee.FloatField()
	sex = peewee.CharField()
	eyes = peewee.CharField()
	hair = peewee.CharField()
	race = peewee.CharField()
	age = 
	city = CharField()
	state = CharField()

	class = db

db.connect()
db.create_tables([Detainee])
