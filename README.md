# Codex
It is just a practice to create a non-standard encoding and decoding method.
# How to use
1-. Instance to create the object in case of encoding or decoding.
2-. To encode you have to give the following values: data, subsequence and expansion.
3-. To decode, it was thought in a way that you can do it without having to pass everything again in the init of the class since everything goes with the same structure coded in the longstr like this mirror_value/mirror_value/mirror_value$subsequence_value-expansion_value

# Example Coding:
#codex = Codex(data="Hola", subsequence="64", expansion=12)
#codex = Codex(data="Hola", subsequence="64")
#codex = Codex(data="Hola", expansion=12)
#print("Encode Text result:", codex.code())

# Example Decoding
Both methods: #NTc=/Mzg=/MzQ=/MjM=$64-12
Subsequence 85 method: #G&K/GBy/GBN/F);$85-
Subsequence 64 method: #NDU=/MjY=/MjI=/MTE=$64-
Expansion method: #57/38/34/23$-12

#codex = Codex()
#print("Decode Text result:", codex.decode('G&K/GBy/GBN/F);$85-'))
