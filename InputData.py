class Data:
    email = ""
    systemPN = ""
    systemSN = ""
    connectionRequest = "Connect microscope to D2i"

    @classmethod
    @property
    def describe(cls):
        return f"System planning number: {cls.systemPN}\nSystem serial number: {cls.systemSN}"

    @classmethod
    @property
    def systemModel(cls):
        return f"System planning number: {cls.systemPN}, System serial number: {cls.systemSN}"
