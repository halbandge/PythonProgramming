"""
Rules to create identifier

1. Allowed symbols: a to z, A to Z, 0 to 9 and underscore (_)
2. Identifier should not start with digit
3. Python identifier is case sensitive
4. Reserved keywords can't be used as identifiers
"""

cash = 10  # valid identifier
# ca$h = 20 -> invalid identifier

total123 = 123  # valid identifier
# 123total = 123 -> invalid identifier

total = 10
Total = 20
TOTAL = 30
print(total, Total, TOTAL)  # 10, 20, 30

x = 12 # valid identifier
# if = 13 -> invalid identifier