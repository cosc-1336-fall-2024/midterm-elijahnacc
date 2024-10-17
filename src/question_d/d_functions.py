#write functions here, don't add input('') statements here!

def get_assessment_value(value):

    assessment = value * 0.6

    return assessment

def get_tax_assessed(assess_value):

    property_tax = assess_value * 0.0072
    property_tax = round(property_tax, 2)
    
    return property_tax