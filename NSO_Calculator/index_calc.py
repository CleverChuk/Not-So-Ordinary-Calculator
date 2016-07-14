## NOT_SO_ORDINARY_CALCULATOR
## MINI PROJECT: CALCULATOR
## THIS MODULE CONTAINS THE LOGIC FOR THE CALCULATOR
## ALL PARSING FUNCTIONS CAN BE FOUND HERE
import math

class data():
    """ Holds input from GUI"""
    lvalue = None;
    rvalue = None;
    rsl = None;
    operator = None;

def add(lv, rv):
    return lv + rv;

def subtract(lv, rv):
    return lv - rv;

def multiply(lv , rv):
    return lv * rv;

def divide(lv, rv):
    return float(lv) / rv;

    
def parse(data):
    """Maps operator to the right function"""
    switch = {
        '+':add(data.lvalue,data.rvalue),
        '-':subtract(data.lvalue,data.rvalue),
        '*':multiply(data.lvalue,data.rvalue),
        '/':divide(data.lvalue,data.rvalue)
        }
    return switch.get(data.operator,'pass')
              
