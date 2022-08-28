         .ORIG x3000
         ADD R1,R2,R3
         ADD R1,R2,x4
         AND R1,R2,R3
         
         AND R1,R2,x-3
         NOT R1,R2
         LD  R1,#3
         LDR R1, R2,#3
         BR data
         LDI R1, data
         LDI R6,#-3
todo         LDR R2, R3,#8
p1         LEA  R3, data
p2         ST  R1, #42
p3         ST R3, todo
p4         STR R2,R7,x-12
p5         STI  R1,test
         
p6         TRAP  x23
p7         GETC
p8         BR todo
p9         BRz data
p10         JMP R2
p11         RET
p12        JSR todo
        
        
p13        JSRR  R2
p14        RTI
test    .FILL  #-5
p15         .BLKW    #3
p16   ADD R1,R1,R3
p17         .STRINGZ "ada232"
         data        LDR R1, R2,x3
         .END