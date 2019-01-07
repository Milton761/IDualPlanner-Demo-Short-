\* SSP-MaxProb *\
Maximize
OBJ: IN_D1 + IN_S1 + IN_S2
Subject To
_C1: IN_S0 - 0.5 S1a0 - 0.25 S2a1 = 0
_C2: IN_S2 - S0a1 = 0
_C3: IN_D1 - 0.5 S0a0 = 0
_C4: IN_S1 - 0.5 S0a0 = 0
_C5: OUT_S0 - S0a0 - S0a1 = 0
_C6: - IN_S0 + OUT_S0 = 1
Bounds
IN_D1 <= 1
IN_S0 <= 1
IN_S1 <= 1
IN_S2 <= 1
OUT_S0 <= 1
End
