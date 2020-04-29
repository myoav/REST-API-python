----
  **POST**
----

* **URL**

  /https://restapiyoav88.herokuapp.com/api/users

* **Method:**
  
  `POST`
  
*  **URL Params**

	None
  

* **Data Params**

	ID = [string[32]],
    Nickname = [string[11]],
    User name = [string[50]],
	Password = [string[200]],
    Status= [int[4]].

* **Success Response:**
  
  * **Code:** 200 
    **Content:** {
					  "ID": string,
					  "Nickname": string,
					  "Status": int,
					  "User name": string,
					  "create_time": "Wed, 29 Apr 2020 08:18:00 GMT"
				 }
	
* **Error Response:**
  
  * **Code:** 404  
    **Content:** `NOT FOUND`
  
  * **Code:** 400  
    **Content:** `INVALID INPUT`
----
  **Get**
----

* **URL**
	
  /https://restapiyoav88.herokuapp.com/api/admin/users

* **Method:**
  
  `GET`
  
*  **URL Params**

	None
  

* **Data Params**

	None

* **Success Response:**
  
  * **Code:** 200 
    **Content:** `Users : {"All users of the database"}`
	

