class DrivingLicense:
    def __init__(self,id_number,name,gender,nation,addr,birth_date,issue_date,cls,validate_from,validate_for):
        super(DrivingLicense, self).__init__()
        self.__id_number = id_number
        self.__name = name
        self.__gender = gender
        self.__nation = nation
        self.__addr = addr
        self.__birth_date = birth_date
        self.__issue_date = issue_date
        self.__class = cls
        self.__validate_from = validate_from
        self.__validate_for = validate_for

    def get_id_number(self):
        return self.__id_number

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_nation(self):
        return self.__nation

    def get_addr(self):
        return self.__addr

    def get_birth_date(self):
        return self.__birth_date

    def get_issue_date(self):
        return self.__issue_date

    def get_class(self):
        return self.__class

    def get_validate_from(self):
        return self.__validate_from

    def get_validate_for(self):
        return self.__validate_for
