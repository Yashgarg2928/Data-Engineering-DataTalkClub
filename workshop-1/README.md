# **What we are building now:**
1. Download CSV data from web
2. Transform and clean the data with pandas
3. Load it into postgreSQL for quying
4. Process data in chunks and heandle larger files
   
### Starting a postgres session in docker 
Its actully fairly easy to use postgres in docker we don't need big setup we just need to give few env variables and a volume where postgres can store there data at. Here is the command which we can use to start postgressession 
```
docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18

  ```
  here we giving user, passward, db as env variable and location to a folder for volume and selecting port. Port is given in this format -p {host port}:{container port} by default postgres listens on port 5432 inside the container and on host but if you have any other service running on port 5432 on host device then change the host port and keep container port same

### Connecting to postgres server 
We are using pgcli to connect to postgres in cli we will need to install it in uv venv by 
1. `uv add --dev pgcli` (--dev flag is used to tell uv to only install this at the time on devlopment not in prodection)
2. Then we can connect to postgres using this `uv run pgcli -h localhost -p 5432 -u root -d ny_taxi` here we will give port of host muchine.
   
   