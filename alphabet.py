from collections import defaultdict
alphabet = defaultdict(str)
for i in [("A0","010"),
            ("A1","101"),
            ("A2","101"),
            ("A3","111"),
            ("A4","101"),
            ("A5","101"),
            ("B0","110"),
            ("B1","101"),
            ("B2","110"),
            ("B3","101"),
            ("B4","101"),
            ("B5","110"),
            ("C0","010"),
            ("C1","101"),
            ("C2","100"),
            ("C3","100"),
            ("C4","101"),
            ("C5","010"),
            ("D0","110"),
            ("D1","101"),
            ("D2","101"),
            ("D3","101"),
            ("D4","101"),
            ("D5","110"),
            ("E0","111"),
            ("E1","100"),
            ("E2","100"),
            ("E3","111"),
            ("E4","100"),
            ("E5","111"),
            ("F0","111"),
            ("F1","100"),
            ("F2","100"),
            ("F3","111"),
            ("F4","100"),
            ("F5","100"),
            ("G0","111"),
            ("G1","100"),
            ("G2","100"),
            ("G3","101"),
            ("G4","101"),
            ("G5","111"),
            ("H0","101"),
            ("H1","101"),
            ("H2","101"),
            ("H3","111"),
            ("H4","101"),
            ("H5","101"),
            ("I0","111"),
            ("I1","010"),
            ("I2","010"),
            ("I3","010"),
            ("I4","010"),
            ("I5","111"),
            ("J0","111"),
            ("J1","001"),
            ("J2","001"),
            ("J3","101"),
            ("J4","101"),
            ("J5","010"),
            ("K0","101"),
            ("K1","101"),
            ("K2","110"),
            ("K3","101"),
            ("K4","101"),
            ("K5","101"),
            ("L0","100"),
            ("L1","100"),
            ("L2","100"),
            ("L3","100"),
            ("L4","100"),
            ("L5","111"),
            ("M0","101"),
            ("M1","111"),
            ("M2","101"),
            ("M3","101"),
            ("M4","101"),
            ("M5","101"),
            ("N0","111"),
            ("N1","101"),
            ("N2","101"),
            ("N3","101"),
            ("N4","101"),
            ("N5","101"),
            ("O0","111"),
            ("O1","101"),
            ("O2","101"),
            ("O3","101"),
            ("O4","101"),
            ("O5","111"),
            ("P0","110"),
            ("P1","101"),
            ("P2","101"),
            ("P3","110"),
            ("P4","100"),
            ("P5","100"),
            ("Q0","010"),
            ("Q1","101"),
            ("Q2","101"),
            ("Q3","101"),
            ("Q4","111"),
            ("Q5","011"),
            ("R0","110"),
            ("R1","101"),
            ("R2","101"),
            ("R3","110"),
            ("R4","101"),
            ("R5","101"),
            ("S0","111"),
            ("S1","100"),
            ("S2","111"),
            ("S3","001"),
            ("S4","001"),
            ("S5","111"),
            ("T0","111"),
            ("T1","010"),
            ("T2","010"),
            ("T3","010"),
            ("T4","010"),
            ("T5","010"),
            ("U0","101"),
            ("U1","101"),
            ("U2","101"),
            ("U3","101"),
            ("U4","101"),
            ("U5","111"),
            ("V0","101"),
            ("V1","101"),
            ("V2","101"),
            ("V3","101"),
            ("V4","101"),
            ("V5","010"),
            ("W0","101"),
            ("W1","101"),
            ("W2","101"),
            ("W3","101"),
            ("W4","111"),
            ("W5","101"),
            ("X0","101"),
            ("X1","101"),
            ("X2","101"),
            ("X3","010"),
            ("X4","101"),
            ("X5","101"),
            ("Y0","101"),
            ("Y1","101"),
            ("Y2","101"),
            ("Y3","010"),
            ("Y4","010"),
            ("Y5","010"),
            ("Z0","111"),
            ("Z1","001"),
            ("Z2","010"),
            ("Z3","100"),
            ("Z4","100"),
            ("Z5","111"),
            (".0","000"),
            (".1","000"),
            (".2","000"),
            (".3","000"),
            (".4","000"),
            (".5","010"),
            ("?0","010"),
            ("?1","101"),
            ("?2","001"),
            ("?3","010"),
            ("?4","000"),
            ("?5","010"),
            ("!0","010"),
            ("!1","010"),
            ("!2","010"),
            ("!3","010"),
            ("!4","000"),
            ("!5","010"),
            (" 0","000"),
            (" 1","000"),
            (" 2","000"),
            (" 3","000"),
            (" 4","000"),
            (" 5","000")]:
            alphabet[i[0]] = i[1]