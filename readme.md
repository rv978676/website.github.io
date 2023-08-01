Title: Stock Inventory App Project Report

Team Name: TechGurus

Team Members:
1. John Smith
2. Jane Doe
3. Michael Johnson

## A. Objectives of the App

The primary objective of the "Stock Inventory" app is to build a comprehensive stock control and monitoring (SCM) system for a shop that sells Arduino Microcontrollers and associated electronic components. The app aims to streamline the inventory management process and provide a user-friendly interface for various tasks, including adding new stock items, monitoring current stock levels, restocking low stock items, and simulating an Electronic Point of Sale (EPOS) system.

## B. Targeted Users

The targeted users of the app include:

1. Admin: Responsible for managing the stock inventory, adding new products, and restocking low stock items.
2. Employees: Authorized users who can use the app to access the till functionality and serve customers.
3. Branch Managers (if applicable): Can access branch-specific data and monitor sales in their respective locations.

## C. Details of Functionalities

1. **Feature 1: Add Stock Item**
   - Only visible to the admin user.
   - Allows the admin to add new items to the stock with information such as barcode number, product name, photo, wholesale price, retail price, and quantity.
   - If a product with the same barcode already exists, the system updates the existing record and increments the quantity accordingly.

2. **Feature 2: View Current Stock Inventory**
   - Visible to all logged-in users.
   - Displays the current stock inventory, including product name, wholesale unit price, retail price, and quantity in stock.
   - Calculates and displays the total stock value based on the wholesale price and quantity.

3. **Feature 3: Restock Low Stock Items**
   - Visible to the admin user.
   - Shows products with low stock levels for restocking.
   - Admin can place orders for these items, specifying the quantity to be ordered (within the range of 1-100).
   - Orders can be marked as received, which updates the stock levels accordingly.

4. **Feature 4: Electronic Point of Sale (EPOS)**
   - Visible to all users except the admin.
   - Simulates an EPOS system, where users can add items to the shopping cart by scanning their barcode.
   - Calculates the total cost and allows users to proceed with the checkout process.

## D. Use Case Diagram

*(Use case diagram goes here)*

## E. Details of Data Involved

The app primarily deals with the following data:

1. Product Data:
   - Barcode number (numeric)
   - Product name (text)
   - Product photo (media file)
   - Wholesale price (numeric range: £1-£30)
   - Retail price (numeric range: £1-£30)
   - Quantity in stock (numeric range: 1-100)

2. User Accounts:
   - Username (text)
   - Password (encrypted)

3. Order Data:
   - Order ID (numeric)
   - Product name (text)
   - Quantity ordered (numeric)

## F. Details of System Architecture

The Stock Inventory app follows a client-server architecture:

1. Client-Side:
   - Developed using modern web technologies and frameworks.
   - Users interact with the app through a user-friendly web interface.
   - Supports various functionalities based on the user's role (admin, employee, branch manager).

2. Server-Side:
   - Handles the business logic, data processing, and interactions with the database.
   - Utilizes RESTful APIs to communicate with external services if required (e.g., LocationIQ for mapping).

3. Database:
   - Stores product data, user accounts, and order information.
   - Can be implemented using a relational database management system (RDBMS) or NoSQL database, depending on scalability requirements.

## G. Screenshots of the App

*(Include relevant screenshots showcasing the app's key features and user interfaces)*

## Conclusion

The Stock Inventory app aims to provide an efficient stock control and monitoring system for a shop selling Arduino Microcontrollers and electronic components. It caters to different user roles, such as admins, employees, and branch managers, to facilitate various inventory-related tasks. The app's user-friendly interface, coupled with functionalities like adding stock items, viewing inventory, restocking low stock items, and simulating an EPOS system, enhances the shop's overall efficiency and customer service. Additionally, incorporating features like using device sensors for branch location tracking and media uploads further improves the app's usability and convenience for the end-users.

Overall, the Stock Inventory app is a valuable tool for any shop dealing with electronic components, empowering them to manage their inventory effectively, streamline operations, and provide excellent service to their customers.








# Stock Inventory App Project Report

## Team Name: TechGurus

### Team Members:
1. John Smith
2. Jane Doe
3. Michael Johnson

---

## Table of Contents

1. **Introduction**
    - Project Name: Stock Inventory App
    - Objectives of the App
    - Targeted Users

2. **Functionalities**
    - Feature 1: Add Stock Item
    - Feature 2: View Current Stock Inventory
    - Feature 3: Restock Low Stock Items
    - Feature 4: Electronic Point of Sale (EPOS)
    - Extras: Sensor and Media Implementations

3. **Use Case Diagram**

4. **Data Involved**
    - Product Data
    - User Accounts
    - Order Data

5. **System Architecture**

6. **Screenshots of the App**

7. **Conclusion**

---

## 1. Introduction

### Project Name: Stock Inventory App

The Stock Inventory app is a stock control and monitoring (SCM) system designed for a shop that sells Arduino Microcontrollers and associated electronic components. The app aims to streamline the inventory management process and provide an intuitive interface for various stock-related tasks, including adding new items, tracking current stock levels, restocking low stock items, and managing sales through an Electronic Point of Sale (EPOS) system.

### Objectives of the App

The main objectives of the Stock Inventory app are:

1. To simplify stock control and monitoring for the shop by providing an easy-to-use interface for managing inventory.
2. To enable the admin to add new stock items, update existing products, and track stock quantities effectively.
3. To provide employees with an EPOS system to efficiently manage sales and update stock levels after each transaction.
4. To incorporate extra features like sensors, media uploads, and API integration to enhance the user experience.

### Targeted Users

The Stock Inventory app caters to the following user categories:

1. **Admin:** Responsible for managing the entire inventory, adding new products, and restocking low stock items.
2. **Employees:** Authorized users who can access the EPOS system to process sales and update stock levels after each transaction.

## 2. Functionalities

### Feature 1: Add Stock Item

The home screen of the app is accessible only to logged-in users. If the user is the admin, they can see an "Add stock item" button, which takes them to a screen to add new products to the inventory. The following information is requested for each new product:

1. Product Barcode Number: Only accepts numbers of the correct length.
2. Product Name: Text input for the name of the product.
3. Product Photo: Allows the admin to upload a photo of the product.
4. Wholesale Price Slider: A slider with the range £1-£30 for the admin to enter the wholesale price (price paid per unit).
5. Retail Price Slider: A slider with the range £1-£30 for the admin to enter the retail price (the price the product will be sold for).
6. Quantity Slider: A slider with the range 1-100 for the admin to enter the quantity of products to be added.

If the admin adds a product with the same barcode as an existing one, the app updates the existing record with the new information and calculates the new quantity as the sum of the existing quantity and the one just added. This indicates that the admin has increased the stock levels and updated the product information.

> To demonstrate this feature and verify the form's correctness, the app performs data persistence through database queries or API calls depending on the platform and technology used.

### Feature 2: View Current Stock Inventory

When any user logs in, the home screen displays the current stock inventory. For each product range in stock, the following details are shown:

1. Product Name
2. Wholesale Unit Price
3. Retail Price
4. Quantity in Stock

At the top of the screen, the app calculates and displays the current stock value by multiplying the wholesale price by the quantity for each product and adding these values. This value represents how much money is tied up in stock.

If the stock level for a product is 5 or less, the app flags the item as "low stock levels."

### Feature 3: Restock Low Stock Items

When the admin user logs in, they see a "Restock" button or link along with a "Received stock" button or link.

The "Restock" button takes the admin to a screen displaying products flagged as "low stock levels." This screen shows the same information for each product as listed in **Feature 2**, but it includes a slider next to each item for indicating the number of units being ordered (within the range of 1-100).

There is a "Place order" button or link that simulates sending the order to the wholesaler.

The "Received stock" button takes the admin to a screen listing all the placed orders, including the items and their quantities.

Next to each order, there is a "Received" button. Clicking this button performs the following actions:

1. Increases the stock levels by the quantity in the order.
2. Updates the list, removing the item that was just received.

This allows the admin to check off the received items against the ordered list and update the stock levels accordingly.

### Feature 4: Electronic Point of Sale (EPOS)

When any user other than the admin logs in, they see a "Till" button, which takes them to a screen simulating an Electronic Point of Sale (EPOS) system commonly used in modern shop tills.

The screen initially displays an empty shopping cart and a single textbox that is automatically selected by the cursor.

The shop worker uses the numeric keypad to enter the barcode number of the item and presses the enter key. This action triggers the following:

1. The app looks up the barcode and adds the product name to the shopping cart along with its price.
2. The app updates the total cost of the items in the cart.
3. The barcode number is deleted, but the textbox remains selected, ready for the shop worker to enter the next barcode.

Once the first item is added to the cart, the screen displays a "Checkout" button or link. Clicking this button initiates the following actions:

1. The app prints the contents of the shopping cart, providing a summary of the items and their prices.
2. The app updates the stock levels based on the items sold during the transaction.
3. The shopping cart is cleared, and the empty textbox is selected again, ready for the next customer.

### Extras: Sensor and Media Implementations

To earn extra marks, the app will incorporate the following sensor and media features:

#### Sensors

1. **Location Sensor:** Each sale captures the current location, which is compared to the branch locations. The sale is then allocated to the nearest match branch.
2. **Camera Sensor:** When prompted for a photo, the user is given access to the device camera (if available).
3. **Map Integration:** The admin can view a map showing the branch locations. Clicking on a pin shows the name of the branch in a bubble, and clicking on the bubble redirects the admin to the branch summary page showing the tracking data.

#### Media

1. **Upload and Capture Options:** In addition to uploading photos, the app will provide users with the choice of uploading photos, video clips, or audio clips. Furthermore, users can directly capture images, audio, and video clips using the built-in

 camera and/or microphone if available.

## 3. Use Case Diagram

*(Use case diagram goes here)*

## 4. Data Involved

The app deals with the following data:

1. **Product Data:**
   - Barcode number (numeric)
   - Product name (text)
   - Product photo (media file)
   - Wholesale price (numeric range: £1-£30)
   - Retail price (numeric range: £1-£30)
   - Quantity in stock (numeric range: 1-100)

2. **User Accounts:**
   - Username (text)
   - Password (encrypted)

3. **Order Data:**
   - Order ID (numeric)
   - Product name (text)
   - Quantity ordered (numeric)

## 5. System Architecture

The Stock Inventory app follows a client-server architecture:

1. **Client-Side:**
   - Developed using modern web technologies and frameworks.
   - Users interact with the app through a user-friendly web interface.
   - Supports various functionalities based on the user's role (admin, employee).

2. **Server-Side:**
   - Handles the business logic, data processing, and interactions with the database.
   - Utilizes RESTful APIs to communicate with external services like LocationIQ for mapping.

3. **Database:**
   - Stores product data, user accounts, and order information.
   - Can be implemented using a relational database management system (RDBMS) or NoSQL database, based on scalability requirements.

## 6. Screenshots of the App

*(Include relevant screenshots showcasing the app's key features and user interfaces)*

## 7. Conclusion

The Stock Inventory app is a powerful tool designed to streamline the stock control and monitoring process for a shop dealing with Arduino Microcontrollers and electronic components. By providing features like adding stock items, viewing current inventory, restocking low stock items, and implementing an EPOS system, the app empowers administrators and employees to efficiently manage stock levels and sales operations.

Additionally, the incorporation of extra features such as sensor data utilization for location tracking, media uploads, and API integration enhances the user experience and functionality of the app. The app's user-friendly interface, coupled with its comprehensive functionalities, makes it a valuable asset for any shop looking to optimize their inventory management and improve overall efficiency.

Through the implementation of the Stock Inventory app, our team, TechGurus, has demonstrated proficiency in software development and created a practical solution for efficient stock control and monitoring. The app's flexibility and potential for expansion further ensure its relevance and utility in various business scenarios.



