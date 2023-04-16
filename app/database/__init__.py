from .models import User, SecurityPermission, Base
from .core import DataAccessLayer,Ses
import os

Dal = DataAccessLayer(
    db_url=os.getenv("DATABASE_URL"),
    base=Base,
    pool_recycle=3600,
    pool_size=5,
    max_overflow=10,
    echo=False,
    use_dev=False
)

if not Dal.connect():
    exit(1)


    
