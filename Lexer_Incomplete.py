from Lexemes import *
from Token import Token
from typing import List


### ======================================== Lexer / Errors ======================================== ###


class Lexer_Match_Error(BaseException):
    """Exception raised because the base Lexer could not find a matching token

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:
        self.message = message


### ======================================== Lexer ======================================== ###

class Lexer():

    def __init__(self) -> None:
        self._lexemes = [
            Lxm_Op_Power,Lxm_Op_Int_Division,Lxm_Op_Bitshift_Right,Lxm_Op_Bitshift_Left,Lxm_Op_And,Lxm_Op_Or,Lxm_Op_Not_Equal,Lxm_Op_Double_Equal,Lxm_Op_Less_Equal,Lxm_Op_Greater_Equal,
            Lxm_Op_Add,Lxm_Op_Subtract,Lxm_Op_Multiply,Lxm_Op_Division,Lxm_Op_Modulo,Lxm_Op_Bitwise_And,Lxm_Op_Bitwise_Or,Lxm_Op_Bitwise_Xor,Lxm_Op_Bitwise_Not,Lxm_Op_Not,Lxm_Op_Less,Lxm_Op_Greater,Lxm_Op_Equal,
            Lxm_Close_Paren_Open,Lxm_Close_Paren_Close,Lxm_Close_Square_Open,Lxm_Close_Square_Close,Lxm_Close_Curly_Open,Lxm_Close_Curly_Close,
            Lxm_Keywords_If,Lxm_Keywords_Else,Lxm_Keywords_While,
            Lxm_Function_Log,Lxm_Function_Print,Lxm_Function_To_Int,Lxm_Function_To_Float,Lxm_Function_To_Bool,Lxm_Function_To_String,
            Lxm_Line_End,
            Lxm_Literals_Int, Lxm_Literals_Float, Lxm_Literals_Bool, Lxm_Literals_String,
            Lxm_Identifiers_Iden,
            Lxm_Comment_Single, Lxm_Comment_Block,
        ]
        self._lexemes = [l() for l in self._lexemes]


    def _possible_tokens(self, char_stream:List[str]) -> List[Token]:
        char_stream = char_stream.copy()
        [lxm.reset() for lxm in self._lexemes]
        #print(len(self._lexemes))
        ### feed the char_stream to the lexemes one character at a time
        ### Important! do not modify the character stream
        ### TODO: write this code
       
        
        for lxm in self._lexemes:
            lxm.feed(char_stream[i])
            if lxm.is_open(): 
                any_open = True
        i +=1
        
        possible_tokens = []
        for lxm in self._lexemes:
            if lxm.is_complete():
                new_token = Token(lxm.get_token(), lxm.get_captured())
                possible_tokens.append(new_token)
        
        
        
        
        """for y in self._lexemes:
            for x in (char_stream):
                if Lexeme_Multi_Char.is_open:
                    Lexeme_Multi_Char(y, x)
                if Lexeme_Multi_Char.is_failed:
                    print()
                    pass
            if Lexeme_Multi_Char.is_complete:
                print(Lexeme_Multi_Char)"""
        


            #print(possible_tokens)
        """for y in self._lexemes: # Gets Tokens from Lexemes
            #print(y.get_token())
                # Gets single characters from stream
                #print(self._lexemes[x])
                #print(char_stream[x])
                if char_stream[0] in y.get_token(): # if charcter is in lexeme token
                    if y not in possible_tokens:
                        possible_tokens.append(y)
                elif char_stream[0].isalpha:
                    if Lxm_Identifiers_Iden and Lxm_Literals_String not in possible_tokens:
                        #possible_tokens.append(Lxm_Literals_String)
                        possible_tokens.append(Lxm_Identifiers_Iden)
                elif char_stream[0].isnumeric:
                    if Lxm_Literals_Int and Lxm_Literals_Float not in possible_tokens:
                        possible_tokens.append(Lxm_Literals_Int)
                        possible_tokens.append(Lxm_Literals_Float)
                        
                else:
                    pass"""
                    
        
        """for y in self._lexemes: # Gets Tokens from Lexemes
            #print(y.get_token())
            
            for x in char_stream: # Gets single characters from stream
                #print(self._lexemes[x])
                #print(char_stream[x])
                if x in y.get_token(): # if charcter is in lexeme token
                    if y not in possible_tokens:
                        possible_tokens.append(y)
                else:
                    pass"""
        
        #print(self._lexemes)
        
        ### fill the list with tokens that match the head of the char_stream
        ### TODO: write this code

        #print(possible_tokens, (len(possible_tokens)))
        ### return the list of tokens
        #print(possible_tokens)
        return possible_tokens
        

    def match_tokens(self, char_stream:str) -> List[str]:

        tokens = []
        
        char_stream = list(char_stream)

        while len(char_stream) > 1:
            ### skip any leading whitespace
            ### TODO: write this code
            if char_stream[0] == " ":
                char_stream.pop(0)
            if char_stream[0] == "\n":
                char_stream.pop(0)

            ### get the possible token matches to the char_stream
            possible_tokens = self._possible_tokens(char_stream)

            ### make sure at least one token matched and raise an error if none did
            if len(possible_tokens) == 0:
                raise(Lexer_Match_Error("No matching Token for:\n{}".format(''.join(char_stream))))

            ### otherwise resolve any conflicts and append the token to tokens
            ### TODO: write this code
            for x in possible_tokens:
                    tokens.append(Token(x,char_stream[0]))
            ### remove the captured characters from the front of the character_stream
            new_token = tokens[-1]
            char_stream = char_stream[len(new_token.get_string()):]

            ### remove the parenthesis from any strings
            if new_token.get_type() == Token_Enum.Literals.String:
                new_token.set_string(new_token.get_string()[1:-1])

        return tokens
                    



                    


                



            
        


