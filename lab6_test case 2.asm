    .ORIG   x3000
            LDR  R1,R1,#3
            BR    data
            
            
data        AND  R1,R2,#3
    .END