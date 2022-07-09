import settings
def heightPercentCalc(percentage):
    return settings.SCREENHEIGHT*(percentage*0.01)

def widthPercentCalc(percentage):
    return settings.SCREENWIDTH*(percentage*0.01)