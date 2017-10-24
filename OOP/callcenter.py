class Call(object):
    _unique_id = 0

    def __init__(self, caller_name, caller_phone, reason_for_call):
        import time

        self.unique_id = self._unique_id
        self.__class__._unique_id += 1
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time_of_call = time.strftime("%c")
        self.reason_for_call = reason_for_call

    def displayCallInfo(self):
        print self.unique_id, self.caller_name, self.caller_phone, self.time_of_call, self.reason_for_call


class CallCenter(object):
    def __init__(self):
        self.call_list = []

    def add(self, call):
        self.call_list.append(call)
        return self

    def remove(self):
        self.call_list.remove(self.call_list[0])
        return self

    def remove_by_phone(self, phone_number):
        for call in self.call_list:
            if phone_number == call.caller_phone:
                self.call_list.remove(call)
        return self

    # Hacker level challenge. Causing "NoneType" object is not iterable?
    def sort_calls(self):
        from operator import attrgetter
        self.call_list = self.call_list.sort(key=attrgetter('time_of_call'))
        return self

    def info(self):
        for call in self.call_list:
            call.displayCallInfo()


call1 = Call('Travis', '206-920-8443', 'Complaint')
call2 = Call('Rebecca', '206-595-3742', 'Support')
call3 = Call('Maddy', '206-555-1234', 'Support')

callcenter = CallCenter()
callcenter.add(call2).add(call1).add(call3).info()
# callcenter.remove_by_phone('206-920-8443').info()
