up:
	cd backend && docker compose -f docker-compose.yaml up -d --build

down:
	cd backend && docker compose -f docker-compose.yaml down && docker network prune --force 

back:
	cd backend && uvicorn main:app --reload