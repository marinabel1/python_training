from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, mail=None, bday_day=None, bday_month=None, bday_year=None, company=None, mobile=None, work=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.mail = mail
        self.bday_day = bday_day
        self.bday_month = bday_month
        self.bday_year = bday_year
        self.company = company
        self.mobile = mobile
        self.work = work
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
