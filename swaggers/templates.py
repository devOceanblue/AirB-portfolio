template = {
    "swagger": "2.0",
    "info": {
        "title": "Airbnb-service-backend API",
        "description": "This is Airbnb-service-backend API",
        "contact": {
            "responsibleOrganization": "Sanfrancisko",
            "responsibleDeveloper": "Jay",
            "email": "neptuner24@gmail.com",
        },
        "termsOfService": "http://airbnb-service.com",
        "version": "0.0.1",
    },
    "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http", "https"],
    "operationId": "getmyData",
    "securitySchemes": {
        "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    },
    "security": {"bearerAuth": []},
}
