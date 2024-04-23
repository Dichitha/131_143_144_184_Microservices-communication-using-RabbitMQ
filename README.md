# 131_143_144_184_Microservices_communication_using_RabbitMQ
Cloud computing project

To run the code:
1) Modify the SQL database credentials in producer and consumer files.
2) Create a database named "ims"
3) Run the db.sql file to create all tables with the necessary fields.
4) Run `docker-compose build`
5) Run `docker-compose up`
6) The application runs on localhost port `localhost:5000/`
7) Visit localhost:15672 to see RabbitMQ queues and messages using username:guest and password: guest
