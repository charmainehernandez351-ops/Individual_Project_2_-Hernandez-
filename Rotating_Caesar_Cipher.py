

class Rotating_CC:
    ALPHA = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    
    def RCC_encrypt(self, msg, shift):
        return self.RCC(msg, shift)

    def RCC_decrypt(self, msg, shift):
        # ToDo - delete 'pass' and replace with the correct code to decript.
        # note - the shift parameter is the encryption integer.  
        pass
    
    def RCC (self, msg, shift):
        new_msg = ""
        new_shift = shift
        for ch in msg:
            if ch.isupper():
                i = self.ALPHA.index(ch)
                ch = self.ALPHA[(i + new_shift) % len(self.ALPHA)]
                new_shift+=shift
            elif ch.islower():
                uppercase_ch = ch.upper()
                i = self.ALPHA.index(uppercase_ch)
                ch = self.ALPHA[(i + new_shift) % len(self.ALPHA)].lower()
                new_shift+=shift
	
				                
            new_msg += ch
                
        return new_msg


    
    
