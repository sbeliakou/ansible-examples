#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'one_filter': self.a_filter,
            'another_filter': self.b_filter
        }
 
    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' processed with one_filter'
        return a_new_variable
 
    def b_filter(self, a_variable, another_variable, yet_another_variable):
        a_new_variable = a_variable + ' - ' + another_variable + ' - ' + yet_another_variable + ' processed with another_filter'
        return a_new_variable