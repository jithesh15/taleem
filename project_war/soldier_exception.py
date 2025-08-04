class SoldierException(Exception):

    def __init__(self, msg, org_msg=None):
        self.msg = msg
        self.org_msg = org_msg
        super().__init__(f"Error occured due to {self.msg} - {self.org_msg}")