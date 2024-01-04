class XPATH:
    inputSystemType = "0"
    logoTF = '//*[@id="root"]/div[2]/div/div/header/a/div/img'
    email = '//*[@id="email"]'
    group = '//*[@data-test-id="request-field-customfield_10292"]/div[2]/div/div[2]/div/span'
    dropMenuGroup = '//*[@id="react-select-4-option-2"]'
    connectionRequest = '//*[@id="summary"]'
    describe = '//*[@id="ak-editor-textarea"]'
    entitlementType = '//*[@data-test-id="request-field-customfield_10525"]/div[2]/div/div[1]'
    dropMenuEntitlementType = '//*[@id="react-select-5-option-6"]'
    customerType = '//*[@data-test-id="request-field-customfield_10526"]/div[2]/div/div[1]'
    dropMenuCustomerType = '//*[@id="react-select-6-option-1"]'
    isSystemNew = '//*[@data-test-id="request-field-customfield_10253"]/div[2]/div/div[1]'
    dropMenuIsSystemNew = '//*[@id="react-select-7-option-1"]'
    region = '//*[@data-test-id="request-field-customfield_10543"]/div[2]/div/div[1]'
    dropMenuRegion = '//*[@id="react-select-8-option-3"]'
    customer = '//*[@data-test-id="request-field-customfield_10185"]/div[2]/div/div[1]'
    dropMenuCustomer = '//*[@id="react-select-9-option-227"]'
    fleet = '//*[@data-test-id="request-field-customfield_10291"]/div[2]/div/div[1]'
    dropMenuFleet = '//*[@id="react-select-10-option-9"]'
    systemType = '//*[@data-test-id="request-field-customfield_10188"]/div[2]/div/div[1]'
    systemModel = '//*[@id="customfield_10627"]'
    nameCSM = '//*[@data-test-id="request-field-customfield_10544"]/div[2]/div/div[2]/div/span'
    dropMenuCSM = '//*[@id="react-select-12-option-13"]'
    nameDSE = '//*[@data-test-id="request-field-customfield_10545"]/div[2]/div/div[2]/div/span'
    dropMenuDSE = '//*[@id="react-select-13-option-9"]'

    @classmethod
    @property
    def dropMenuSystemType(cls):
        return f'//*[@id="react-select-11-option-{cls.inputSystemType}"]'
