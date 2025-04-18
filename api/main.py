from fastapi import FastAPI
from api.routes import auth, users,category,product,address,cart,review,order, dashboard,registerNow , marriage,s_user, s_gallery
from api.database.connection import engine
from api.database.base import Base
from fastapi.middleware.cors import CORSMiddleware


# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust based on your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])

# Include user-related routes
app.include_router(registerNow.router, prefix="/registerNow", tags=["RegisterNow"])

# Include user-related routes
app.include_router(marriage.router, prefix="/marriage", tags=["Marriage"])

# Include produt-related routes
app.include_router(category.router, prefix="/category", tags=["Category"])

# Include produt-related routes
app.include_router(product.router, prefix="/product", tags=["Product"])

# Include produt-related routes
app.include_router(address.router, prefix="/address", tags=["Address"])

# Include produt-related routes
app.include_router(cart.router, prefix="/cart", tags=["Cart"])

# Include produt-related routes
app.include_router(order.router, prefix="/order", tags=["Order"])

# Include produt-related routes
app.include_router(review.router, prefix="/review", tags=["Review"])

app.include_router(dashboard.router, prefix="/dashbord", tags=["Dashboard"])


app.include_router(s_user.router, prefix="/student", tags=["Student"])

app.include_router(s_gallery.router, prefix="/school", tags=["Gallery"])
