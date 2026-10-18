# Data Model

- Customers[Customer_ID] (1) → Sales_Clean[Customer_ID] (*)
- Products[Product_ID] (1) → Sales_Clean[Product_ID] (*)

Use single-direction filtering from dimension tables to Sales_Clean. Check that keys are unique in Customers and Products.
