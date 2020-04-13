class VehicleLicense:

    def __init__(self,plate_number,vtype,owner,addr,use_chara,model_ch,model_num,
                 vin,engine_num,reg_date,issue_date):
        super(VehicleLicense, self).__init__()
        self.__plate_number = plate_number
        self.__vtype = vtype
        self.__owner = owner
        self.__addr = addr
        self.__use_chara = use_chara
        self.__model_ch = model_ch
        self.__model_num = model_num
        self.__vin = vin
        self.__engine_num = engine_num
        self.__reg_date = reg_date
        self.__issue_date = issue_date

    def get_plate_number(self):
        return self.__plate_number

    def get_vtype(self):
        return self.__vtype

    def get_owner(self):
        return self.__owner

    def get_addr(self):
        return self.__addr

    def get_use_chara(self):
        return self.__use_chara

    def get_model_ch(self):
        return self.__model_ch

    def get_model_num(self):
        return self.__model_num

    def get_vin(self):
        return self.__vin

    def get_engine_num(self):
        return self.__engine_num

    def get_reg_date(self):
        return self.__reg_date

    def get_issue_date(self):
        return self.__issue_date