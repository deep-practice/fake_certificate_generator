#encoding=utf-8
class BusinessLicense:
    def __init__(self,corp_name,corp_type,uscc,regist_number,addr,legal_rep,
                 regist_capital,establish_date,validate_for,business_scope,issue_date):
        super(BusinessLicense, self).__init__()
        self.__corp_name = corp_name
        self.__uscc = uscc if uscc is not None else "" #uniform social credit code
        self.__regist_number = regist_number if regist_number is not None else ""
        self.__corp_type = corp_type
        self.__addr = addr
        self.__legal_rep = legal_rep
        self.__regist_capital = regist_capital
        self.__establish_date = establish_date
        self.__validate_for = validate_for
        self.__business_scope = business_scope
        self.__issue_date = issue_date

    def get_corp_name(self):
        return self.__corp_name

    def get_corp_type(self):
        return self.__corp_type

    def get_uscc(self):
        return self.__uscc

    def get_regist_number(self):
        return self.__regist_number

    def get_addr(self):
        return self.__addr

    def get_legal_rep(self):
        return self.__legal_rep

    def get_regist_capital(self):
        return self.__regist_capital

    def get_establish_date(self):
        return self.__establish_date

    def get_business_term(self):
        return self.__establish_date+"至"+self.__validate_for

    def get_business_scope(self):
        return self.__business_scope

    def get_issue_date(self):
        return self.__issue_date

