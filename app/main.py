from fastapi import FastAPI
from app.routes import user_routes, seva_routes, submission_routes, auth_routes, report_routes

app = FastAPI(title="Seva Management Backend")

#include routes
app.include_router(auth_routes.router)
app.include_router(seva_routes.router)
app.include_router(submission_routes.router)
app.include_router(user_routes.router)
app.include_router(report_routes.router)



@app.get("/")
def root():
    return {"message": "Seva Management Backend Running"}
