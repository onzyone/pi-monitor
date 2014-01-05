import argparse


def buildParser():
    parser = argparse.ArgumentParser(description='This is monitroing script for Temp, Light and Humidty')
    paa = parser.add_argument
    
    paa('-l', '--light', dest='light', action='store_true', 
        help='get light value in Lux')
    paa('-u', '--humidity', dest='humidity', action='store_true', 
        help='get humidity in %')
    paa('-t', '--temperature', dest='temperature', action='store_true', 
        help='get temperature in oC')
    paa('--thermostat', dest='thermostat', action='store_true', 
        help='get json back from thermostat ct50')
    paa('-a', '--all', dest='all', action='store_true', 
        help='get all of the above')
    paa('-v', '--verbose', dest='verbose', action='store_true', 
        help='will print values')
    paa('--version', action='version', version='%(prog)s 2.0')

    args = parser.parse_args()

    return args 