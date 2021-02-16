# SECRET-CODE TELEGRAM BOT


### Idea:
Create a bot that can send secret-code to the users. But to get code users must be verified. To get verified users join telegram-chat, where they send command "/getdrops", after that they are added to the whitelist and can get the secret-code in PM with bot. If there is attempt to get the secret-code without being verified - the bot will not send the code BUT will kindly ask the user to join the group and complete all demands.

***
### Functionality:
1. User part:
    * Get the secret-code.
    * Get description.
2. Admin part:
    * Update the secret-code.
    * Manage texts that are send to the user.
    * View all users in the db.
    
    
***
### Technologies:
1. aiogram.
2. asyncpg.
3. python-dotenv.
4. Docker.
5. PostgreSQL.
6. Deployed on the AWS ec-2 user.

(requirements.txt for more details)
