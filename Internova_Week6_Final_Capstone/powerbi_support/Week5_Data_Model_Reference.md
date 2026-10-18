# Data Model

Customers[Customer_ID] 1 → * Sales_Clean[Customer_ID]
Products[Product_ID] 1 → * Sales_Clean[Product_ID]

Customers and Products are lookup/dimension tables. Sales_Clean is the transaction/fact table. Use single-direction filtering from dimensions to Sales_Clean.
