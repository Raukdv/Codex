import base64

class Codex():

    #data: Will be any value in str type that can be change into new values
    #subsequence: will be the second iter when the first encode happen, that's mean it will use another encode process over the current one
    #expansion: will be a sum for the main key-loop value in the encode process, it will need a rest for decode to get exact value.
    #KV will be an mirror for KeyValue, initaly was thinked as first change step
    #VK it's the mirror translator itself for coming values from KV.
    #base64 and base85 it's just the subsequence methods for make more complex the essence of encode andecode

    def __init__(self, **kwargs) -> None:
        #This for KeyValue
        self.KV = {
            '1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': 'a', '12': 'b', '13': 'c', '14': 'd', 
            '15': 'e', '16': 'f', '17': 'g', '18': 'h', '19': 'i', '20': 'j', '21': 'k', '22': 'l', '23': 'm', '24': 'n', '25': 'ñ', '26': 'o', '27': 'p', '28': 'q', 
            '29': 'r', '30': 's', '31': 't', '32': 'u', '33': 'v', '34': 'w', '35': 'x', '36': 'y', '37': 'z', '38': 'A', '39': 'B', '40': 'C', '41': 'D', '42': 'E', 
            '43': 'F', '44': 'G', '45': 'H', '46': 'I', '47': 'J', '48': 'K', '49': 'L', '50': 'M', '51': 'N', '52': 'Ñ', '53': 'O', '54': 'P', '55': 'Q', '56': 'R', 
            '57': 'S', '58': 'T', '59': 'U', '60': 'V', '61': 'W', '62': 'X', '63': 'Y', '64': 'Z', '65': '<', '66': '=', '67': '>', '68': '@', '69': '#', '70': '%', 
            '71': '&', '72': '+', '73': '(', '74': ')', '75': '^'}
        #This for ValueKey
        self.VK = {
            '0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10', 'a': '11', 'b': '12', 'c': '13', 'd': '14', 
            'e': '15', 'f': '16', 'g': '17', 'h': '18', 'i': '19', 'j': '20', 'k': '21', 'l': '22', 'm': '23', 'n': '24', 'ñ': '25', 'o': '26', 'p': '27', 'q': '28', 
            'r': '29', 's': '30', 't': '31', 'u': '32', 'v': '33', 'w': '34', 'x': '35', 'y': '36', 'z': '37', 'A': '38', 'B': '39', 'C': '40', 'D': '41', 'E': '42', 
            'F': '43', 'G': '44', 'H': '45', 'I': '46', 'J': '47', 'K': '48', 'L': '49', 'M': '50', 'N': '51', 'Ñ': '52', 'O': '53', 'P': '54', 'Q': '55', 'R': '56', 
            'S': '57', 'T': '58', 'U': '59', 'V': '60', 'W': '61', 'X': '62', 'Y': '63', 'Z': '64', '<': '65', '=': '66', '>': '67', '@': '68', '#': '69', '%': '70', 
            '&': '71', '+': '72', '(': '73', ')': '74', '^': '75'}
        
        #Init value - Ternario Method
        self.data = kwargs.get('data') if 'data' in kwargs else None
        self.subsequence = kwargs.get('subsequence') if 'subsequence' in kwargs else None
        self.expansion = kwargs.get('expansion') if 'expansion' in kwargs else None

        #Auto revision for do with:
        #1-. Expansion with no subsequence
        #2.-Subsequence with no expansion
        #3.- Both or none

        self.with_expansion = True if self.expansion else False
        self.with_subsequence = True if self.subsequence else False

    #Mirror - Encode 
    def mirror_kv(self):
        print("Starting Mirror for: ", self.data)
        #validate data-type is always str
        if isinstance(self.data, str):
            pass
        else:
            raise TypeError("data most be str")

        mirror_string = None
        #Loop to change each value to the new encode
        #loop for compare actual template dict for each value given
        #Check if the current character it's the same as the template value and if is, change to the key (loop int)
        #Frist change for values
        mirror_string = [key for character in self.data for key, value in self.KV.items() if character == value]
        print("Code Mirror: ", mirror_string)
        return mirror_string
    
    #Mirror Translator - Decode - Data is a list of mirror values
    def mirror_vk(self, data):
        decode_string = ''
        parse_segment = data if isinstance(data, list) else None
    
        if parse_segment:
            #Loop to change each value to the new encode
            for character in parse_segment:
                #loop for compare actual template dict for each value given
                for key, value in self.VK.items():
                    #Check if the current character it's the same as the template valu and if is, change to the key 
                    if character == value:
                        decode_string += f'{key}'

        return decode_string
    
    #This will expand our initial values as a primary concealment step.
    def expanded(self, code_string=None):

        if self.expansion and isinstance(self.expansion, int):
            print("Doing expansion")
            expansion_list = [str(int(code)+self.expansion) for code in code_string if code.isnumeric()]
            print("Code Expanded: ", expansion_list)
        
        return expansion_list

    #This will reduce our primary concealment step to the inital form. With this you can apply mirror translator
    def reduced(self, code_string=None, expan=None):
        expansion = self.expansion if not expan else expan

        if expansion and isinstance(expansion, int):
            print("Doing reduction")
            reduce_list = [str(int(code)-expansion) for code in code_string if code.isnumeric()]
            print("Code reducted: ", reduce_list)

        return reduce_list
    
    def subsequence_base(self, mirror_code):
        #Do with base 64
        if self.subsequence == '64':
            print("Doing subsequence:", self.subsequence)
            container_based = []
            for value in mirror_code:
                container_based.append(self.encode_base64(value))
                
        #Do with base 85
        elif self.subsequence == '85':
            print("Doing subsequence:", self.subsequence)
            container_based = []
            for value in mirror_code:
                container_based.append(self.encode_base85(value)) 
        else:
            raise ValueError("The Lookup base encode given isnt correct, try use 64 or 85 signal.")
        
        return container_based 

    #Subsequence methods
    #This will called for code the first mirrored value using at least one of those base encode, 64/85 or whatever you want here.

    def encode_base64(self, texto):
        texto_bytes = texto.encode('utf-8')
        base64_bytes = base64.b64encode(texto_bytes)
        base64_string = base64_bytes.decode('utf-8')
        return base64_string

    def decode_base64(self, base64_string):
        base64_bytes = base64_string.encode('utf-8')
        texto_bytes = base64.b64decode(base64_bytes)
        texto = texto_bytes.decode('utf-8')
        return texto

    def encode_base85(self, texto):
        texto_bytes = texto.encode('utf-8')
        base85_bytes = base64.b85encode(texto_bytes)
        base85_string = base85_bytes.decode('utf-8')
        return base85_string

    def decode_base85(self, base85_string):
        base85_bytes = base85_string.encode('utf-8')
        texto_bytes = base64.b85decode(base85_bytes)
        texto = texto_bytes.decode('utf-8')
        return texto
    
    def parse_code(self, code):
        print("Parsing result")
        #Formating to get a better response
        parced_code = '/'.join(code)
        if parced_code.endswith("/"):
            parced_code = parced_code.rstrip(parced_code[-1])

        #Add identification about subsequence and expansion if was added
        if self.with_expansion and self.with_subsequence: #Both methods
            parced_code = parced_code+'$64-'+f'{self.expansion}' if self.subsequence == '64' else parced_code+'$85-'+f'{self.expansion}'
        elif not self.with_subsequence and self.with_expansion: #Just expansion method
            parced_code = parced_code+f'$-{self.expansion}'
        elif not self.with_expansion and self.with_subsequence: #Just subsequence method
            parced_code = parced_code+'$64-' if self.subsequence == '64' else parced_code+'$85-'
        else: #Just mirror method
            parced_code = parced_code+'$-'
        
        return parced_code
    
    #Do Code and Decode Proccess
    def code(self):
        container = None
        #Get mirror values
        mirror = self.mirror_kv()
        print("Value in mirror: ", mirror)

        #Start formating second process
        #In the end to handle better the code you should return some str with this structure for decoding propuse
        #mirror_value/mirror_value/mirror_value$subsequence_value-expansion_value

        #Apply Subsequence or expansion or whatever given to work
        if self.with_expansion and self.with_subsequence: #Both methods
            #Expand first and then apply base code subsequence, not reverse.
            mirror_expaned = self.expanded(mirror)
            container = self.subsequence_base(mirror_expaned)
        elif not self.with_subsequence and self.with_expansion: #Just expansion method
            container = self.expanded(mirror)
        elif not self.with_expansion and self.with_subsequence: #Just subsequence method
            container = self.subsequence_base(mirror)
        else: #Just mirror method
            container = mirror

        #Parce the reminder information about subsequence and expasion
        parsed_container = self.parse_code(container)
        
        return parsed_container
    
    #Decode can be called generally with no init values in the class. Just give the code value to try decode.
    def decode(self, value_code=None):
        #First separate encode str from meta process (Subsequence and expansion indicators)
        separate_values = value_code.split("$")

        #assign encode str and meta indicators to differents new variables
        if len(separate_values) == 2:
            encode_str = separate_values[0] #It's a long str encode, nothing else
            separate_str = encode_str.split('/') #Separate each value by / to get the current one
            indicators = separate_values[1] #Have a specific format an need to be follow. the divider is "-" left for subsequence and right for expansion. THIS IS IMPORTANT
            
            #At the same time you need to separate indicators in subsequence and expansion if those was given, in other case indicate  
            separate_indicators = indicators.split('-') #Split will give you a list with the current position for subsequence and expansion, beware maybe this change in other python version
            
            #check if left position response with ['subsequence', 'empty'] -> this will work for subsequence
            #Check if right posiiton resposne with ['empty', 'expansion'] -> this will work for expansion
            #Check if left and right response with ['subsequence', 'expansion'] -> This will work for both methods
            if separate_indicators[0] and separate_indicators[1] and separate_indicators[0] != '' and separate_indicators[1] != '': #this should work for both methods
                metadata = dict(method='both', subsequence=separate_indicators[0], expansion=separate_indicators[1])
            elif separate_indicators[1] and not separate_indicators[0] and separate_indicators[1] != '' and separate_indicators[0] == '': #This should work for expansion method and not subsequence
                metadata = dict(method='expansion', expansion=separate_indicators[1])
            elif separate_indicators[0] and not separate_indicators[1] and separate_indicators[0] != '' and separate_indicators[1] == '': # this should work for subsequence and not expansion method
                metadata = dict(method='subsequence', subsequence=separate_indicators[0])
            else:
                metadata = None
                raise IndexError("A value was found that cannot be worked on.")
            
            #decode acording metadata instruction
            if 'method' in metadata and metadata.get('method'):
                if metadata.get('method', None) == 'both':
                    #First decode base subsequence and then decode expansion result from subsequence
                    print("DECODING BOTH METHODS")
                    if 'subsequence' in metadata and 'expansion' in metadata:
                        if metadata.get('subsequence', None) == '64':
                            decode_base_str = [self.decode_base64(encode) for encode in separate_str]
                        elif metadata.get('subsequence', None) == '85':
                            decode_base_str = [self.decode_base85(encode) for encode in separate_str]
                        else:
                            decode_base_str = None
                            raise ValueError(f"The given {metadata.get('subsequence', None)} base is incorrect for decoding")
                        
                        #Second to reduce the expansion, taking in count if the decode was made. 
                        if decode_base_str:
                            base_str = self.reduced(decode_base_str, int(metadata.get('expansion', None)))
                        
                        #Finally translate the mirror values
                        if base_str:
                            original_str = self.mirror_vk(base_str)

                elif metadata.get('method', None) == 'expansion':
                    print("DECODING EXPANSION METHODS")
                    #Just reduce the expansion.
                    if 'expansion' in metadata:
                        base_str = self.reduced(separate_str, int(metadata.get('expansion', None)))
                    #Finally translate the mirror values
                    if base_str:
                        original_str = self.mirror_vk(base_str)
                    
                elif metadata.get('method', None) == 'subsequence':
                    print("DECODING SUBSEQUENCE METHOD")
                    if 'subsequence' in metadata:
                        if metadata.get('subsequence', None) == '64':
                            decode_base_str = [self.decode_base64(encode) for encode in separate_str]
                        elif metadata.get('subsequence', None) == '85':
                            decode_base_str = [self.decode_base85(encode) for encode in separate_str]
                        else:
                            decode_base_str = None
                            raise ValueError(f"The given {metadata.get('subsequence', None)} base is incorrect for decoding")
                        
                    if decode_base_str:
                        original_str = self.mirror_vk(decode_base_str)
                else:
                    raise Exception("Something went wrong decoding one or more indicators")
            else:
                original_str = None
                print("Indicator went empty, something faild doing initial indentification in the encode str")

        else:
            raise IndexError(f"Decode use 2 parameters and {len(separate_values)} was given")
        
        return original_str
