from pyteal import *
import program 



def approval():
    global_counter = Bytes("counter") # uint64
    global_owner = Bytes("owner") # bytes 


    return program.event(
        init=Seq(
            # create a variable
            App.globalPut(global_counter, Int(0)),
            App.globalPut(global_owner, Bytes("Me")),
            Approve()
            
        )
    )

def clear():
    return Approve()
