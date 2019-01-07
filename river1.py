from ssp import *



ssp = SSP()


ssp.S.append("S0")
ssp.S.append("2")
ssp.S.append("3")
ssp.S.append("4")
ssp.S.append("5")
ssp.S.append("W")
ssp.S.append("7R")
ssp.S.append("8R")
ssp.S.append("9R")
ssp.S.append("10R")
ssp.S.append("SG")
ssp.S.append("12")
ssp.S.append("13")
ssp.S.append("14")
ssp.S.append("15")

ssp.S.append("DE")

ssp._s0 = "S0"

ssp.G.append("SG")

ssp.P("S0","R","2",1)
ssp.P("S0","U","W",1)

ssp.P("2","R","3",1)
ssp.P("2","L","S0",1)
ssp.P("2","R","3",1)