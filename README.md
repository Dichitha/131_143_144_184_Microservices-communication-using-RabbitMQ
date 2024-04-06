# Microservices-communication-using-RabbitMQ
1. Clone the github repository
2. Start docker engine
3. Go to the project directory, open the terminal and run **docker-compose up --build**
4. Open the localhost of rabbitMQ ( localhost:15672 )
5. Navigate to the Exchange option and verify if the `microservices` exchange is available. If not, click on `Add a new exchange`
   * Name: microservices
   * Type: direct
   * Durability: Durable
6. Click on the Add exchange.
7. Stop all the containers running by pressing Ctrl + C.
8. Again run docker-compose up --build
9. Go to localhost:5000 in your browser. You should now be able to access the website.
10. Click on the Health Check option. It will show a message, "Health Check Message Sent"

### Database is not getting stored for now. This is just for checking the connection with rabbitMQ. We need to make lot of changes ;)
