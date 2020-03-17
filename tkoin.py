#tkoin, example blockchain
#Copyright (C) 2020 Keffen Della-Torre and Tom Simon

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed WITHOUT ANY WARRANTY.
#See the license in the file LICENSE


#tkoin is an example blockchain, despite its name it is not (yet) a cryptocurrency, just a blockchain.
#We used it for "TIPE" ("Travaux d'Interet Personnel Encadre", it is French for "Personal Interest Supervised Work"), it is a part of an exam for MPSI (Mathematics Physics Engineering, in French "Mathematiques Physique Sciences de l'Ingenieur"). It is very experimental and, you should NOT USE that as is for an actual project.
#It is named "tkoin" because it was made by *T*om Simon and *K*effen Della-Torre, two French students.
from hashlib import sha256
def hash(x):
    return sha256(x).hexdigest()

class Block:
    def __init__(self,transaction,lastcs=None):
        self.transaction=transaction
        self.lastcs=lastcs or bytes(16)
        if type(transaction)!=bytes or len(transaction)!=2:
            raise Exception("You should provide a 16bit (2bytes) bytes object for transaction")
        if type(self.lastcs)!=bytes or len(self.lastcs)!=16:
            raise Exception("You should provide a 256bit (16bytes) bytes object for lastcs")
        self.checksum=hash(self.transaction+self.lastcs)
    def get_transaction(self):
        fromto,amount=self.transaction[0],self.transaction[1]
        if fromto<128:
            return (0,fromto,amount)
        else:
            hex_fromto=hex(fromto)[2:]
            hextable={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
            from_=hex_fromto[0]
            to=hex_fromto[1]
            return (hextable[from_],hextable[to],amount)
    def get_checksum(self):
        return self.checksum
    def get_last_checksum(self):
        return self.lastcs
class BlockChain:
    def __init__(self,transac_init):
        self.chain=[]
        self.chain.append(Block(transac_init))
    def addblock(self,transaction):
        self.chain.append(Block(transaction,self.chain[-1].checksum))
    def get_transactions(self):
        return [block.get_transaction() for block in self.chain]
