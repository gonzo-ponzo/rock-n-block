### Make sure that you have **Docker** and **make** installed

---

### **Quick start**

1. Install requirements with **requirements.txt** in **{Project DIR}/backend** folder
2. Fill .env file with .env_example in **{Project DIR}/backend** folder
3. Start DB services with `make up` command
4. Run app with `make back` command

---

Visit http://localhost:8000/docs after app start up to learn API routes

---

### Make commands

`make up` POSTGRESQL container start up

`make down` POSTGRESQL container shut down

`make back` App start up and apply migrations
