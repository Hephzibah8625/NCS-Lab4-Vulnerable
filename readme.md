# NCS: Lab 4 - Web Security part 2

Shakirov Azamat B20-CS a.shakirov@innopolis.university

Emil Latypov B20-CS e.latypov@innopolis.university



## SQLi



### Description

![image-20230418205831867](/home/azam/.config/Typora/typora-user-images/image-20230418205831867.png)

Page to get information about student's scholarship by ID:

![image-20230418205915988](/home/azam/.config/Typora/typora-user-images/image-20230418205915988.png)

### Weakness

![image-20230418210016901](/home/azam/.config/Typora/typora-user-images/image-20230418210016901.png)

Direct use of a variable from a web query in SQL query



### Exploitation process

![image-20230418210628114](/home/azam/.config/Typora/typora-user-images/image-20230418210628114.png)

The full query will be: **SELECT * FROM Student WHERE id = '1' or 1 = 1;--'**

As 1=1 is always *TRUE* this will return all data from Student table

![image-20230418210645939](/home/azam/.config/Typora/typora-user-images/image-20230418210645939.png)

### Fixing

![image-20230418212833419](/home/azam/.config/Typora/typora-user-images/image-20230418212833419.png)

The best approach is to use built-in arguments parameter in execute function and delete single quotes ('id')

![image-20230418212847800](/home/azam/.config/Typora/typora-user-images/image-20230418212847800.png)



![image-20230418212904136](/home/azam/.config/Typora/typora-user-images/image-20230418212904136.png)

### Deployment

Using docker compose from repository (port is 4005)

https://github.com/Hephzibah8625/NCS-Lab4-Vulnerable/tree/master/sql_injection

![image-20230418214135359](/home/azam/.config/Typora/typora-user-images/image-20230418214135359.png)

### Fixed Code

Repository Link (Directly To Code Line): 

**https://github.com/Hephzibah8625/NCS-Lab4-Fixed/blob/56c4b50377d8263c7af7f16d88d0b5d521cb8f85/sql_injection/app/main.py#L20**

 



## XSS

### Description

![image-20230418222838951](/home/azam/.config/Typora/typora-user-images/image-20230418222838951.png)

Simple page to add comments for image:



![image-20230418223035122](/home/azam/.config/Typora/typora-user-images/image-20230418223035122.png)

And result is:

![image-20230418223043545](/home/azam/.config/Typora/typora-user-images/image-20230418223043545.png)

### Weakness

![image-20230418223240719](/home/azam/.config/Typora/typora-user-images/image-20230418223240719.png)

Text formatting using raw html



### Exploitation process

![image-20230418223447401](/home/azam/.config/Typora/typora-user-images/image-20230418223447401.png)

Result:

![image-20230418223514939](/home/azam/.config/Typora/typora-user-images/image-20230418223514939.png)

### Fixing

![image-20230418223822092](/home/azam/.config/Typora/typora-user-images/image-20230418223822092.png)

Delete raw html in JavaScript part and add text formatting directly to html part of code

Then, result will be:

![image-20230418223920908](/home/azam/.config/Typora/typora-user-images/image-20230418223920908.png)



### Deployment

No need in deployment: Single HTML file, used Vue.js was imported by link

![image-20230418224040123](/home/azam/.config/Typora/typora-user-images/image-20230418224040123.png)

https://hephzibah8625.github.io/NCS-Lab4-Vulnerable/xss/

Link below will open working page

### Fixed Code

Repository Link: 

**https://github.com/Hephzibah8625/NCS-Lab4-Fixed/blob/05fab4a4ec3888f8d8e69ad769419cc5af848543/xss/index.html#L71**

Also working page link: https://hephzibah8625.github.io/NCS-Lab4-Fixed/xss/