morsedeCode = {".-":"A","-...":"B","-.-.":"C"}
morsedeCode ["-.."]  = "D"
morsedeCode ["."]    = "E"
morsedeCode ["..-."] = "F"
morsedeCode ["--."]  = "G"
morsedeCode ["...."] = "H"
morsedeCode [".."]   = "I"
morsedeCode [".---"] = "J"
morsedeCode ["-.-"]  = "K"
morsedeCode [".-.."] = "L"
morsedeCode ["--"]   = "M"
morsedeCode ["-."]   = "N"
morsedeCode ["---"]  = "O"
morsedeCode [".--."] = "P"
morsedeCode ["--.-"] = "Q"
morsedeCode [".-."]  = "R"
morsedeCode ["..."]  = "S"
morsedeCode ["-"]    = "T"
morsedeCode ["..-"]  = "U"
morsedeCode ["...-"] = "V"
morsedeCode [".--"]  = "W"
morsedeCode ["-..-"] = "X"
morsedeCode ["-.--"] = "Y"
morsedeCode ["--.."] = "Z"

FILE=open("morse.txt", 'r+')
defile = FILE.read()
print("Your morse :"+ defile)

decodedMessage = ""
for character in defile:
    if character in morsedeCode:
       decodedMessage += morsedeCode[character] + ""
    else:
       decodedMessage += ""
               
print("your morse in password :"+ decodedMessage)
FILE.close()
