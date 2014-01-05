import logging

import ca.onzy.core.properties_helper as properties_helper
import ca.onzy.pi_monitor.arpparser as ap
import ca.onzy.pi_monitor.monitor as monitor

from dictionary import Dictionary

def main():
    
    # read yaml logger file
    ph = properties_helper.PropertiesHelper() 
    log_config = ph.get_yaml_config(filename='logging.conf') 
    # setup logger 
    ph.set_logger(log_config) 
    # get logger
    logger = logging.getLogger("main")
    
    logger.info("hello world")
    # get arguments
    args = ap.buildParser()
    
    myDict = Dictionary().newDict()
    m = monitor.monitor()

    if args.verbose:
        verbose = True
    if args.light:
        logger.debug('light')
        myDict = m.getLight(verbose, myDict)
        if verbose:
            print(myDict)

    if args.humidity:
        logger.debug('humidity')
        myDict = m.getHumidity(verbose, myDict)
        if verbose:
            print(myDict)

    if args.temperature:
        logger.debug('temperature')
        myDict = m.getTemperature(verbose, myDict)
        if verbose:
            print(myDict)

    if args.thermostat:
        logger.debug('termostat')
        m.getThermostat(verbose, myDict)
        if verbose:
            print(myDict)

    if args.all:
        logger.debug('all')
        myDict = m.getLight(verbose, myDict)
        myDict = m.getHumidity(verbose, myDict)
        myDict = m.getTemperature(verbose, myDict)
#        myDict = m.getThermostat(verbose, myDict)
        if verbose:
            print(myDict)
    
if __name__ == '__main__':
    main()
