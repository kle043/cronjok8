import sys
import os
import uvicorn
from .server import app

def main(args=None):
    uvicorn.run(app, host="0.0.0.0", port=os.getenv('PORT', 8000))

if __name__ == "__main__":
    sys.exit(main())
